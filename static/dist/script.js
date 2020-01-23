document.addEventListener('DOMContentLoaded', () => {
    init();
});

const init = () => {
    const navigationButton = document.querySelector('#navigation-button');
    const navigation = document.querySelector('#navigation-wrapper');
    const navItems = document.querySelectorAll('.navigation__item');

    const setMobile = () => {
        navigationButton.classList.remove('nodisplay');
        navigation.classList.add('nodisplay');
    };

    const setDesktop = () => {
        navigationButton.classList.add('nodisplay');
        navigation.classList.remove('nodisplay');
    };

    const showNav = () => {
        navigation.classList.remove('nodisplay');
    };

    const hideNav = () => {
        navigation.classList.add('nodisplay');
    };

    const resize = () => {
        if (this.window.screen.width < 1200) {
            setMobile();
        } else {
            setDesktop();
        }
    };

    resize();

    window.addEventListener('resize', function() {
        resize();
    });

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            hideNav();
        })
    })

    navigationButton.addEventListener('click', () => {

        if (navigation.classList.contains('nodisplay')) {
            showNav();
        } else {
            hideNav();
        }
    });
};