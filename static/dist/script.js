document.addEventListener('DOMContentLoaded', () => {
    initScript();
});

const initScript = () => {
    const navigationButton = document.querySelector('#navigation-button');
    const navigation = document.querySelector('#navigation-wrapper');
    const navItems = document.querySelectorAll('.navigation__item');
    const titleMobile = document.querySelector('#header-title--mobile');
    const titleDesktop = document.querySelector('#header-title--desktop');

    const setMobile = () => {
        navigationButton.classList.remove('nodisplay');
        navigation.classList.add('nodisplay');
        titleDesktop.classList.add('nodisplay');
        titleMobile.classList.remove('nodisplay');
    };

    const setDesktop = () => {
        navigationButton.classList.add('nodisplay');
        navigation.classList.remove('nodisplay');
        titleDesktop.classList.remove('nodisplay');
        titleMobile.classList.add('nodisplay');
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