window.onload = function () {
  const navbar = document.querySelector("nav");
  navbar.addEventListener("mouseover", function () {
    navbar.style.opacity = 1;
  });
  navbar.addEventListener("mouseout", function () {
    navbar.style.opacity = 0;
  });
};
