// Booking data object
export let bookingData = {
  category: "",
  service: "",
  bedrooms: 1,
  bathrooms: 0, // values are [studio, 1, 2, 3]
  frequency: "one_off", // default frequency, can be "one_off", "weekly", "bi-weekly", or "monthly"
  addOns: [],
  selectedDate: "",
  selectedTime: "",
  paymentMethod: "",
  price: 0,
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
    country: "canada", // default country
  },
  additionalInfo: "",
};

// initializer
export const bookingState = {
  currentStep: 1,
  totalPrice: 0,
  serviceCost: 0,
  subtotal: 0,
  discountPrice: 0,
  addonPrice: 0,
  tax: 0,
  serviceLabel: null,
};

export const setTotalPrice = (price) => (bookingState.totalPrice = price);
export const increaseCurrentStep = () => bookingState.currentStep++;
export const decreaseCurrentStep = () => bookingState.currentStep--;
export const setCurrentStep = (value) => (bookingState.currentStep = value);
export const setServiceCost = (amount) => (bookingState.serviceCost = amount);

export function resetBookingData() {
  bookingData = {
    category: "",
    service: "",
    bedrooms: 1,
    bathrooms: 0,
    frequency: "one_off",
    addOns: [],
    selectedDate: "",
    selectedTime: "",
    paymentMethod: "",
    price: 0,
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
    },
    additionalInfo: "",
  };
}

export const resetBookingState = () => {
  bookingState.currentStep = 1;
  bookingState.totalPrice = 0;
  bookingState.serviceCost = 0;
  bookingState.subtotal = 0;
  bookingState.discountPrice = 0;
  bookingState.addonPrice = 0;
  bookingState.tax = 0;
  bookingState.serviceLabel = null;
};
