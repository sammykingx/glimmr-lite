import { bookingData, bookingState } from "./bookingData.js";
import { paymentMethods } from "./constants.js"; //passed

// export function updateBookingSummary() { ... }

export function updateBookingSummary() {
  const totalPrice = bookingState.totalPrice;
  bookingData.price = totalPrice;

  // service Details
  let selectedCategory = bookingData.category;
  selectedCategory = selectedCategory
    .replace(/_/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());

  document.getElementById("summaryCategory").textContent =
    selectedCategory || "Not Available";

  document.getElementById("summaryService").textContent = bookingData.service
    .replace(/_/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
  // ? bookingData.category === "residential_cleaning"
  // : `${bookingData.service} (${bookingState.serviceLabel})`;

  let propertyDisplay = null;

  if (bookingData.category === "residential_cleaning") {
    propertyDisplay = `${bookingData.bedrooms} bedroom${
      bookingData.bedrooms > 1 ? "s" : ""
    }, ${bookingData.bathrooms} bathroom${
      bookingData.bathrooms > 1 ? "s" : ""
    }`;
  } else {
    propertyDisplay = bookingState.serviceLabel;
  }

  document.getElementById("summaryProperty").textContent = propertyDisplay;

  const freq = bookingData.frequency || "one off";
  document.getElementById("summaryFrequency").textContent = freq.replace(
    /\b\w/g,
    (c) => c.toUpperCase()
  );

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
      div.innerHTML = `<span class="text-xs md:text-sm text-gray-400">${
        addOn.name
      }</span><span class="text-xs md:text-sm text-gray-400">+${addOn.price.toLocaleString(
        "en-CA",
        {
          style: "currency",
          currency: "CAD",
        }
      )}</span>`;
      addOnsList.appendChild(div);
    });
    addOnsSection.classList.remove("hidden");
  } else {
    addOnsSection.classList.add("hidden");
  }

  // Price breakdown
  // base service display in price breakdown
  document.getElementById("summaryBasePrice").textContent =
    bookingState.subtotal.toLocaleString("en-CA", {
      style: "currency",
      currency: "CAD",
    });

  // addon services in  price breakdown
  if (bookingData.addOns.length > 0) {
    document.getElementById("summaryAddOnPrice").classList.remove("hidden");
    document
      .getElementById("summaryAddOnPrice")
      .querySelector("span:last-child").textContent =
      "+" +
      bookingState.addonPrice.toLocaleString("en-CA", {
        style: "currency",
        currency: "CAD",
      });
  } else {
    document.getElementById("summaryAddOnPrice").classList.add("hidden");
  }

  // Frequency display in price breakdown
  if (bookingState.discountPrice > 0) {
    document.getElementById("summaryDiscount").classList.remove("hidden");
    document
      .getElementById("summaryDiscount")
      .querySelector("span:last-child").textContent =
      "- " +
      bookingState.discountPrice.toLocaleString("en-CA", {
        style: "currency",
        currency: "CAD",
      });
  } else {
    document.getElementById("summaryDiscount").classList.add("hidden");
  }

  document
    .getElementById("taxAmount")
    .querySelector("span:last-child").textContent =
    "+ " +
    bookingState.tax.toLocaleString("en-CA", {
      style: "currency",
      currency: "CAD",
    });

  document.getElementById("summaryTotal").textContent =
    bookingState.totalPrice.toLocaleString("en-CA", {
      style: "currency",
      currency: "CAD",
    });
}
