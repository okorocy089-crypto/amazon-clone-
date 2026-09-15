document.addEventListener('DOMContentLoaded', function () {
    const bottomHeader = document.querySelector('.header-bottom');
    if (!bottomHeader) return;
    if (window.innerWidth > 700) return;

    let lastScrollY = window.scrollY;
    let ticking = false;

    function onScroll() {
        const currentScrollY = window.scrollY;

        if (currentScrollY < lastScrollY) {
            // scrolling UP -> hide
            bottomHeader.classList.add('hidden-mobile');
        } else if (currentScrollY > lastScrollY) {
            // scrolling DOWN -> show
            bottomHeader.classList.remove('hidden-mobile');
        }

        lastScrollY = currentScrollY;
        ticking = false;
    }

    window.addEventListener('scroll', function () {
        if (!ticking) {
            window.requestAnimationFrame(onScroll);
            ticking = true;
        }
    }, { passive: true });
});