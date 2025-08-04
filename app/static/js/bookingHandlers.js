import {
  bookingData,
  bookingState,
  resetBookingData,
  resetBookingState,
} from "./bookingData.js";
import { canProceed } from "./bookingSteps.js";
import { updateCalendarDisplay } from "./calendar.js";
import { updateProgress, updateNextButton } from "./uiHelpers.js";
import { updateTotalPrice } from "./pricing.js";

// Handle booking
export function handleBooking() {
  if (!canProceed(bookingState.currentStep)) return;

  bookingData.additionalInfo = document.getElementById("additionalInfo").value;
  const token =
    document.head.querySelector('meta[name="csrf-token"]')?.content || "";

  // Show loading modal
  document.getElementById("loadingModal").classList.remove("hidden");

  fetch("/booking", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
    body: JSON.stringify(bookingData),
  })
    .then(async (response) => {
      const data = await response.json();

      // Hide loading animation
      document.getElementById("loadingModal").classList.add("hidden");

      if (response.status === 200) {
        if (data.checkout_url) {
          // redirect to checkout
          window.location.href = data.checkout_url;
        } else {
          // No checkout URL — show confirmation modal
          showConfirmationModal();
        }
      } else {
        // Error response when status code not 200
        showErrorModal(data);
      }
    })
    .catch((error) => {
      document.getElementById("loadingModal").classList.add("hidden");
      showErrorModal(error);
    });
}

// Reset booking
export function resetBooking() {
  // Reset booking data and booking state
  resetBookingData();
  resetBookingState();

  // Reset UI
  document.getElementById("bookingComplete").classList.add("hidden");
  document.getElementById("bookingError").classList.add("hidden");
  document
    .querySelectorAll(".step")
    .forEach((step) => step.classList.remove("active"));
  document.getElementById("step1").classList.add("active");

  // Reset form fields
  document
    .querySelectorAll("input, textarea")
    .forEach((field) => (field.value = ""));

  // Reset buttons
  document
    .querySelectorAll(
      ".category-btn, .service-btn, .bedroom-btn, .bathroom-btn, .frequency-btn, .addon-btn, .time-btn, .payment-btn"
    )
    .forEach((btn) => {
      btn.classList.remove("border-primary", "bg-green-50");
      btn.classList.add("border-gray-200");

      if (btn.classList.contains("service-btn")) {
        btn.dataset.listenerAttached = false;
      }
    });

  // Hide service selection and summaries
  document.getElementById("serviceSelection").classList.add("hidden");
  document.getElementById("addOnSummary").classList.add("hidden");
  document.getElementById("scheduleSummary").classList.add("hidden");

  // Reset navigation
  document.getElementById("prevBtn").classList.add("hidden");
  document.getElementById("nextBtn").classList.remove("hidden");
  document.getElementById("bookBtn").classList.add("hidden");

  // Reset calendar
  updateCalendarDisplay();

  updateProgress();
  updateTotalPrice();
  updateNextButton();

  // temporal fix
  location.reload(true);
}

function showConfirmationModal() {
  document.getElementById("confirmedTotal").textContent =
    "$" + bookingState.totalPrice;

  // Show schedule in confirmation
  if (bookingData.selectedDate && bookingData.selectedTime) {
    const date = new Date(bookingData.selectedDate);
    const formattedDate = date.toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    document.getElementById(
      "confirmedSchedule"
    ).textContent = `Scheduled for ${formattedDate} at ${bookingData.selectedTime}`;
  }

  document.getElementById("bookingComplete").classList.remove("hidden");
}

function showErrorModal(data) {
  document.getElementById("errMsg").textContent =
    data?.message || "An error occurred while processing your booking.";

  document.getElementById("bookingError").classList.remove("hidden");
}
