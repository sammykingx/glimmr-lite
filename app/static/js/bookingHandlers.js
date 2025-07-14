import { bookingData, bookingState, resetBookingData } from "./bookingData.js";
import { canProceed } from "./bookingSteps.js";
import { updateCalendarDisplay } from "./calendar.js";
import { updateProgress, updateNextButton } from "./uiHelpers.js";
import { updateTotalPrice } from "./pricing.js";

// Handle booking
export function handleBooking() {
  if (!canProceed(bookingState.currentStep)) return;

  // Collect personal information
  bookingData.personalInfo = {
    firstName: document.getElementById("firstName").value,
    lastName: document.getElementById("lastName").value,
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value,
  };

  bookingData.address = {
    street: document.getElementById("street").value,
    city: document.getElementById("city").value,
    state: document.getElementById("state").value,
    zipCode: document.getElementById("zipCode").value,
  };

  bookingData.additionalInfo = document.getElementById("additionalInfo").value;
  const token =
    document.head.querySelector('meta[name="csrf-token"]')?.content || "";

  // Show loading modal
  document.getElementById("loadingModal").classList.remove("hidden");

  // Simulate processing time
  setTimeout(() => {
    document.getElementById("loadingModal").classList.add("hidden");

    // Show booking complete modal
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

    console.log("Booking Data:", bookingData);
  }, 2000);
}

// Reset booking
export function resetBooking() {
  // Reset data
  resetBookingData();

  bookingState.currentStep = 1;
  bookingState.totalPrice = 90;

  // Reset UI
  document.getElementById("bookingComplete").classList.add("hidden");
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
  currentCalendarDate = new Date();
  updateCalendarDisplay();

  updateProgress();
  updateTotalPrice();
  updateNextButton();
}
