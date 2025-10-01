// import validator from "validator";

document
  .getElementById("registerForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    let email = document.getElementById("email").value;
    const raw_password = document.getElementById("raw_password").value;
    let password = document.getElementById("password").value;

    if (!email || !raw_password || !password) {
      document.querySelector(".blnkErr").classList.toggle("hidden", false);
      return;
    }
    
    // if (!validator.isEmail(email)) {
    //   document.getElementById("emailErr").classList.toggle("hidden", false);
    //   return;
    // }
      
    if (raw_password !== password) {
      document.getElementById("pwdErr").classList.toggle("hidden", false);
      return;
    }

    // email = validator.normalizeEmail(email);
    // password = validator.escape(password); 
    const token =
          document.head.querySelector('meta[name="csrf-token"]')?.content || "";
      
    console.log(`Sanitized data: Email - ${email}, Password - ${password}`);

    try {
      const response = await fetch("/auth/create-account", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": token,
        },
        body: JSON.stringify({ email, raw_password, password }),
      });

      const result = await response.json();

      if (response.ok) {
        alert(
          result.message ||
            "Registration successful! Please check your email to verify your account."
        );
        window.location.href = "{{ url_for('auth.user_login') }}";
      } else {
        alert(result.error || "Registration failed. Please try again.");
      }
    } catch (error) {
      console.error("Error during registration:", error);
      alert("An error occurred. Please try again later.");
    }
  });
