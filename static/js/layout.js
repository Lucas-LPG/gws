// ============================================================================================
// Essa página lida com as funções JavaScript no template, ou seja, header, menu e cursor
// ============================================================================================

// ============================================================================================
// Abrir e fechar o menu, lidar com as 3 barras do botão
// ============================================================================================

const firstBar = document.getElementById("firstBar");
const secondBar = document.getElementById("secondBar");
const thirdBar = document.getElementById("thirdBar");
const menuContainer = document.getElementById("menuContainer");
let isMenuOpened = false;

function handleMenuBars() {
  if (!isMenuOpened) {
    firstBar.classList.remove("first-bar");
    secondBar.classList.remove("second-bar");
    thirdBar.classList.remove("third-bar");
    firstBar.classList.add("active-first-bar");
    secondBar.classList.add("active-second-bar");
    thirdBar.classList.add("active-third-bar");
    menuContainer.style.height = "100vh";
  } else {
    firstBar.classList.remove("active-first-bar");
    secondBar.classList.remove("active-second-bar");
    thirdBar.classList.remove("active-third-bar");
    firstBar.classList.add("first-bar");
    secondBar.classList.add("second-bar");
    thirdBar.classList.add("third-bar");
    menuContainer.style.height = "0px";
  }

  isMenuOpened = !isMenuOpened;
}

// ============================================================================================
// Criar o StickyCursor => elemento que segue o mouse
// ============================================================================================

const cursorOuter = document.getElementById("cursorOuter");
const cursorInner = document.getElementById("cursorInner");
const cursorCoordinates = { x: 0, y: 0 };
let cursorSize = 35;

window.addEventListener("mousemove", (e) => {
  cursorCoordinates.x = e.clientX;
  cursorCoordinates.y = e.clientY;
  stickyCursor();
});

function stickyCursor() {
  let x = cursorCoordinates.x;
  let y = cursorCoordinates.y;

  cursorOuter.style.left = x - cursorSize / 2 + "px";
  cursorOuter.style.top = y - cursorSize / 2 + "px";
}

// ============================================================================================
// Ativar e disativar Cursor
// ============================================================================================

const menuBarsContainer = document.getElementById("menuBarsContainer");
const cursorVertical = document.querySelectorAll(".cursor-vertical");
const cursorHorizontal = document.querySelectorAll(".cursor-horizontal");
const cursorVerticalTop = document.getElementById("cursorVerticalTop");
const cursorVerticalBottom = document.getElementById("cursorVerticalBottom");
const cursorHorizontalLeft = document.getElementById("cursorHorizontalLeft");
const cursorHorizontalRight = document.getElementById("cursorHorizontalRight");

function toggleCursor(state) {
  const method = state === "activate" ? "add" : "remove";
  const inverseMethod = state === "activate" ? "remove" : "add";

  cursorInner.classList[inverseMethod]("cursor-inner");
  cursorInner.classList[method]("active-cursor-inner");

  cursorVertical.forEach((cursor) => {
    cursor.classList[method]("active-cursor-vertical");
  });
  cursorHorizontal.forEach((cursor) => {
    cursor.classList[method]("active-cursor-horizontal");
  });

  cursorVerticalTop.classList[inverseMethod]("cursor-vertical-top");
  cursorVerticalBottom.classList[inverseMethod]("cursor-vertical-bottom");
  cursorHorizontalLeft.classList[inverseMethod]("cursor-horizontal-left");
  cursorHorizontalRight.classList[inverseMethod]("cursor-horizontal-right");

  cursorVerticalTop.classList[method]("active-cursor-vertical-top");
  cursorVerticalBottom.classList[method]("active-cursor-vertical-bottom");
  cursorHorizontalLeft.classList[method]("active-cursor-horizontal-left");
  cursorHorizontalRight.classList[method]("active-cursor-horizontal-right");

  cursorOuter.style.transform = state === "activate" ? "rotate(180deg)" : "";
}

function activateCursor() {
  toggleCursor("activate");
}

function deactivateCursor() {
  toggleCursor("deactivate");
}

// ============================================================================================
// Adiciona função de ativar cursor dinamicamente para todos os links do Menu
// ============================================================================================

const menuTextContainer = document.getElementById("menuTextContainer");
const pagesLinks = menuTextContainer.getElementsByTagName("a");

for (let link of pagesLinks) {
  link.addEventListener("mouseover", activateCursor);
  link.addEventListener("mouseleave", deactivateCursor);
}
