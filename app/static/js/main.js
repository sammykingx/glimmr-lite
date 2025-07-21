import { initializeCalendar } from "./calendar.js"; //passed
import { updateTotalPrice } from "./pricing.js"; //passed
import { attachEventHandlers } from "./eventHandlers.js"; //passed
import { updateProgress } from "./uiHelpers.js";

// DOMContentLoaded
document.addEventListener("DOMContentLoaded", function () {
  updateProgress();
  initializeCalendar();
  updateTotalPrice();
  attachEventHandlers();
});
