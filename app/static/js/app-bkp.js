// Booking data object
let bookingData = {
  category: "",
  service: "",
  bedrooms: 1,
  bathrooms: 1,
  frequency: "",
  addOns: [],
  selectedDate: "",
  selectedTime: "",
  paymentMethod: "",
  personalInfo: {
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
  },
  address: {
    street: "",
    city: "",
    state: "",
    zipCode: "",
  },
  additionalInfo: "",
};

let currentStep = 1;
let totalPrice = 90;
let currentCalendarDate = new Date();
let maxBookingDate = new Date();
maxBookingDate.setDate(maxBookingDate.getDate() + 45);

// Service categories
const serviceCategories = {
  "Standard Cleaning": [
    "Regular House Cleaning",
    "Apartment Cleaning",
    "Weekly Maintenance",
  ],
  "Deep Cleaning": [
    "Move-in Cleaning",
    "Move-out Cleaning",
    "Spring Cleaning",
    "Post-Construction Cleanup",
  ],
  Specialized: ["Office Cleaning", "Airbnb Cleaning", "Post-Party Cleanup"],
};

// Frequency multipliers
const frequencyMultipliers = {
  weekly: 1.0,
  "bi-weekly": 0.9,
  monthly: 0.8,
};

// Payment method names
const paymentMethods = {
  interac: "Interac (Email)",
  onsite: "Pay On Site",
  stripe: "Stripe",
  paystack: "Paystack",
  applepay: "Apple Pay",
  googlepay: "Google Pay",
};

// Initialize calendar
function initializeCalendar() {
  updateCalendarDisplay();
}

// Update calendar display
function updateCalendarDisplay() {
  const monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  document.getElementById("currentMonth").textContent = `${
    monthNames[currentCalendarDate.getMonth()]
  } ${currentCalendarDate.getFullYear()}`;

  generateCalendarDays();
}

// Generate calendar days
function generateCalendarDays() {
  const calendarDays = document.getElementById("calendarDays");
  calendarDays.innerHTML = "";

  const year = currentCalendarDate.getFullYear();
  const month = currentCalendarDate.getMonth();
  const firstDay = new Date(year, month, 1);
  const lastDay = new Date(year, month + 1, 0);
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  // Add empty cells for days before the first day of the month
  for (let i = 0; i < firstDay.getDay(); i++) {
    const emptyDay = document.createElement("div");
    emptyDay.className = "calendar-day disabled";
    calendarDays.appendChild(emptyDay);
  }

  // Add days of the month
  for (let day = 1; day <= lastDay.getDate(); day++) {
    const dayElement = document.createElement("button");
    const currentDate = new Date(year, month, day);
    const isPast = currentDate < today;
    const isBeyondLimit = currentDate > maxBookingDate;
    const isSelected = bookingData.selectedDate === currentDate.toDateString();

    dayElement.className = `calendar-day p-2 rounded-lg border-2 transition-all duration-200 ${
      isPast || isBeyondLimit
        ? "past cursor-not-allowed"
        : isSelected
        ? "border-primary bg-green-50 text-primary font-bold"
        : "border-gray-200 hover:border-gray-300 hover:shadow-md hover-card"
    }`;

    dayElement.innerHTML = `
                    <div class="text-lg font-medium">${day}</div>
                    <div class="text-xs text-gray-500">${currentDate.toLocaleDateString(
                      "en-US",
                      { weekday: "short" }
                    )}</div>
                `;

    if (!isPast && !isBeyondLimit) {
      dayElement.onclick = () => selectDate(currentDate);
    }

    calendarDays.appendChild(dayElement);
  }
}

// Navigate calendar months
function previousMonth() {
  currentCalendarDate.setMonth(currentCalendarDate.getMonth() - 1);
  updateCalendarDisplay();
}

function nextMonth() {
  currentCalendarDate.setMonth(currentCalendarDate.getMonth() + 1);
  updateCalendarDisplay();
}

// Select date
function selectDate(date) {
  bookingData.selectedDate = date.toDateString();
  updateCalendarDisplay();
  updateScheduleSummary();
  updateNextButton();
}

// Select time
function selectTime(time) {
  bookingData.selectedTime = time;

  // Update UI
  document.querySelectorAll(".time-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target.classList.add("border-primary", "bg-green-50");
  event.target.classList.remove("border-gray-200");

  updateScheduleSummary();
  updateNextButton();
}

// Update schedule summary
function updateScheduleSummary() {
  const summary = document.getElementById("scheduleSummary");
  const scheduleText = document.getElementById("selectedSchedule");

  if (bookingData.selectedDate && bookingData.selectedTime) {
    const date = new Date(bookingData.selectedDate);
    const formattedDate = date.toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    scheduleText.textContent = `${formattedDate} at ${bookingData.selectedTime}`;
    summary.classList.remove("hidden");
  } else {
    summary.classList.add("hidden");
  }
}

// Select payment method
function selectPayment(method) {
  bookingData.paymentMethod = method;

  // Update UI
  document.querySelectorAll(".payment-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target.classList.add("border-primary", "bg-green-50");
  event.target.classList.remove("border-gray-200");

  updateNextButton();
}

// Calculate base price
function calculateBasePrice(bedrooms, bathrooms) {
  const bedroomPrice = 90 + (bedrooms - 1) * 25;
  const bathroomPrice = (bathrooms - 1) * 15;
  return bedroomPrice + bathroomPrice;
}

// Update total price
function updateTotalPrice() {
  const basePrice = calculateBasePrice(
    bookingData.bedrooms,
    bookingData.bathrooms
  );
  const frequencyMultiplier = bookingData.frequency
    ? frequencyMultipliers[bookingData.frequency]
    : 1;
  const addOnPrice = bookingData.addOns.length * 30;
  totalPrice = Math.round(basePrice * frequencyMultiplier + addOnPrice);

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

// Update progress
function updateProgress() {
  const progress = (currentStep / 8) * 100;
  document.getElementById(
    "stepIndicator"
  ).textContent = `Step ${currentStep} of 8`;
  document.getElementById("progressPercent").textContent = `${Math.round(
    progress
  )}% complete`;
  document.getElementById("progressBar").style.width = `${progress}%`;
}

// Update booking summary
function updateBookingSummary() {
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
      : "-";

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

// Select category
function selectCategory(category) {
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
    button.onclick = () => selectService(service);
    button.innerHTML = `<span class="font-medium">${service}</span>`;
    serviceOptions.appendChild(button);
  });

  serviceSelection.classList.remove("hidden");
  updateNextButton();
}

// Select service
function selectService(service) {
  bookingData.service = service;

  // Update UI
  document.querySelectorAll(".service-btn").forEach((btn) => {
    btn.classList.remove("border-primary", "bg-green-50");
    btn.classList.add("border-gray-200");
  });
  event.target.classList.add("border-primary", "bg-green-50");
  event.target.classList.remove("border-gray-200");

  updateNextButton();
}

// Select bedrooms
function selectBedrooms(num) {
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
function selectBathrooms(num) {
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

// Select frequency
function selectFrequency(frequency) {
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

// Toggle add-on
function toggleAddOn(addOn) {
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

// Check if can proceed
function canProceed() {
  switch (currentStep) {
    case 1:
      return bookingData.category && bookingData.service;
    case 2:
      return bookingData.bedrooms && bookingData.bathrooms;
    case 3:
      return bookingData.frequency;
    case 4:
      return true; // Add-ons are optional
    case 5:
      return bookingData.selectedDate && bookingData.selectedTime;
    case 6:
      return bookingData.paymentMethod;
    case 7:
      const firstName = document.getElementById("firstName").value;
      const lastName = document.getElementById("lastName").value;
      const email = document.getElementById("email").value;
      const phone = document.getElementById("phone").value;
      const street = document.getElementById("street").value;
      const city = document.getElementById("city").value;
      const state = document.getElementById("state").value;
      const zipCode = document.getElementById("zipCode").value;

      return (
        firstName &&
        lastName &&
        email &&
        phone &&
        street &&
        city &&
        state &&
        zipCode
      );
    case 8:
      return true; // Summary step
    default:
      return false;
  }
}

// Update next button
function updateNextButton() {
  const nextBtn = document.getElementById("nextBtn");
  const bookBtn = document.getElementById("bookBtn");

  if (currentStep < 8) {
    if (canProceed()) {
      nextBtn.classList.remove(
        "bg-gray-300",
        "text-gray-500",
        "cursor-not-allowed"
      );
      nextBtn.classList.add(
        "bg-primary",
        "text-white",
        "hover:bg-green-800",
        "hover:shadow-lg"
      );
    } else {
      nextBtn.classList.add(
        "bg-gray-300",
        "text-gray-500",
        "cursor-not-allowed"
      );
      nextBtn.classList.remove(
        "bg-primary",
        "text-white",
        "hover:bg-green-800",
        "hover:shadow-lg"
      );
    }
  } else {
    if (canProceed()) {
      bookBtn.classList.remove(
        "bg-gray-300",
        "text-gray-500",
        "cursor-not-allowed"
      );
      bookBtn.classList.add(
        "bg-primary",
        "text-white",
        "hover:bg-green-800",
        "hover:shadow-lg"
      );
    } else {
      bookBtn.classList.add(
        "bg-gray-300",
        "text-gray-500",
        "cursor-not-allowed"
      );
      bookBtn.classList.remove(
        "bg-primary",
        "text-white",
        "hover:bg-green-800",
        "hover:shadow-lg"
      );
    }
  }
}

// Next step
function nextStep() {
  if (!canProceed()) return;

  if (currentStep < 8) {
    document.getElementById(`step${currentStep}`).classList.remove("active");
    currentStep++;
    document.getElementById(`step${currentStep}`).classList.add("active");

    updateProgress();

    // Show/hide navigation buttons
    if (currentStep > 1) {
      document.getElementById("prevBtn").classList.remove("hidden");
    }

    if (currentStep === 8) {
      document.getElementById("nextBtn").classList.add("hidden");
      document.getElementById("bookBtn").classList.remove("hidden");
      updateBookingSummary();
    }

    updateNextButton();
  }
}

// Previous step
function prevStep() {
  if (currentStep > 1) {
    document.getElementById(`step${currentStep}`).classList.remove("active");
    currentStep--;
    document.getElementById(`step${currentStep}`).classList.add("active");

    updateProgress();

    // Show/hide navigation buttons
    if (currentStep === 1) {
      document.getElementById("prevBtn").classList.add("hidden");
    }

    if (currentStep < 8) {
      document.getElementById("nextBtn").classList.remove("hidden");
      document.getElementById("bookBtn").classList.add("hidden");
    }

    updateNextButton();
  }
}

// Handle booking
function handleBooking() {
  if (!canProceed()) return;

  // Collect personal information
  bookingData.personalInfo = {
    firstName: document.getElementById("firstName").value,
    lastName: document.getElementById("lastName").value,
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value,
  };

  bookingData.address = {
    street: document.getElementById("street").value,
    city: document.getElementById("city").value,
    state: document.getElementById("state").value,
    zipCode: document.getElementById("zipCode").value,
  };

  bookingData.additionalInfo = document.getElementById("additionalInfo").value;

  // Show loading modal
  document.getElementById("loadingModal").classList.remove("hidden");

  // Simulate processing time
  setTimeout(() => {
    document.getElementById("loadingModal").classList.add("hidden");

    // Show booking complete modal
    document.getElementById("confirmedTotal").textContent = "$" + totalPrice;

    // Show schedule in confirmation
    if (bookingData.selectedDate && bookingData.selectedTime) {
      const date = new Date(bookingData.selectedDate);
      const formattedDate = date.toLocaleDateString("en-US", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
      });
      document.getElementById(
        "confirmedSchedule"
      ).textContent = `Scheduled for ${formattedDate} at ${bookingData.selectedTime}`;
    }

    document.getElementById("bookingComplete").classList.remove("hidden");

    console.log("Booking Data:", bookingData);
  }, 2000);
}

// Reset booking
function resetBooking() {
  // Reset data
  bookingData = {
    category: "",
    service: "",
    bedrooms: 1,
    bathrooms: 1,
    frequency: "",
    addOns: [],
    selectedDate: "",
    selectedTime: "",
    paymentMethod: "",
    personalInfo: { firstName: "", lastName: "", email: "", phone: "" },
    address: { street: "", city: "", state: "", zipCode: "" },
    additionalInfo: "",
  };

  currentStep = 1;
  totalPrice = 90;

  // Reset UI
  document.getElementById("bookingComplete").classList.add("hidden");
  document
    .querySelectorAll(".step")
    .forEach((step) => step.classList.remove("active"));
  document.getElementById("step1").classList.add("active");

  // Reset form fields
  document
    .querySelectorAll("input, textarea")
    .forEach((field) => (field.value = ""));

  // Reset buttons
  document
    .querySelectorAll(
      ".category-btn, .service-btn, .bedroom-btn, .bathroom-btn, .frequency-btn, .addon-btn, .time-btn, .payment-btn"
    )
    .forEach((btn) => {
      btn.classList.remove("border-primary", "bg-green-50");
      btn.classList.add("border-gray-200");
    });

  // Hide service selection and summaries
  document.getElementById("serviceSelection").classList.add("hidden");
  document.getElementById("addOnSummary").classList.add("hidden");
  document.getElementById("scheduleSummary").classList.add("hidden");

  // Reset navigation
  document.getElementById("prevBtn").classList.add("hidden");
  document.getElementById("nextBtn").classList.remove("hidden");
  document.getElementById("bookBtn").classList.add("hidden");

  // Reset calendar
  currentCalendarDate = new Date();
  updateCalendarDisplay();

  updateProgress();
  updateTotalPrice();
  updateNextButton();
}

// Add event listeners for form validation
document.addEventListener("DOMContentLoaded", function () {
  const formFields = [
    "firstName",
    "lastName",
    "email",
    "phone",
    "street",
    "city",
    "state",
    "zipCode",
  ];
  formFields.forEach((fieldId) => {
    document
      .getElementById(fieldId)
      .addEventListener("input", updateNextButton);
  });

  initializeCalendar();
  updateTotalPrice();
  updateNextButton();
});
