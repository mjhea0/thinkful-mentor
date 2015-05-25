var gulp = require('gulp'),
    connect = require('gulp-connect'),
    jshint = require('gulp-jshint');

gulp.task('lint', function(){
  gulp.src(['./*.js'])
    .pipe(jshint())
    .pipe(jshint.reporter('default'));
});

gulp.task('connect', function() {
  connect.server({
    root: './app'
  });
});

// Default Task
gulp.task('default', ['connect', 'lint']);
