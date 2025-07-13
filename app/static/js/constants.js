// Service categories
export const serviceCategories = {
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

export const frequencyMultipliers = {
  weekly: 1.0,
  "bi-weekly": 0.9,
  monthly: 0.8,
};

export const paymentMethods = {
  interac: "Interac (Email)",
  onsite: "Pay On Site",
  stripe: "Stripe",
  paystack: "Paystack",
  applepay: "Apple Pay",
  googlepay: "Google Pay",
};

// addons services