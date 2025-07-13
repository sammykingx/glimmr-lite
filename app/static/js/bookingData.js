// Booking data object
export let bookingData = {
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

// initializer
export let currentStep = 1;
export let totalPrice = 90;

export const setTotalPrice = (price) => (totalPrice = price);
export const setCurrentStep = (step) => (currentStep = step);