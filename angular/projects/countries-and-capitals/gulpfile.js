var gulp = require('gulp'); 
var connect = require('gulp-connect');
var uglify = require('gulp-uglify');
var minifyCss = require('gulp-minify-css');
var usemin = require('gulp-usemin');
var jshint = require('gulp-jshint')
var rev = require('gulp-rev');
var del = require('del');

//del is rimraf with support for multiple files and globbing.
gulp.task('clean', function(cb){
  del(['build/partials', 'build/assets'], cb)
});

//copy-files has clean as a dependency, will call it, and then
//wait for it to complete before copy-files runs:
gulp.task('copy-files', ['clean'], function() {
  gulp.src(['./app/**/*.html', '!./app/index.html'], {base: './app'})
    .pipe(gulp.dest('build/'));
  gulp.src(['./app/img/*'], {base: './app'})
    .pipe(gulp.dest('build/assets/'));
});

gulp.task('lint', function(){
  gulp.src(['./app/partials/**/*.js', './app/index.js'])
    .pipe(jshint())
    .pipe(jshint.reporter('default'))
});

//usemin has copy-files as a dependency, will call it, and then
//wait for it to complete before usemin runs:
gulp.task('usemin', ['copy-files'], function() {
  gulp.src('./app/index.html')
    .pipe(usemin({
      css: [minifyCss(), 'concat', rev()],
      js: [uglify(), rev()]
    }))
    .pipe(gulp.dest('build/'));
});

gulp.task('connect', function() {
  connect.server({
    root: 'app/'
  });
});

gulp.task('runbuild', function(){
  connect.server({
    root: 'build/'
  });
});

// Default Task
gulp.task('default', ['connect']);
gulp.task('build', ['lint', 'usemin']);
