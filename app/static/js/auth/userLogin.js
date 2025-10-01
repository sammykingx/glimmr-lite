document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if (!email || !password) {
        document.querySelector(".blnkErr").classList.toggle("hidden", false);
        return;
    }

    email = validator.normalizeEmail(email);
    password = validator.escape(password);

    const next = new URLSearchParams(window.location.search).get("next") || "";
    const token =
        document.head.querySelector('meta[name="csrf-token"]')?.content || "";
    
    try {
      const response = await fetch("/auth/checkpiont", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": token,
        },
        body: JSON.stringify({ email, password, next }),
      });

    const result = await response.json();
    if (!response.ok || result.status === "error") {
      alert(result.message || "Login failed. Please try again.");
      return;
    }

    window.location.href = result.redirect;

    } catch (error) {
      alert("An error occurred. Please try again later.");
    }
});