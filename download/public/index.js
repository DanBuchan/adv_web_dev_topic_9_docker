const button = document.getElementsByTagName("button");
const loading_container = document.getElementsByClassName(
  "loading-container"
)[0];

button[0].addEventListener("click", e => {
  e.target.classList.add("hide");
  loading_container.classList.remove("hide");
});
