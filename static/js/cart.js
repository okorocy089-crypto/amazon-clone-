function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

function post(url) {
  return fetch(url, {
    method: "POST",
    headers: { "X-CSRFToken": getCookie("csrftoken") },
  }).then((r) => r.json());
}

function updateBadge(count) {
  document.querySelectorAll(".cart-badge").forEach(b => b.textContent = count);
}

function recalcTotal() {
  let total = 0;
  // Sum across whichever grid is visible — both desktop .cart-item
  // and mobile .cart-card-mobile share data-price and .qty-value
  document.querySelectorAll("[data-item-id]").forEach((row) => {
    const price = parseFloat(row.dataset.price || 0);
    const qtyEl = row.querySelector(".qty-value");
    if (qtyEl) total += price * parseInt(qtyEl.textContent, 10);
  });
  const fmt = "$" + total.toFixed(2);
  ["cart-total", "cart-total-mobile"].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.textContent = fmt;
  });
}

function showEmptyState() {
  // Replace the whole cart page content with a properly styled empty state
  const cartPage = document.querySelector(".cart-page");
  if (cartPage) {
    cartPage.innerHTML = `
      <div style="
        min-height: 60vh;
        display: flex;
        align-items: center;
        justify-content: center;
        background: var(--color-empty-bg);
        border-radius: var(--radius-md);
      ">
        <p style="color: var(--color-text-empty); font-size: 1.2rem; text-align: center;">
          Cart is empty
        </p>
      </div>
    `;
  }
  // Hide the mobile sticky bar
  const bar = document.querySelector(".cart-bar-mobile");
  if (bar) bar.style.display = "none";
  // Remove the extra bottom padding
  document.body.style.paddingBottom = "0";
  updateBadge(0);
}

function removeRow(row) {
  // Each item has a matching row in both desktop and mobile grids
  const itemId = row.dataset.itemId;
  document.querySelectorAll(`[data-item-id="${itemId}"]`).forEach(r => {
    r.style.transition = "opacity 0.3s";
    r.style.opacity = "0";
    setTimeout(() => {
      r.remove();
      recalcTotal();
      if (!document.querySelector("[data-item-id]")) showEmptyState();
    }, 300);
  });
}

// Increase
document.querySelectorAll(".increase-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const row = btn.closest("[data-item-id]");
    post(`/cart/increase/${row.dataset.itemId}/`).then((data) => {
      if (data.error) {
        alert(typeof data.error === "string" ? data.error : data.error.join(", "));
        return;
      }
      // Update qty in ALL matching rows (desktop + mobile)
      document.querySelectorAll(`[data-item-id="${row.dataset.itemId}"] .qty-value`)
        .forEach(el => el.textContent = parseInt(el.textContent, 10) + 1);
      recalcTotal();
    });
  });
});

// Decrease
document.querySelectorAll(".decrease-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const row = btn.closest("[data-item-id]");
    const current = parseInt(row.querySelector(".qty-value").textContent, 10);
    post(`/cart/decrease/${row.dataset.itemId}/`).then((data) => {
      if (data.error) { alert(data.error); return; }
      if (current <= 1) {
        removeRow(row);
      } else {
        document.querySelectorAll(`[data-item-id="${row.dataset.itemId}"] .qty-value`)
          .forEach(el => el.textContent = current - 1);
        recalcTotal();
      }
    });
  });
});

// Remove single item
document.querySelectorAll(".remove-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const row = btn.closest("[data-item-id]");
    post(`/cart/remove/${row.dataset.itemId}/`).then(() => removeRow(row));
  });
});

// Remove all — desktop button
const removeAllDesktop = document.getElementById("remove-all-btn-desktop");
if (removeAllDesktop) {
  removeAllDesktop.addEventListener("click", () => {
    post("/cart/remove-all/").then(() => {
      showEmptyState();
      updateBadge(0);
    });
  });
}

// Remove all — mobile trash icon
const removeAllMobile = document.getElementById("remove-all-btn-mobile");
if (removeAllMobile) {
  removeAllMobile.addEventListener("click", () => {
    post("/cart/remove-all/").then(() => {
      showEmptyState();
      updateBadge(0);
    });
  });
}