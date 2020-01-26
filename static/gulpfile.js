const { src, dest, watch } = require('gulp');

const autoprefixer = require('gulp-autoprefixer');
const concat = require('gulp-concat');
const csso = require('gulp-csso');
const merge = require('merge-stream');
const less = require('gulp-less');

function css(cb) {
	merge(
		src('node_modules/normalize.css/normalize.css'),
		src('src/less/style.less')
			.pipe(less())
	)
		.pipe(concat('style.css'))
		.pipe(autoprefixer())
		.pipe(csso({
			comments: false,
			restructure: false
		}))
		.pipe(dest('dist'));

	cb();
};

function js(cb) {
	src('src/js/*.js')
		.pipe(concat('script.js'))
		.pipe(dest('dist'));

	cb();
};

exports.css = css;
exports.js = js;

exports.build = parallel(js, css);

exports.default = function() {
	watch('src/less/*.less', { ignoreInitial: false }, css);
	watch('src/js/*.js', { ignoreInitial: false }, js);
};

