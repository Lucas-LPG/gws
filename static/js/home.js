const capacityLevel = document.querySelector(".capacity-level");
capacityLevel.style.height = parseInt(document.getElementById("peopleInfo").innerText) + "%";

const temperatureLevel = document.querySelector(".temperature-level");
temperatureLevel.style.height = parseInt(document.getElementById("temperatureInfo").innerText) + "%";
