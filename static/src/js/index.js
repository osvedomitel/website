document.addEventListener('DOMContentLoaded', () => {
    initScript();
});

const initScript = () => {
    const menuButton = document.querySelector('#navigation-button');
    const navigation = document.querySelector('#navigation-wrapper');
    const navItems = document.querySelectorAll('.navigation__item');
    const titleMobile = document.querySelector('#header-title--mobile');
    const titleDesktop = document.querySelector('#header-title--desktop');

    const setMobile = () => {
        menuButton.classList.remove('nodisplay');
        navigation.classList.add('nodisplay');
        titleDesktop.classList.add('nodisplay');
        titleMobile.classList.remove('nodisplay');
    };

    const setDesktop = () => {
        menuButton.classList.add('nodisplay');
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

    const handleResize = () => {
        if (this.window.screen.width < 1200) {
            setMobile();
        } else {
            setDesktop();
        }
    };

    handleResize();

    window.addEventListener('resize', () => {
        handleResize();
    });

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            hideNav();
        })
    });

    menuButton.addEventListener('click', () => {
        if (navigation.classList.contains('nodisplay')) {
            showNav();
        } else {
            hideNav();
        }
    });
};
