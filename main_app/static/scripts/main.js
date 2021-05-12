console.log("[main.js] Loaded");

$(".navbar-burger").click(function () {
  // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
  $(".navbar-burger").toggleClass("is-active");
  $(".navbar-menu").toggleClass("is-active");
});

$(".dropdown").click(function () {
  $(this).toggleClass("is-active");
});
