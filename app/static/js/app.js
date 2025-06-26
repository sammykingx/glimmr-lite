// Booking data object
let bookingData = {
  category: "",
  service: "",
  bedrooms: 1,
  bathrooms: 1,
  frequency: "",
  addOns: [],
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
let totalPrice = 0;

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
  "one-off": 1.0,
  weekly: 0.9,
  "bi-weekly": 0.8,
  monthly: 0.7,
};

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
  const progress = (currentStep / 5) * 100;
  document.getElementById(
    "stepIndicator"
  ).textContent = `Step ${currentStep} of 5`;
  document.getElementById("progressPercent").textContent = `${Math.round(
    progress
  )}% complete`;
  document.getElementById("progressBar").style.width = `${progress}%`;
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
    default:
      return false;
  }
}

// Update next button
function updateNextButton() {
  const nextBtn = document.getElementById("nextBtn");
  const bookBtn = document.getElementById("bookBtn");

  if (currentStep < 5) {
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

  if (currentStep < 5) {
    document.getElementById(`step${currentStep}`).classList.remove("active");
    currentStep++;
    document.getElementById(`step${currentStep}`).classList.add("active");

    updateProgress();

    // Show/hide navigation buttons
    if (currentStep > 1) {
      document.getElementById("prevBtn").classList.remove("hidden");
    }

    if (currentStep === 5) {
      document.getElementById("nextBtn").classList.add("hidden");
      document.getElementById("bookBtn").classList.remove("hidden");
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

    if (currentStep < 5) {
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

  const token =
    document.head.querySelector('meta[name="csrf-token"]')?.content || "";
  // Send booking data to server
  fetch("/booking", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
    body: JSON.stringify(bookingData),
  })
    .then((response) => {
      if (!response.ok) {
        if (response.status === 400) {
          throw new Error(
            "Your session was terminated for security reasons. Please refresh the page and try again."
          );
        } else if (response.status === 404) {
          throw new Error(
            "The requested service is not available. Please check and try again."
          );
        } else {
          throw new Error(
            "Our booking service is currently not available, please try again."
          );
        }
        // showNotification(
        //   "There was a problem submitting your booking. Please try again."
        // );
        //return Promise.reject();
      }
      return response.json();
    })
    .then((data) => {
      console.log("Booking successful:", JSON.stringify(data, null, 2));
      //showBookingCompleteModal();
      document.getElementById("confirmedTotal").textContent = "$" + totalPrice;
      document.getElementById("bookingComplete").classList.remove("hidden");
    })
    .catch((error) => {
      console.error("Error during booking:", error);
      alert(error.message);
      window.location.reload();
    });

  // Show booking complete modal
  // document.getElementById("confirmedTotal").textContent = "$" + totalPrice;
  // document.getElementById("bookingComplete").classList.remove("hidden");
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
    personalInfo: { firstName: "", lastName: "", email: "", phone: "" },
    address: { street: "", city: "", state: "", zipCode: "" },
    additionalInfo: "",
  };

  currentStep = 1;
  totalPrice = 0;

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
      ".category-btn, .service-btn, .bedroom-btn, .bathroom-btn, .frequency-btn, .addon-btn"
    )
    .forEach((btn) => {
      btn.classList.remove("border-primary", "bg-green-50");
      btn.classList.add("border-gray-200");
    });

  // Hide service selection
  document.getElementById("serviceSelection").classList.add("hidden");
  document.getElementById("addOnSummary").classList.add("hidden");

  // Reset navigation
  document.getElementById("prevBtn").classList.add("hidden");
  document.getElementById("nextBtn").classList.remove("hidden");
  document.getElementById("bookBtn").classList.add("hidden");

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

  updateTotalPrice();
  updateNextButton();
});
