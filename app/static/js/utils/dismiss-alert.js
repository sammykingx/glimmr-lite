document.addEventListener("DOMContentLoaded", () => {
  const alerts = document.querySelectorAll("#alerts-container .alert");

  alerts.forEach((alert, index) => {
    // position stacking like toasts
    alert.style.top = `${index * 90}px`;

    // trigger entrance
    requestAnimationFrame(() => {
      alert.classList.remove("opacity-0", "-translate-y-3");
      alert.classList.add("opacity-100", "translate-y-0");
    });

    // auto dismiss after 5s
    setTimeout(() => dismissAlert(alert), 5000);

    // close button click
    const closeBtn = alert.querySelector(".close-btn");
    if (closeBtn) {
      closeBtn.addEventListener("click", () => dismissAlert(alert));
    }
  });

  function dismissAlert(alert) {
    alert.classList.remove("opacity-100", "translate-y-0");
    alert.classList.add("opacity-0", "-translate-y-3");

    alert.addEventListener(
      "transitionend",
      () => {
        alert.remove();
      },
      { once: true }
    );
  }
});
