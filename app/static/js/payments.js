import { bookingData } from "./bookingData.js";
import { updateNextButton } from "./uiHelpers.js";

export function selectPayment(method, event) {
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
