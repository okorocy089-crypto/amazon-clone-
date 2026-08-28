(function () {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.getElementById("sidebar-overlay");
  const openBtn = document.getElementById("menu-toggle-btn");
  const closeBtn = document.getElementById("sidebar-close");
  const categoriesToggle = document.getElementById("categories-toggle");
  const categoriesPanel = document.getElementById("sidebar-categories");
  const categoriesArrow = document.getElementById("categories-arrow");

  function openSidebar() {
    sidebar.classList.add("open");
    overlay.classList.add("active");
    document.body.style.overflow = "hidden"; // prevent background scroll
  }

  function closeSidebar() {
    sidebar.classList.remove("open");
    overlay.classList.remove("active");
    document.body.style.overflow = "";
  }

  if (openBtn) openBtn.addEventListener("click", openSidebar);
  if (closeBtn) closeBtn.addEventListener("click", closeSidebar);
  if (overlay) overlay.addEventListener("click", closeSidebar);

  if (categoriesToggle) {
    categoriesToggle.addEventListener("click", () => {
      const isOpen = categoriesPanel.classList.toggle("open");
      categoriesArrow.classList.toggle("open", isOpen);
    });
  }
})();
