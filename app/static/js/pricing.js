import { bookingData, setTotalPrice } from "./bookingData.js";
import { frequencyMultipliers } from "./constants.js";

// service base prices
export function calculateBasePrice(bedrooms, bathrooms) {
  const bedroomPrice = 90 + (bedrooms - 1) * 25;
  const bathroomPrice = (bathrooms - 1) * 15;
  return bedroomPrice + bathroomPrice;
}

// updates app's total price
export function updateTotalPrice() {
  const basePrice = calculateBasePrice(
    bookingData.bedrooms,
    bookingData.bathrooms
  );
  const frequencyMultiplier = bookingData.frequency
    ? frequencyMultipliers[bookingData.frequency]
    : 1;
  const addOnPrice = bookingData.addOns.length * 30;
  const total = Math.round(basePrice * frequencyMultiplier + addOnPrice);
  setTotalPrice(total);

    // DOM update logic here
    
    document.getElementById("totalPrice").textContent = "$" + totalPrice;
    document.getElementById("finalPrice").textContent = totalPrice;

    // Update frequency prices
    document.getElementById("weeklyPrice").textContent =
      "$" + Math.round(basePrice * 1.0);
    document.getElementById("biWeeklyPrice").textContent =
      "$" + Math.round(basePrice * 0.9);
    document.getElementById("monthlyPrice").textContent =
      "$" + Math.round(basePrice * 0.8);

    // Update base price display
    document.getElementById("basePrice").textContent = "$" + basePrice;
}
