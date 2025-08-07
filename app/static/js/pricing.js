import { bookingData, bookingState, setTotalPrice } from "./bookingData.js"; // passed
import { residentialPricing, frequencyMultipliers } from "./constants.js"; // passed

function getFirstKey(bedrooms, bathObj) {
  // returns the first key when the for bathrooms mapp
  // when the bedrooms is 1 else returns studio
  if (bedrooms === 1) {
    return "studio";
  }
  return Object.keys(bathObj)[0];
}
// service base prices
export function getBasePrice() {
  // Default to 0 in case no matching pricing is found
  let basePrice = 0;

  const { category, service, bedrooms, bathrooms } = bookingData;

  // Only handle residential cleaning in this function for now
  if (category === "residential_cleaning") {
    const servicePricing = residentialPricing[service];
    const bedroomPricing = servicePricing?.[bedrooms];

    if (bedroomPricing) {
      // Use first available bathroom key if bathroom is 0
      const selectedBathroom =
        bathrooms !== 0 ? bathrooms : getFirstKey(bedrooms, bedroomPricing);
      basePrice = bedroomPricing?.[selectedBathroom] ?? 0;
    }
  } else {
    // Fallback for other categories
    basePrice = bookingState.serviceCost ?? 0;
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
