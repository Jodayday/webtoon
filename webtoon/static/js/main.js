// var dayButtons = document.querySelectorAll(".day");

// dayButtons.forEach(function (button) {
//   button.addEventListener("click", function () {
//     var value = this.value;
//     var url = new URL(window.location.href);
//     url.pathname = "/webtoon/list/";
//     url.searchParams.set("day", value);
//     window.location.href = url.toString();
//   });
// });
document.addEventListener("DOMContentLoaded", function () {
  var dayButtons = document.querySelectorAll(".day");

  dayButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var value = this.value;
      var url = new URL(window.location.href);
      url.searchParams.set("day", value);
      url.searchParams.set("page", 1);
      window.location.href = url.toString();
    });
  });
});
document.addEventListener("DOMContentLoaded", function () {
  var navButtons = document.querySelectorAll(".navbut");

  navButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var value = this.value;
      var url = new URL(window.location.href);
      url.searchParams.set("status", value);
      url.searchParams.set("page", 1);
      window.location.href = url.toString();
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var tagButtons = document.querySelectorAll(".tag");

  tagButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var value = this.value;
      console.log(value);
      var url = new URL(window.location.href);
      url.searchParams.set("tag", value);
      url.searchParams.set("page", 1);
      window.location.href = url.toString();
    });
  });
});
document.addEventListener("DOMContentLoaded", function () {
  var tagButtons = document.querySelectorAll(".page");

  tagButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var value = this.value;
      console.log(value);
      var url = new URL(window.location.href);
      url.searchParams.set("page", value);
      window.location.href = url.toString();
    });
  });
});
