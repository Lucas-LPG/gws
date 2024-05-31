let peoplePercentage = parseInt(
  document.getElementById("peopleInfo").innerHTML,
);

const capacityLevel = document.querySelector(".capacity-level");

console.log(capacityLevel);
capacityLevel.style.height = peoplePercentage + "%";

const temperatureDiv = document.querySelector(".temperature-count");
let currentTemperature = parseInt(temperatureDiv.innerHTML.split("°"[0]));
const temperatureLevel = document.querySelector(".temperature-level");

temperatureLevel.style.height = currentTemperature + "%";
