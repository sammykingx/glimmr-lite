import { initializeCalendar } from "./calendar.js"; //passed
import { updateTotalPrice } from "./pricing.js"; //passed
import { attachEventHandlers } from "./eventHandlers.js"; //passed

// DOMContentLoaded
document.addEventListener("DOMContentLoaded", function () {
  initializeCalendar();
  updateTotalPrice();
  attachEventHandlers();
});
