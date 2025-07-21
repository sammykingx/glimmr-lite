// eventHandlers.js
import {
  selectCategory,
  selectService,
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
  // Category Selection
  document.querySelectorAll(".category-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const category = btn.dataset.category;
      selectCategory(category, e);
    });
  });

  // Service selection after htmx response
  document.body.addEventListener("htmx:afterSettle", function (evt) {
    const target = evt.target;

    // Restrict to only the service or category areas
    if (
      target.closest("#serviceSelection") ||
      target.closest("#serviceOptions")
    ) {
      document.querySelectorAll(".service-btn").forEach((btn) => {
        if (!btn.dataset.listenerAttached) {
          btn.dataset.listenerAttached = "true";
          btn.addEventListener("click", (event) => {
            const selectedService = btn.dataset.service;
            const amount = btn.dataset.amount;
            const label = btn.dataset.label;
            selectService(selectedService, amount, label, event);
          });
        }
      });
    }
  });

  // Event handlers for bedrooms and bathrooms are dynamically added
  // to the DOM in service.js

  // Frequency
  document.querySelectorAll(".frequency-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      selectFrequency(e.target.dataset.frequency, e);
    });
  });

  // Add-ons
  document.querySelectorAll(".addon-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      toggleAddOn(btn.dataset.addons, Number(btn.dataset.addonsAmount), e);
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
