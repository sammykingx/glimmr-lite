import { bookingState } from "./bookingData.js"; //passed
import { canProceed } from "./bookingSteps.js"; //passed

// Update progress
export function updateProgress() {
  const currentStep = bookingState.currentStep;
  const progress = (currentStep / 8) * 100;
  document.getElementById(
    "stepIndicator"
  ).textContent = `Step ${currentStep} of 8`;
  document.getElementById("progressPercent").textContent = `${Math.round(
    progress
  )}% complete`;
  document.getElementById("progressBar").style.width = `${progress}%`;
}

// Update next button
export function updateNextButton() {
  const currentStep = bookingState.currentStep;
  const nextBtn = document.getElementById("nextBtn");
  const bookBtn = document.getElementById("bookBtn");

  if (currentStep < 8) {
    if (canProceed(currentStep)) {
      nextBtn.classList.remove(
        "bg-gray-300",
        "text-gray-500",
        "cursor-not-allowed"
      );
      nextBtn.classList.add(
        "bg-primary",
        "text-white",
        "hover:bg-green-800",
        "hover:shadow-lg"
      );
    } else {
      nextBtn.classList.add(
        "bg-gray-300",
        "text-gray-500",
        "cursor-not-allowed"
      );
      nextBtn.classList.remove(
        "bg-primary",
        "text-white",
        "hover:bg-green-800",
        "hover:shadow-lg"
      );
    }
  } else {
    if (canProceed(currentStep)) {
      bookBtn.classList.remove(
        "bg-gray-300",
        "text-gray-500",
        "cursor-not-allowed"
      );
      bookBtn.classList.add(
        "bg-primary",
        "text-white",
        "hover:bg-green-800",
        "hover:shadow-lg"
      );
    } else {
      bookBtn.classList.add(
        "bg-gray-300",
        "text-gray-500",
        "cursor-not-allowed"
      );
      bookBtn.classList.remove(
        "bg-primary",
        "text-white",
        "hover:bg-green-800",
        "hover:shadow-lg"
      );
    }
  }
}
