// eventHandlers.js
import {
  selectBedrooms,
  selectBathrooms,
  selectFrequency,
  toggleAddOn,
  selectPayment,
  selectTime,
  nextStep,
  prevStep,
  handleBooking,
  resetBooking,
} from "./bookingActions.js";

export function attachEventHandlers() {
  // Bedrooms
  document.querySelectorAll(".bedroom-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectBedrooms(Number(e.target.dataset.value), e);
    });
  });

  // Bathrooms
  document.querySelectorAll(".bathroom-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectBathrooms(Number(e.target.dataset.value), e);
    });
  });

  // Frequency
  document.querySelectorAll(".frequency-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectFrequency(e.target.dataset.value, e);
    });
  });

  // Add-ons
  document.querySelectorAll(".addon-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      toggleAddOn(btn.dataset.addon, e);
    });
  });

  // Payment method
  document.querySelectorAll(".payment-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectPayment(btn.dataset.method, e);
    });
  });

  // Time selection
  document.querySelectorAll(".time-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectTime(btn.textContent.trim(), e);
    });
  });

  // Navigation
  document.getElementById("nextBtn").addEventListener("click", nextStep);
  document.getElementById("prevBtn").addEventListener("click", prevStep);
  document.getElementById("bookBtn").addEventListener("click", handleBooking);

  // Reset
  document.getElementById("resetBtn")?.addEventListener("click", resetBooking);
}
