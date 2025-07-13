import { updateNextButton } from "./uiHelpers.js"; //passed

export function setupFormValidation() {
  const fields = [
    "firstName",
    "lastName",
    "email",
    "phone",
    "street",
    "city",
    "state",
    "zipCode",
  ];
  fields.forEach((id) => {
    document.getElementById(id).addEventListener("input", updateNextButton);
  });
}
