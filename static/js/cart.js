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
  const badge = document.querySelector(".cart-badge");
  if (badge) badge.textContent = count;
}

function recalcTotal() {
  // Re-sum all visible per-item prices × quantities.
  // Each .cart-item has data-price (unit price) and .qty-value (current qty).
  let total = 0;
  document.querySelectorAll(".cart-item").forEach((row) => {
    const price = parseFloat(row.dataset.price || 0);
    const qty = parseInt(row.querySelector(".qty-value").textContent, 10);
    total += price * qty;
  });
  const totalEl = document.getElementById("cart-total");
  if (totalEl) totalEl.textContent = "$" + total.toFixed(2);
}

document.querySelectorAll(".increase-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const row = btn.closest(".cart-item");
    const itemId = row.dataset.itemId;
    const qtyEl = row.querySelector(".qty-value");

    post(`/cart/increase/${itemId}/`).then((data) => {
      if (data.error) {
        alert(typeof data.error === "string" ? data.error : data.error.join(", "));
        return;
      }
      qtyEl.textContent = parseInt(qtyEl.textContent, 10) + 1;
      recalcTotal();
    });
  });
});

document.querySelectorAll(".decrease-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const row = btn.closest(".cart-item");
    const itemId = row.dataset.itemId;
    const qtyEl = row.querySelector(".qty-value");
    const current = parseInt(qtyEl.textContent, 10);

    post(`/cart/decrease/${itemId}/`).then((data) => {
      if (data.error) {
        alert(data.error);
        return;
      }
      if (current <= 1) {
        // Item was removed entirely — fade the row out then delete it
        row.style.transition = "opacity 0.3s";
        row.style.opacity = "0";
        setTimeout(() => {
          row.remove();
          recalcTotal();
          // Show empty state if no items remain
          if (!document.querySelector(".cart-item")) {
            document.getElementById("cart-items").innerHTML =
              '<p style="padding:2rem;text-align:center;color:var(--color-text-empty)">You have not added anything yet</p>';
            const summary = document.querySelector(".cart-summary");
            if (summary) summary.style.display = "none";
          }
        }, 300);
      } else {
        qtyEl.textContent = current - 1;
        recalcTotal();
      }
    });
  });
});

document.querySelectorAll(".remove-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const row = btn.closest(".cart-item");
    const itemId = row.dataset.itemId;

    post(`/cart/remove/${itemId}/`).then(() => {
      row.style.transition = "opacity 0.3s";
      row.style.opacity = "0";
      setTimeout(() => {
        row.remove();
        recalcTotal();
        if (!document.querySelector(".cart-item")) {
          document.getElementById("cart-items").innerHTML =
            '<p style="padding:2rem;text-align:center;color:var(--color-text-empty)">You have not added anything yet</p>';
          const summary = document.querySelector(".cart-summary");
          if (summary) summary.style.display = "none";
        }
      }, 300);
    });
  });
});

const removeAllBtn = document.getElementById("remove-all-btn");
if (removeAllBtn) {
  removeAllBtn.addEventListener("click", () => {
    post("/cart/remove-all/").then(() => {
      document.getElementById("cart-items").innerHTML =
        '<p style="padding:2rem;text-align:center;color:var(--color-text-empty)">You have not added anything yet</p>';
      const summary = document.querySelector(".cart-summary");
      if (summary) summary.style.display = "none";
      updateBadge(0);
    });
  });
}
