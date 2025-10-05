document.addEventListener("DOMContentLoaded", () => {
  const alerts = document.querySelectorAll("#alerts-container .alert");

  alerts.forEach((alert, index) => {
    // Position stacking (optional if multiple)
    alert.style.marginTop = `${index * 10}px`;

    // Animate entrance
    requestAnimationFrame(() => {
      alert.classList.remove("opacity-0", "-translate-y-3");
      alert.classList.add("opacity-100", "translate-y-0");
    });

    // Auto-dismiss after 5 seconds
    setTimeout(() => dismissAlert(alert), 5000);
  });

  function dismissAlert(alert) {
    alert.classList.remove("opacity-100", "translate-y-0");
    alert.classList.add("opacity-0", "-translate-y-3");

    alert.addEventListener("transitionend", () => alert.remove(), {
      once: true,
    });
  }
});
