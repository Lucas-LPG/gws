const activePeopleGraph = document.querySelector(
  ".capacity--body--right--active-graph",
);
const peoplePercentage = document.querySelector(
  ".capacity--body--right--text-container--span",
);

let currentPeople = parseInt(document.querySelector(".people").innerHTML);

activePeopleGraph.style.height = (currentPeople * 250) / 100 + "px";
peoplePercentage.style.marginBottom =
  (currentPeople * 250) / 100 - 10 > 0
    ? (currentPeople * 250) / 100 - 10 + "px"
    : 0 + "px";

function enviarInformacao(valor) {
  var data = {
    valor: valor,
  };

  fetch("/publish_message", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (response.ok) {
        console.log("Informação enviada com sucesso!");
        return response.json();
      } else {
        console.error("Erro ao enviar informação.");
        throw new Error("Erro ao enviar informação");
      }
    })
    .then((data) => {})
    .catch((error) => {
      console.error("Erro ao enviar informação:", error);
    });
  window.location.reload();
}

setTimeout(() => {
  window.location.reload();
}, 10000);
