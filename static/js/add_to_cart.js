function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

document.querySelectorAll(".add-to-cart-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    if (btn.classList.contains("added")) return; // one-directional, no revert

    const productId = btn.dataset.productId;

    fetch(`/cart/add/${productId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert(data.error);
          return;
        }

        btn.classList.add("added");
        btn.textContent = "Added";

        const badge = document.querySelector(".cart-badge");
        if (badge) badge.textContent = data.cart_count;
      })
      .catch(() => {
        alert("Something went wrong adding this to your cart.");
      });
  });
});