function showNotification(message) {
  const notification = document.getElementById("notification");
  const notificationMessage = document.getElementById("notificationMessage");
  notificationMessage.textContent = message;
  notification.style.display = "block";
  // Slide down
  setTimeout(() => {
    notification.classList.remove("top-[-100px]");
    notification.classList.add("top-6");
  }, 10);

  // Hide after 2.5 seconds, then slide up and reload
  setTimeout(() => {
    notification.classList.remove("top-6");
    notification.classList.add("top-[-100px]");
    setTimeout(() => {
      notification.style.display = "none";
      window.location.reload();
    }, 500);
  }, 2500);
}
