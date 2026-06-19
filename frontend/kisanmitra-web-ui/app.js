(() => {
  "use strict";

  const form = document.getElementById("loginForm");
  const passwordInput = document.getElementById("password");
  const togglePassword = document.getElementById("togglePassword");
  const statusMessage = document.getElementById("statusMessage");
  const forgotPassword = document.getElementById("forgotPassword");
  const signUp = document.getElementById("signUp");

  togglePassword?.addEventListener("click", () => {
    const isPassword = passwordInput.type === "password";
    passwordInput.type = isPassword ? "text" : "password";
    togglePassword.setAttribute("aria-label", isPassword ? "Hide password" : "Show password");
  });

  form?.addEventListener("submit", (event) => {
    event.preventDefault();

    const userId = form.userId.value.trim();
    const password = form.password.value;

    if (!userId || !password) {
      statusMessage.textContent = "Please enter User ID and Password.";
      return;
    }

    /*
      Production backend wiring will be added after api.kisanmitraai.com is live.
      Keep secrets only in Render Environment Variables. No frontend secrets.
    */
    statusMessage.textContent = "Login screen ready. Backend connection pending.";
  });

  forgotPassword?.addEventListener("click", (event) => {
    event.preventDefault();
    statusMessage.textContent = "Forgot password flow will connect after backend setup.";
  });

  signUp?.addEventListener("click", (event) => {
    event.preventDefault();
    statusMessage.textContent = "Sign up flow will connect after backend setup.";
  });
})();


