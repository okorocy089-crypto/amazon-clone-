// Runs on any page that has password or card-number fields.
// Add <script src="{% static 'js/eye_toggle.js' %}"></script> to base.html's extra_js
// so it applies everywhere automatically.

(function () {
  const EYE_OPEN = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none"
    stroke="currentColor" stroke-width="2">
    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
    <circle cx="12" cy="12" r="3"/>
  </svg>`;

  const EYE_CLOSED = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none"
    stroke="currentColor" stroke-width="2">
    <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94"/>
    <path d="M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19"/>
    <line x1="1" y1="1" x2="23" y2="23"/>
  </svg>`;

  document.querySelectorAll('input[type="password"]').forEach((input) => {
    const wrap = document.createElement("div");
    wrap.className = "password-wrap";
    input.parentNode.insertBefore(wrap, input);
    wrap.appendChild(input);

    // Copy the margin the input previously had onto the wrapper
    wrap.style.marginBottom = "1rem";
    input.style.marginBottom = "0";

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "eye-btn";
    btn.innerHTML = EYE_CLOSED;
    btn.setAttribute("aria-label", "Toggle visibility");
    wrap.appendChild(btn);

    btn.addEventListener("click", () => {
      const visible = input.type === "text";
      input.type = visible ? "password" : "text";
      btn.innerHTML = visible ? EYE_CLOSED : EYE_OPEN;
    });
  });
})();
