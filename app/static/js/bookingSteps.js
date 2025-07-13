import { bookingData } from "./bookingData.js"; // passed

export function canProceed(currentStep) {
  switch (currentStep) {
    case 1:
      return bookingData.category && bookingData.service;
    case 2:
      return bookingData.bedrooms && bookingData.bathrooms;
    case 3:
      return bookingData.frequency;
    case 4:
      return true;
    case 5:
      return bookingData.selectedDate && bookingData.selectedTime;
    case 6:
      return bookingData.paymentMethod;
    case 7:
      return (
        Object.values(bookingData.personalInfo).every(Boolean) &&
        Object.values(bookingData.address).every(Boolean)
      );
    case 8:
      return true;
    default:
      return false;
  }
}
