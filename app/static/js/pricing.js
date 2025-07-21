import { bookingData, bookingState, setTotalPrice } from "./bookingData.js"; // passed
import { residentialPricing, frequencyMultipliers } from "./constants.js"; // passed

// service base prices
export function getBasePrice() {
  let basePrice = 0;
  if (bookingData.category === "residential_cleaning") {
    basePrice =
      residentialPricing[bookingData.service]?.[bookingData.bedrooms]?.[
        bookingData.bathrooms
      ] ?? 0;
  } else if (bookingData.category === "commercial_cleaning") {
    // basePrice = size * multiplier;
    basePrice = 200 * 0.2;
  } else {
    basePrice = bookingState.serviceCost;
  }

  return basePrice;
}

// updates app's total price
export function updateTotalPrice() {
  const basePrice = getBasePrice();
  const cleaningFrequency = frequencyMultipliers[bookingData.frequency]
    ? frequencyMultipliers[bookingData.frequency]
    : frequencyMultipliers["oneOff"];
  const calculatedPrice = basePrice * cleaningFrequency.multiplier;
  const discountedPrice = calculatedPrice * cleaningFrequency.discount;
  const addOnPrice = bookingData.addOns.reduce((sum, addon) => {
    return sum + addon.price;
  }, 0);
  const total = calculatedPrice - discountedPrice + addOnPrice;
  const tax = total * 0.15;

  // Set state values
  bookingState.subtotal = calculatedPrice;
  bookingState.discountPrice = discountedPrice;
  bookingState.addonPrice = addOnPrice;
  bookingState.tax = total * 0.15;
  setTotalPrice(total + tax);

  // DOM update logic here
  document.getElementById("totalPrice").textContent = total.toLocaleString(
    "en-CA",
    { style: "currency", currency: "CAD" }
  );
  document.getElementById("finalPrice").textContent =
    bookingState.totalPrice.toLocaleString("en-CA", {
      style: "currency",
      currency: "CAD",
    });

  updateFrequnecyUI(basePrice, calculatedPrice, discountedPrice);

  // Update base price display
  //document.getElementById("basePrice").textContent = "$" + basePrice;
}

function updateFrequnecyUI(basePrice) {
  const weeklyPrice = basePrice * frequencyMultipliers["weekly"]["multiplier"];
  const biWeeklyPrice =
    basePrice * frequencyMultipliers["bi-weekly"]["multiplier"];
  const monthlyPrice =
    basePrice * frequencyMultipliers["monthly"]["multiplier"];

  const weeklyDiscount =
    weeklyPrice * frequencyMultipliers["weekly"]["discount"];
  const biWeeklyDiscount =
    biWeeklyPrice * frequencyMultipliers["bi-weekly"]["discount"];
  const monthlyDiscount =
    monthlyPrice * frequencyMultipliers["monthly"]["discount"];

  // update saved amount in freequcny step
  document.getElementById("weeklyDiscount").textContent =
    weeklyDiscount.toLocaleString("en-CA", {
      style: "currency",
      currency: "CAD",
    });

  document.getElementById("biWeeklyDiscount").textContent =
    biWeeklyDiscount.toLocaleString("en-CA", {
      style: "currency",
      currency: "CAD",
    });

  document.getElementById("monthlyDiscount").textContent =
    monthlyDiscount.toLocaleString("en-CA", {
      style: "currency",
      currency: "CAD",
    });

  // Update frequency prices
  document.getElementById("weeklyPrice").textContent = (
    weeklyPrice - weeklyDiscount
  ).toLocaleString("en-CA", { style: "currency", currency: "CAD" });

  document.getElementById("biWeeklyPrice").textContent = (
    biWeeklyPrice - biWeeklyDiscount
  ).toLocaleString("en-CA", { style: "currency", currency: "CAD" });

  document.getElementById("monthlyPrice").textContent = (
    monthlyPrice - monthlyDiscount
  ).toLocaleString("en-CA", { style: "currency", currency: "CAD" });
}
