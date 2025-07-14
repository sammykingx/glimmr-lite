import { canProceed } from "./bookingSteps.js";
import {
  bookingState,
  decreaseCurrentStep,
  increaseCurrentStep,
} from "./bookingData.js"; //passed
import { updateProgress, updateNextButton } from "./uiHelpers.js"; //passed
import { updateBookingSummary } from "./bookingSummary.js"; //passed

// Next step
export function nextStep() {
  if (!canProceed(bookingState.currentStep)) return;

  if (bookingState.currentStep < 8) {
    document
      .getElementById(`step${bookingState.currentStep}`)
      .classList.remove("active");
    increaseCurrentStep();
    document
      .getElementById(`step${bookingState.currentStep}`)
      .classList.add("active");

    updateProgress();

    // Show/hide navigation buttons
    if (bookingState.currentStep > 1) {
      document.getElementById("prevBtn").classList.remove("hidden");
    }

    if (bookingState.currentStep === 8) {
      document.getElementById("nextBtn").classList.add("hidden");
      document.getElementById("bookBtn").classList.remove("hidden");
      updateBookingSummary();
    }

    updateNextButton();
  }
}

// Previous step
export function prevStep() {
  if (bookingState.currentStep > 1) {
    document
      .getElementById(`step${bookingState.currentStep}`)
      .classList.remove("active");
    decreaseCurrentStep();
    document
      .getElementById(`step${bookingState.currentStep}`)
      .classList.add("active");

    updateProgress();

    // Show/hide navigation buttons
    if (bookingState.currentStep === 1) {
      document.getElementById("prevBtn").classList.add("hidden");
    }

    if (bookingState.currentStep < 8) {
      document.getElementById("nextBtn").classList.remove("hidden");
      document.getElementById("bookBtn").classList.add("hidden");
    }

    updateNextButton();
  }
}
