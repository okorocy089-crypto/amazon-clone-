(function () {
  const track = document.getElementById("hero-track");
  const prevBtn = document.getElementById("hero-prev");
  const nextBtn = document.getElementById("hero-next");
  if (!track) return;

   const realSlides = Array.from(track.children);
  const slideCount = realSlides.length;
 
  const firstClone = realSlides[0].cloneNode(true);
  track.appendChild(firstClone);
 
  let currentIndex = 0;
  let isTransitioning = false;
 
  function render(withTransition = true) {
    track.style.transition = withTransition ? "transform 0.5s ease" : "none";
    track.style.transform = `translateX(-${currentIndex * 100}%)`;
  }
 
  function goNext() {
    if (isTransitioning) return;
    isTransitioning = true;
    currentIndex += 1;
    render(true);
  }
 
  function goPrev() {
    if (isTransitioning) return;
    isTransitioning = true;
    if (currentIndex === 0) {
      currentIndex = slideCount;
      render(false);
      requestAnimationFrame(() => {
        currentIndex -= 1;
        render(true);
      });
    } else {
      currentIndex -= 1;
      render(true);
    }
  }
 
  track.addEventListener("transitionend", () => {
    isTransitioning = false;
    if (currentIndex === slideCount) {
      currentIndex = 0;
      render(false);
    }
  });
 
  prevBtn.addEventListener("click", goPrev);
  nextBtn.addEventListener("click", goNext);
 
  render(false);
 
  let autoplay = setInterval(goNext, 6000);
  track.parentElement.addEventListener("mouseenter", () => clearInterval(autoplay));
  track.parentElement.addEventListener("mouseleave", () => {
    autoplay = setInterval(goNext, 6000);
  });
})();