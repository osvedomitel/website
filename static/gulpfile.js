const { src, dest, watch } = require('gulp');
const autoprefixer = require('gulp-autoprefixer');


function css(cb) {
	src('src/style.css')
		.pipe(autoprefixer())
		.pipe(dest('dist'));
	cb();
};


exports.css = css;

exports.default = function() {
	watch('src/*.css', css);
};
