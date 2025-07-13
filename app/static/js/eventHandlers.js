// eventHandlers.js
import {
  selectCategory,
  selectBedrooms,
  selectBathrooms,
  selectFrequency,
  toggleAddOn,
} from "./services.js"; //passed
import { selectPayment } from "./payments.js"; //passed
import { selectTime } from "./calendar.js"; //passed
import { nextStep, prevStep } from "./bookingNavigation.js"; //passed
import { handleBooking, resetBooking } from "./bookingHandlers.js"; //passed

export function attachEventHandlers() {
  
  // Category & Service selection
  document.querySelectorAll(".category-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const category = btn.dataset.category;
      selectCategory(category, e);
    });
  });

  // Bedrooms
  document.querySelectorAll(".bedroom-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      console.log(`Selected Bedrooms: ${e.target.dataset.value}`);
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
