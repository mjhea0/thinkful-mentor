// include gulp
var gulp = require('gulp');

// include plug-ins
var jshint = require('gulp-jshint');
var connect = require('gulp-connect');
var uglify = require('gulp-uglify');
var minifyHtml = require('gulp-minify-html');
var minifyCss = require('gulp-minify-css');
var usemin = require('gulp-usemin');
var rev = require('gulp-rev');
var clean = require('gulp-clean');

// JS hint task
gulp.task('jshint', function() {
    gulp.src(['./app/**/*.js', '!./app/bower_components/**'])
    .pipe(jshint())
    .pipe(jshint.reporter('default'));
});

gulp.task('copy-html-files', function () {
    gulp.src(['./app/**/*.html', '!./app/index.html'], { base: './app' })
      .pipe(gulp.dest('dist/'));
});

gulp.task('usemin', function () {
    gulp.src('./app/index.html')
      .pipe(usemin({
          css: [minifyCss(), 'concat', rev()],
          js: [uglify(), rev()]
      }))
      .pipe(gulp.dest('dist/'));
});

gulp.task('connect', function () {
    connect.server({
        root: 'app/',
        port: 8888
    });
});

gulp.task('connectDist', function () {
    connect.server({
        root: 'dist/',
        port: 8090
    });
});

// Default Task
gulp.task('default', ['connect']);
gulp.task('build', ['copy-html-files', 'usemin']);