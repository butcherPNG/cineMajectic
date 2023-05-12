const leftBtn = document.querySelector(".slider-control-left");
const rightBtn = document.querySelector(".slider-control-right");
const sliderImages = document.querySelector(".slider-images");

let counter = 0;

leftBtn.addEventListener("click", () => {
  if (counter === 0) {
    counter = sliderImages.children.length - 1;
  } else {
    counter--;
  }
  sliderImages.style.transform = `translateX(-${counter * 33.33}%)`;
});

rightBtn.addEventListener("click", () => {
  if (counter === sliderImages.children.length - 1) {
    counter = 0;
  } else {
    counter++;
  }
  sliderImages.style.transform = `translateX(-${counter * 33.33}%)`;
});

