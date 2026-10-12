(function () {
  const input = document.querySelector(".search-input");
  const form = document.querySelector(".search-bar");
  if (!input || !form) return;

  const dropdown = document.createElement("div");
  dropdown.className = "search-suggestions";
  dropdown.id = "search-suggestions";
  dropdown.setAttribute("role", "listbox");
  form.appendChild(dropdown);
  input.setAttribute("aria-controls", dropdown.id);

  let debounceTimer;
  let activeRequest;

  function hideSuggestions() {
    clearTimeout(debounceTimer);
    if (activeRequest) {
      activeRequest.abort();
      activeRequest = null;
    }
    dropdown.replaceChildren();
    dropdown.style.display = "none";
    input.setAttribute("aria-expanded", "false");
  }

  input.addEventListener("input", () => {
    hideSuggestions();
    const q = input.value.trim();

    if (!q) return;

    debounceTimer = setTimeout(() => {
      activeRequest = new AbortController();
      const url = new URL(form.dataset.suggestionsUrl, window.location.origin);
      url.searchParams.set("q", q);

      fetch(url, { signal: activeRequest.signal })
        .then((response) => {
          if (!response.ok) {
            throw new Error(`Suggestion request failed (${response.status})`);
          }
          return response.json();
        })
        .then((suggestions) => {
          if (input.value.trim() !== q) return;
          if (!suggestions.length) {
            hideSuggestions();
            return;
          }

          dropdown.replaceChildren();
          suggestions.forEach((suggestion) => {
            const link = document.createElement("a");
            link.href = `/catalog/product/${encodeURIComponent(suggestion.id)}/`;
            link.className = "suggestion-item";
            link.setAttribute("role", "option");
            link.textContent = suggestion.name;
            dropdown.appendChild(link);
          });
          dropdown.style.display = "block";
          input.setAttribute("aria-expanded", "true");
        })
        .catch((error) => {
          if (error.name === "AbortError") return;
          hideSuggestions();
          console.error("Unable to load product suggestions.", error);
        });
    }, 250);
  });

  document.addEventListener("click", (e) => {
    if (!form.contains(e.target)) hideSuggestions();
  });

  input.addEventListener("keydown", (e) => {
    if (e.key === "Escape") hideSuggestions();
  });
})();
