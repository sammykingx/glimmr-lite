import { bookingData } from "./bookingData.js";

export function selectPayment(method) {
  bookingData.paymentMethod = method;

  // Update UI
  document.querySelectorAll(".payment-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target.classList.add("border-primary", "bg-green-50");
  event.target.classList.remove("border-gray-200");

  updateNextButton();
}
