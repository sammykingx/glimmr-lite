// eventHandlers.js
import {
  selectCategory,
  selectBedrooms,
  selectBathrooms,
  selectFrequency,
  toggleAddOn,
} from "./services.js";
import { selectPayment } from "./payments.js";
import { previousMonth, nextMonth, selectTime } from "./calendar.js";
import { nextStep, prevStep } from "./bookingNavigation.js";
import { handleBooking, resetBooking } from "./bookingHandlers.js";
import { setClientData } from "./clientData.js";

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
      selectBedrooms(Number(e.target.dataset.bedrooms), e);
    });
  });

  // Bathrooms
  document.querySelectorAll(".bathroom-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectBathrooms(Number(e.target.dataset.bathrooms), e);
    });
  });

  // Frequency
  document.querySelectorAll(".frequency-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectFrequency(e.target.dataset.frequency, e);
    });
  });

  // Add-ons
  document.querySelectorAll(".addon-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      toggleAddOn(btn.dataset.addons, e);
    });
  });

  // Previous Month Navigation
  document
    .getElementById("prev-month")
    .addEventListener("click", previousMonth);

  // Next Month Navigation
  document.getElementById("next-month").addEventListener("click", nextMonth);

  // Select Time
  document.querySelectorAll(".time-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectTime(btn.dataset.time, e);
    });
  });

  // Time selection
  // document.querySelectorAll(".time-btn").forEach((btn) => {
  //   btn.addEventListener("click", (e) => {
  //     selectTime(btn.textContent.trim(), e);
  //   });
  // });

  // Payment method
  document.querySelectorAll(".payment-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectPayment(btn.dataset.payWith, e);
    });
  });

  // Collect client Info
  document.querySelectorAll("[data-group][data-field]").forEach((input) => {
    input.addEventListener("input", (e) => {
      const group = e.target.dataset.group;
      const field = e.target.dataset.field;
      const value = e.target.value.trim();

      setClientData(group, field, value);
    });
  });

  // Handle Booking
  document.getElementById("bookBtn").addEventListener("click", handleBooking);

  // Reset
  document.getElementById("resetBtn")?.addEventListener("click", resetBooking);
  document
    .getElementById("retryBooking")
    ?.addEventListener("click", resetBooking);

  // Navigation
  document.getElementById("nextBtn").addEventListener("click", nextStep);
  document.getElementById("prevBtn").addEventListener("click", prevStep);
  document.getElementById("bookBtn").addEventListener("click", handleBooking);
}
