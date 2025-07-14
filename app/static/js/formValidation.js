import { updateNextButton } from "./uiHelpers.js"; //passed
import { bookingData } from "./bookingData.js";

export function setupFormValidation() {
  const requiredFields = [
    "firstName",
    "lastName",
    "email",
    "phone",
    "street",
    "city",
    "state",
    "zipCode",
  ];


}

// requiredFields.forEach((id) => {
//   document.getElementById(id).addEventListener("input", updateNextButton);
// });