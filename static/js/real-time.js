const activePeopleGraph = document.querySelector(
  ".capacity--body--right--active-graph",
);
const peoplePercentage = document.querySelector(
  ".capacity--body--right--text-container--span",
);

let currentPeople = parseInt(document.querySelector(".people").innerHTML);
console.log(currentPeople);

activePeopleGraph.style.height = (currentPeople * 250) / 100 + "px";
peoplePercentage.style.marginBottom =
  (currentPeople * 250) / 100 - 10 > 0
    ? (currentPeople * 250) / 100 - 10 + "px"
    : 0 + "px";
