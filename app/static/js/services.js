import { bookingData } from "./bookingData.js";
import { serviceCategories } from "./constants.js";
import { updateNextButton, updateProgress } from "./uiHelpers.js";
import { updateTotalPrice } from "./pricing.js";

// Select category
export function selectCategory(category, event) {
  bookingData.category = category;

  // Update UI
  document.querySelectorAll(".category-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target
    .closest(".category-btn")
    .classList.add("border-primary", "bg-green-50");
  event.target.closest(".category-btn").classList.remove("border-gray-200");

  // Show service options
  const serviceSelection = document.getElementById("serviceSelection");
  const serviceOptions = document.getElementById("serviceOptions");
  serviceOptions.innerHTML = "";

  serviceCategories[category].forEach((service) => {
    const button = document.createElement("button");
    button.className =
      "service-btn p-4 rounded-lg border-2 border-gray-200 hover:border-gray-300 transition-all duration-200 text-left hover:shadow-md hover-card";
    button.dataset.service = service;
    button.innerHTML = `<span class="font-medium">${service}</span>`;
    serviceOptions.appendChild(button);
  });

  serviceSelection.classList.remove("hidden");

  // Attach service button click handlers immediately
  // since service was dynamically added to the DOM
  document.querySelectorAll(".service-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const selected = btn.dataset.service;
      selectService(selected, e);
    });
  });

  updateNextButton();
}

// Select service
export function selectService(service, event) {
  bookingData.service = service;

  // Update UI
  document.querySelectorAll(".service-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target
    .closest(".service-btn")
    .classList.add("border-primary", "bg-green-50");
  event.target.closest(".service-btn").classList.remove("border-gray-200");

  updateTotalPrice();
  updateProgress();
  updateNextButton();
}

// Select bedrooms
export function selectBedrooms(num, event) {
  bookingData.bedrooms = num;

  // Update UI
  document.querySelectorAll(".bedroom-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target.classList.add("border-primary", "bg-green-50");
  event.target.classList.remove("border-gray-200");

  document.getElementById("bedroomDisplay").textContent = num;
  updateTotalPrice();
  updateNextButton();
}

// Select bathrooms
export function selectBathrooms(num, event) {
  bookingData.bathrooms = num;

  // Update UI
  document.querySelectorAll(".bathroom-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target.classList.add("border-primary", "bg-green-50");
  event.target.classList.remove("border-gray-200");

  document.getElementById("bathroomDisplay").textContent = num;
  updateTotalPrice();
  updateNextButton();
}

// Toggle add-on
export function toggleAddOn(addOn, event) {
  const index = bookingData.addOns.indexOf(addOn);
  const button = event.target.closest(".addon-btn");

  if (index > -1) {
    bookingData.addOns.splice(index, 1);
    button.classList.remove("border-primary", "bg-green-50");
    button.classList.add("border-gray-200");
  } else {
    bookingData.addOns.push(addOn);
    button.classList.add("border-primary", "bg-green-50");
    button.classList.remove("border-gray-200");
  }

  // Update add-on summary
  const summary = document.getElementById("addOnSummary");
  const count = document.getElementById("addOnCount");
  const total = document.getElementById("addOnTotal");

  if (bookingData.addOns.length > 0) {
    summary.classList.remove("hidden");
    count.textContent = bookingData.addOns.length;
    total.textContent = "+$" + bookingData.addOns.length * 30;
  } else {
    summary.classList.add("hidden");
  }

  updateTotalPrice();
  updateNextButton();
}

// Select frequency
export function selectFrequency(frequency, event) {
  bookingData.frequency = frequency;

  // Update UI
  document.querySelectorAll(".frequency-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target.classList.add("border-primary", "bg-green-50");
  event.target.classList.remove("border-gray-200");

  updateTotalPrice();
  updateNextButton();
}
