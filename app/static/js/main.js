import { initializeCalendar } from "./calendar.js";
import { updateTotalPrice } from "./pricing.js";
import { updateNextButton } from "./uiHelpers.js";
import { setupFormValidation } from "./formValidation.js";
import { attachEventHandlers } from "./eventHandlers.js";

// DOMContentLoaded
document.addEventListener("DOMContentLoaded", function () {
    initializeCalendar();
    updateTotalPrice();
    updateNextButton();
    setupFormValidation();
    attachEventHandlers();
});
