import { initializeCalendar } from "./calendar.js"; //passed
import { updateTotalPrice } from "./pricing.js"; //passed
import { updateNextButton } from "./uiHelpers.js"; //passed
import { setupFormValidation } from "./formValidation.js"; //passed
import { attachEventHandlers } from "./eventHandlers.js"; //passed

// DOMContentLoaded
document.addEventListener("DOMContentLoaded", function () {
  initializeCalendar();
  updateTotalPrice();
  updateNextButton();
  setupFormValidation();
  attachEventHandlers();
});
