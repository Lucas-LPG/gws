const sensorsBtn = document.getElementById("sensorsBtn");
const actuatorsBtn = document.getElementById("actuatorsBtn");

const sensorsBody = document.getElementById("sensorsBody");
const actuatorsBody = document.getElementById("actuatorsBody");

let showSensors = true;
let showActuators = true;

sensorsBtn.addEventListener("click", () => {
  if (showSensors) {
    sensorsBody.style.height = "0px";
    sensorsBody.style.overflow = "hidden";
    sensorsBtn.classList.remove("fa-chevron-down");
    sensorsBtn.classList.add("fa-chevron-up");
  } else {
    sensorsBody.style.height = "";
    sensorsBody.style.overflow = "";
    sensorsBtn.classList.remove("fa-chevron-up");
    sensorsBtn.classList.add("fa-chevron-down");
  }

  showSensors = !showSensors;
});

actuatorsBtn.addEventListener("click", () => {
  if (showActuators) {
    actuatorsBody.style.height = "0px";
    actuatorsBody.style.overflow = "hidden";
    actuatorsBtn.classList.remove("fa-chevron-down");
    actuatorsBtn.classList.add("fa-chevron-up");
  } else {
    actuatorsBody.style.height = "";
    actuatorsBody.style.overflow = "";
    actuatorsBtn.classList.remove("fa-chevron-up");
    actuatorsBtn.classList.add("fa-chevron-down");
  }

  showActuators = !showActuators;
});
