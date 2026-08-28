(function () {
  const input = document.querySelector(".search-input");
  const form = document.querySelector(".search-bar");
  if (!input) return;

  const dropdown = document.createElement("div");
  dropdown.className = "search-suggestions";
  form.appendChild(dropdown);

  let debounceTimer;

  input.addEventListener("input", () => {
    clearTimeout(debounceTimer);
    const q = input.value.trim();

    if (q.length < 2) {
      dropdown.innerHTML = "";
      dropdown.style.display = "none";
      return;
    }

    debounceTimer = setTimeout(() => {
      fetch(`/catalog/search/suggestions/?q=${encodeURIComponent(q)}`)
        .then((r) => r.json())
        .then((suggestions) => {
          if (!suggestions.length) {
            dropdown.style.display = "none";
            return;
          }

          dropdown.innerHTML = suggestions
            .map(
              (s) =>
                `<a href="/catalog/product/${s.id}/" class="suggestion-item">
                  ${s.name}
                </a>`
            )
            .join("");

          dropdown.style.display = "block";
        });
    }, 250);
  });

  document.addEventListener("click", (e) => {
    if (!form.contains(e.target)) dropdown.style.display = "none";
  });
})();
