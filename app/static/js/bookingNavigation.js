import { canProceed } from "./bookingSteps.js";
import { currentStep, increaseCurrentStep } from "./bookingData.js"; //passed
import { updateProgress, updateNextButton } from "./uiHelpers.js"; //passed
import { updateBookingSummary } from "./bookingSummary.js"; //passed

// Next step
export function nextStep() {
  if (!canProceed(currentStep)) return;

  if (currentStep < 8) {
    document.getElementById(`step${currentStep}`).classList.remove("active");
    increaseCurrentStep++;
    document.getElementById(`step${currentStep}`).classList.add("active");

    updateProgress();

    // Show/hide navigation buttons
    if (currentStep > 1) {
      document.getElementById("prevBtn").classList.remove("hidden");
    }

    if (currentStep === 8) {
      document.getElementById("nextBtn").classList.add("hidden");
      document.getElementById("bookBtn").classList.remove("hidden");
      updateBookingSummary();
    }

    updateNextButton();
  }
}

// Previous step
export function prevStep() {
  if (currentStep > 1) {
    document.getElementById(`step${currentStep}`).classList.remove("active");
    currentStep--;
    document.getElementById(`step${currentStep}`).classList.add("active");

    updateProgress();

    // Show/hide navigation buttons
    if (currentStep === 1) {
      document.getElementById("prevBtn").classList.add("hidden");
    }

    if (currentStep < 8) {
      document.getElementById("nextBtn").classList.remove("hidden");
      document.getElementById("bookBtn").classList.add("hidden");
    }

    updateNextButton();
  }
}
