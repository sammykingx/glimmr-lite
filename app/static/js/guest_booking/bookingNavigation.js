import { canProceed } from "./bookingSteps.js";
import {
  bookingData,
  bookingState,
  decreaseCurrentStep,
  increaseCurrentStep,
  setCurrentStep,
} from "./bookingData.js"; //passed
import { updateProgress, updateNextButton } from "./uiHelpers.js"; //passed
import { updateBookingSummary } from "./bookingSummary.js"; //passed

// Next step
export function nextStep() {
  if (!canProceed(bookingState.currentStep)) return;

  if (bookingState.currentStep < 8) {
    // makes it a horizontal flow
    // disabling this part converts it to a vertical flow
    document
      .getElementById(`step${bookingState.currentStep}`)
      .classList.remove("active");

    if (
      bookingState.currentStep === 1 &&
      bookingData.category !== "residential_cleaning"
    ) {
      setCurrentStep(3);
    } else {
      increaseCurrentStep();
    }

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
    if (
      bookingState.currentStep === 3 &&
      bookingData.category !== "residential_cleaning"
    ) {
      setCurrentStep(1);
    } else {
      decreaseCurrentStep();
    }

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
