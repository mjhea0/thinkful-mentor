// gulp
var gulp = require('gulp');

// plugins
var gutil = require('gulp-util');
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');
var minifyCSS = require('gulp-minify-css');
var concat = require('gulp-concat');
var clean = require('gulp-clean');
var connect = require('gulp-connect');

gulp.task('lint', function() {
    gulp.src(['./app/**/*.js', '!./app/bower_components/**'])
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

gulp.task('clean', function() {
    gulp.src('./dist/*')
        .pipe(clean({force: true}));
});

gulp.task('minify-css', function() {
    var opts = {comments:true,spare:true};
    gulp.src(['./app/**/*.css', '!./app/bower_components/**'])
       .pipe(minifyCSS(opts))
       .pipe(gulp.dest('./dist/'))
});

gulp.task('minify-js', function() {
    gulp.src(['./app/**/*.js', '!./app/bower_components/**'])
        .pipe(uglify({
    	    // inSourceMap:
    	    // outSourceMap: "app.js.map"
        }))
        .pipe(gulp.dest('./dist/'))
});

gulp.task('copy-bower-components', function () {
    gulp.src('./app/bower_components/**')
      .pipe(gulp.dest('dist/bower_components'));
});

gulp.task('copy-html-files', function () {
    gulp.src('./app/**/*.html')
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

// Default
gulp.task('default',
    ['lint', 'connect']
);


gulp.task('build',
    ['lint', 'minify-css', 'minify-js', 'copy-html-files', 'copy-bower-components', 'connectDist']
);

