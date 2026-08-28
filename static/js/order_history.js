const dateBtns = document.querySelectorAll(".history-date-btn");
const groups = document.querySelectorAll(".history-group");

dateBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    const target = btn.dataset.date;

    dateBtns.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");

    groups.forEach((g) => {
      g.classList.toggle("hidden", g.dataset.date !== target);
    });
  });
});
