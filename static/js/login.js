document.addEventListener("DOMContentLoaded", function () {
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    document.documentElement.style.setProperty("--custom-dark", "#f7f7f7");
    document.documentElement.style.setProperty("--custom-light", "#0d0d0d");
    document.documentElement.style.setProperty("--custom-blue", "#EB5939");
    document.documentElement.style.setProperty("--card-head", "#121212");
    document.documentElement.style.setProperty("--card-surface", "#212121");
  } else {
    document.documentElement.style.setProperty("--custom-dark", "#0d0d0d");
    document.documentElement.style.setProperty("--custom-light", "#f7f7f7");
    document.documentElement.style.setProperty("--custom-blue", "#005acd");
    document.documentElement.style.setProperty("--card-head", "#ececec");
    document.documentElement.style.setProperty("--card-surface", "#fff");
  }
});
