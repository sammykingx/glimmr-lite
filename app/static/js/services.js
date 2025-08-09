import { bookingData, bookingState, setServiceCost } from "./bookingData.js";
import { updateNextButton, updateProgress } from "./uiHelpers.js";
import { updateTotalPrice } from "./pricing.js";
import { residentialPricing } from "./constants.js";

// Select category
export function selectCategory(category, event) {
  bookingData.category = category;
  bookingData.service = null;
  setServiceCost(0); // always start the price at zero

  // Update UI
  document.querySelectorAll(".category-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target
    .closest(".category-btn")
    .classList.add("border-primary", "bg-green-50");
  //event.target.closest(".category-btn").classList.remove("border-gray-200");

  updateNextButton();
  updateTotalPrice();
}

// Select service
export function selectService(service, amount, label, event) {
  if (
    bookingData.category === "commercial_cleaning" &&
    service.toLowerCase() === "custom"
  ) {
    bookingData.category = "";
    document.querySelectorAll(".category-btn").forEach((btn) => {
      btn.classList.remove("border-primary", "bg-green-50");
      btn.classList.add("border-gray-200");
    });
    location.href =
      "mailto:booking@oliveglitters.com?subject=Custom Cleaning Service Request";
    return;
  }
  bookingData.service = service;
  bookingState.serviceLabel =
    bookingData.category !== "residential_cleaning" ? label : "";
  const excludedCategories = ["residential_cleaning"]; //"commercial_cleaning"];
  if (!excludedCategories.includes(bookingData.category)) {
    //
    setServiceCost(amount);
  } else if (bookingData.category === "residential_cleaning") {
    //bookingData.bathrooms = "studio";
    renderBedAndBathOptions(bookingData.service);
  }

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
  bookingData.bathrooms = 0; // reset bathrooms to 0 when bedrooms change after selecting bedrooms and bathrooms
  renderBathrooms(bookingData.service, num);

  // Update UI
  document.querySelectorAll(".bedroom-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target.classList.add("border-primary", "bg-green-50");
  event.target.classList.remove("border-gray-200");

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

  const bathroomDisplay =
    Number.isInteger(+num) && +num > 0
      ? `${num} bath${+num > 1 ? "s" : ""}`
      : `${num}`;

  document.getElementById("bathroomDisplay").textContent = bathroomDisplay;
  updateTotalPrice();
  updateNextButton();
  displayPropertySummary();
}

// Toggle add-on
export function toggleAddOn(addOn, amount, event) {
  const index = bookingData.addOns.findIndex((a) => a.name === addOn);
  const button = event.target.closest(".addon-btn");

  if (index > -1) {
    bookingData.addOns.splice(index, 1);
    button.classList.remove("border-primary", "bg-green-50");
    button.classList.add("border-gray-200");
  } else {
    const newAddon = { name: addOn, price: amount };
    bookingData.addOns.push(newAddon);
    button.classList.add("border-primary", "bg-green-50");
    button.classList.remove("border-gray-200");
  }

  // Update add-on summary
  const summary = document.getElementById("addOnSummary");
  const count = document.getElementById("addOnCount");
  const total = document.getElementById("addOnTotal");

  updateTotalPrice();

  if (bookingData.addOns.length > 0) {
    summary.classList.remove("hidden");
    count.textContent = bookingData.addOns.length;
    total.textContent = bookingState.addonPrice.toLocaleString("en-CA", {
      style: "currency",
      currency: "CAD",
    });
  } else {
    summary.classList.add("hidden");
  }

  updateNextButton();
}

// Select frequency
export function selectFrequency(frequency, event) {
  const isSelected = bookingData.frequency === frequency;
  bookingData.frequency = isSelected ? "one_off" : frequency;

  // Reset all buttons
  document
    .querySelectorAll(".frequency-btn")
    .forEach(
      (btn) =>
        btn.classList.toggle("border-primary", false) ||
        btn.classList.toggle("bg-green-50", false) ||
        btn.classList.toggle("border-gray-200", true)
    );

  // Highlight only if newly selected
  if (!isSelected) {
    event.target.classList.toggle("border-primary", true);
    event.target.classList.toggle("bg-green-50", true);
    event.target.classList.toggle("border-gray-200", false);
  }

  updateTotalPrice();
  updateNextButton();
}

function renderBedAndBathOptions(service) {
  if (!residentialPricing[service]) return;

  const pricing = residentialPricing[service];
  const bedroomOptionsContainer = document.getElementById("bedroomOptions");
  const bathroomOptionsContainer = document.getElementById("bathroomOptions");

  // Clear existing options
  bedroomOptionsContainer.innerHTML = "";
  // bathroomOptionsContainer.innerHTML = "";

  // Get sorted list of bedrooms
  const bedroomKeys = Object.keys(pricing).sort((a, b) => +a - +b);

  // Populate bedrooms
  bedroomKeys.forEach((bedroom) => {
    const button = document.createElement("button");
    button.className =
      "bedroom-btn p-4 rounded-lg border-2 border-gray-200 hover:border-gray-300 transition-all duration-200 hover:shadow-md hover-card";
    button.setAttribute("data-bedrooms", bedroom);
    button.innerHTML = `<span class="text-primary font-bold text-lg">${bedroom}</span>`;
    button.addEventListener("click", (e) => {
      selectBedrooms(Number(e.target.dataset.bedrooms), e);
    });
    bedroomOptionsContainer.appendChild(button);
  });

  // Automatically trigger bathroom rendering for first bedroom
  const defaultBedroom = bedroomKeys[0];
  renderBathrooms(service, defaultBedroom);
  //const bathroomDisplay = "studio"; //default is studio
}

// Renders bathrooms when a bedroom is selected
function renderBathrooms(service, bedroom) {
  const pricing = residentialPricing[service];
  const bathrooms = pricing?.[bedroom];
  const bathroomOptionsContainer = document.getElementById("bathroomOptions");

  bathroomOptionsContainer.innerHTML = "";

  if (!bathrooms) return;

  const bathroomKeys = Object.keys(bathrooms);

  bathroomKeys.forEach((bathroom) => {
    const label = bathroom === "studio" ? "Studio" : bathroom;
    const button = document.createElement("button");
    button.className =
      "bathroom-btn p-4 rounded-lg border-2 border-gray-200 hover:border-gray-300 transition-all duration-200 hover:shadow-md hover-card";
    button.setAttribute("data-bathrooms", bathroom);
    button.innerHTML = `<span class="text-primary font-bold text-lg">${label}</span>`;
    button.addEventListener("click", (e) => {
      selectBathrooms(e.target.dataset.bathrooms, e);
    });
    bathroomOptionsContainer.appendChild(button);
  });
}

function displayPropertySummary() {
  const { bedrooms, bathrooms, service } = bookingData;

  // Exit if any of the required fields are missing
  if (!bedrooms || !bathrooms || !service) return;

  const price = residentialPricing?.[service]?.[bedrooms]?.[bathrooms] || 0;

  document.getElementById("bedroomDisplay").textContent = bedrooms;
  document.getElementById("bathroomDisplay").textContent = Number.isInteger(
    +bathrooms
  )
    ? `${+bathrooms} bath${+bathrooms > 1 ? "s" : ""}`
    : bathrooms;
  console.log(Number.isInteger(+bathrooms), typeof bathrooms);
  document.getElementById("propertyPrice").textContent = price.toLocaleString(
    "en-CA",
    { style: "currency", currency: "CAD" }
  );

  const summary = document.getElementById("propertySummary");
  if (summary) {
    // only show if the summary element exists
    summary.classList.remove("hidden");
  }
}
