function togglePassword() {
  const passwordInput = document.getElementById("password");
  const eyeIcon = document.getElementById("eyeIcon");

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    eyeIcon.setAttribute("stroke", "green");
  } else {
    passwordInput.type = "password";
    eyeIcon.setAttribute("stroke", "currentColor");
  }
}

document
  .getElementById("togglePassword")
  .addEventListener("click", function () {
    togglePassword();
  });