import { bookingData } from "./bookingData.js";
import { updateNextButton } from "./uiHelpers.js";

export function setClientData(group, field, value) {

  const allowedGroups = ["personalInfo", "address"];

  if (!allowedGroups.includes(group)) return;

  bookingData[group][field] = value;
  updateNextButton();
}
