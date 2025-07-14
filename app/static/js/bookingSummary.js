import { bookingData, bookingState } from "./bookingData.js";
import { calculateBasePrice } from "./pricing.js"; //passed
import { frequencyMultipliers, paymentMethods } from "./constants.js"; //passed

// export function updateBookingSummary() { ... }

export function updateBookingSummary() {
  const totalPrice = bookingState.totalPrice;
  document.getElementById("summaryCategory").textContent =
    bookingData.category || "-";
  document.getElementById("summaryService").textContent =
    bookingData.service || "-";
  document.getElementById("summaryProperty").textContent = `${
    bookingData.bedrooms
  } bedroom${bookingData.bedrooms > 1 ? "s" : ""}, ${
    bookingData.bathrooms
  } bathroom${bookingData.bathrooms > 1 ? "s" : ""}`;
  document.getElementById("summaryFrequency").textContent =
    bookingData.frequency
      ? bookingData.frequency.charAt(0).toUpperCase() +
        bookingData.frequency.slice(1)
      : "-";

  // Schedule
  if (bookingData.selectedDate) {
    const date = new Date(bookingData.selectedDate);
    document.getElementById("summaryDate").textContent =
      date.toLocaleDateString("en-US", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
      });
  }
  document.getElementById("summaryTime").textContent =
    bookingData.selectedTime || "-";

  // Payment & Contact
  document.getElementById("summaryPayment").textContent =
    bookingData.paymentMethod ? paymentMethods[bookingData.paymentMethod] : "-";
  document.getElementById("summaryContact").textContent =
    bookingData.personalInfo.firstName && bookingData.personalInfo.lastName
      ? `${bookingData.personalInfo.firstName} ${bookingData.personalInfo.lastName}`
      : "John Doe";

  // Add-ons
  const addOnsSection = document.getElementById("summaryAddOns");
  const addOnsList = document.getElementById("summaryAddOnsList");
  if (bookingData.addOns.length > 0) {
    addOnsList.innerHTML = "";
    bookingData.addOns.forEach((addOn) => {
      const div = document.createElement("div");
      div.className = "flex justify-between";
      div.innerHTML = `<span>${addOn}</span><span>+$30</span>`;
      addOnsList.appendChild(div);
    });
    addOnsSection.classList.remove("hidden");
  } else {
    addOnsSection.classList.add("hidden");
  }

  // Price breakdown
  const basePrice = calculateBasePrice(
    bookingData.bedrooms,
    bookingData.bathrooms
  );
  const frequencyMultiplier = bookingData.frequency
    ? frequencyMultipliers[bookingData.frequency]
    : 1;
  const addOnPrice = bookingData.addOns.length * 30;
  const discountAmount = basePrice - basePrice * frequencyMultiplier;

  document.getElementById("summaryBasePrice").textContent =
    "$" + Math.round(basePrice * frequencyMultiplier);

  if (addOnPrice > 0) {
    document.getElementById("summaryAddOnPrice").classList.remove("hidden");
    document
      .getElementById("summaryAddOnPrice")
      .querySelector("span:last-child").textContent = "+$" + addOnPrice;
  } else {
    document.getElementById("summaryAddOnPrice").classList.add("hidden");
  }

  if (discountAmount > 0) {
    document.getElementById("summaryDiscount").classList.remove("hidden");
    document
      .getElementById("summaryDiscount")
      .querySelector("span:last-child").textContent =
      "-$" + Math.round(discountAmount);
  } else {
    document.getElementById("summaryDiscount").classList.add("hidden");
  }

  document.getElementById("summaryTotal").textContent = "$" + totalPrice;
}
