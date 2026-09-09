document.addEventListener('DOMContentLoaded', function () {
    const bottomHeader = document.querySelector('.header-bottom');
    const footer = document.querySelector('.site-footer');

    if (!bottomHeader || !footer) return;
    if (window.innerWidth > 700) return; // mobile-only behavior

    let hidden = false;

    function hideBottomHeader() {
        if (!hidden) {
            bottomHeader.classList.add('hidden-mobile');
            hidden = true;
        }
    }

    function showBottomHeader() {
        if (hidden) {
            bottomHeader.classList.remove('hidden-mobile');
            hidden = false;
        }
    }

    // Hide as soon as the user starts scrolling down at all
    let lastScrollY = window.scrollY;
    window.addEventListener('scroll', function () {
        if (window.scrollY > lastScrollY && window.scrollY > 40) {
            hideBottomHeader();
        }
        lastScrollY = window.scrollY;
    }, { passive: true });

    // Reveal again once the footer scrolls into view ("rock bottom")
    const footerObserver = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                showBottomHeader();
            } else if (window.scrollY > lastScrollY) {
                hideBottomHeader();
            }
        });
    }, { threshold: 0.01 });

    footerObserver.observe(footer);
});