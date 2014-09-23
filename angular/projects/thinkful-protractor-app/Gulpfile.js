var gulp = require('gulp');
var shell = require('gulp-shell');
var nodemon = require('gulp-nodemon');
var protractor = require("gulp-protractor").protractor;
var fs = require('fs');

gulp.task('install', function() {
  gulp.src('api/install.js')
    .pipe(shell([
      'node api/install.js'
    ])); 
});

gulp.task('install:test', function() {
  gulp.src('api/install.js')
    .pipe(shell([
      'NODE_ENV=TEST node api/install.js'
    ])); 
});

function expressServer(port, env) {
  env = env || 'DEVELOPMENT'
  nodemon({
    script: 'server.js',
    ext: 'js json',
    verbose : true,
    ignore: ['ignored.js', './node_modules', './frontend'],
    env: {
      'NODE_ENV': env,
      'PORT': port
    }, 
    nodeArgs: [env == 'DEVELOPMENT' ? '--debug=9999' : '--debug=9898']
  });
};

gulp.task('serve:dev', function() {
  expressServer(8888);
});

gulp.task('serve:test', function() {
  expressServer(7777, 'TEST');
});

function runProtractor(debug) {
  return function() {
    var args = ['--baseUrl', 'http://127.0.0.1:8000'];
    if(debug) {
      args.unshift('debug');
    }
    gulp.src(["./e2e-tests/**/*Spec.js"])
        .pipe(protractor({
            configFile: "protractor.js",
            args: args
        })) 
        .on('error', function(e) { throw e })
  }
}

gulp.task('run-e2e-tests', runProtractor());
gulp.task('debug-e2e-tests', runProtractor(true));

gulp.task('default', ['serve:dev']);

gulp.task('test:e2e', ['install:test', 'run-e2e-tests']);
gulp.task('test:e2e:debug', ['install:test', 'debug-e2e-tests']);
