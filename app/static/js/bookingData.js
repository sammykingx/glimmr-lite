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
    zipCode: "",
  },
  additionalInfo: "",
};

// initializer
export const bookingState = {
  currentStep: 1,
  totalPrice: 90,
};

export const setTotalPrice = (price) => (bookingState.totalPrice = price);
export const increaseCurrentStep = () => bookingState.currentStep++;
export const decreaseCurrentStep = () => bookingState.currentStep--;

export function resetBookingData() {
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
      zipCode: "",
    },
    additionalInfo: "",
  };
}