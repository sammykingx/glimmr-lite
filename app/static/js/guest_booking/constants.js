// Residential Pricing list
// Bedrooms as parent keys and bathrooms as child keys
export const residentialPricing = {
  house_cleaning: {
    1: { 1: 110, studio: 90 },
    2: { 1: 130, 2: 145, 3: 160 },
    3: { 1: 145, 2: 160, 3: 175 },
    4: { 1: 175, 2: 190, 3: 210 },
    5: { 1: 190, 2: 210, 3: 230 },
    //6: { 1: 230, 2: 245, 3: 260 },
  },
  deep_cleaning: {
    1: { 1: 190, studio: 170 },
    2: { 1: 210, 2: 225, 3: 240 },
    3: { 1: 220, 2: 240, 3: 255 },
    4: { 1: 250, 2: 270, 3: 290 },
    5: { 1: 270, 2: 290, 3: 310 },
    6: { 1: 310, 2: 325, 3: 340 },
  },
  airbnb_cleaning: {
    1: { 1: 150, studio: 130 },
    2: { 1: 170, 2: 185, 3: 205 },
    3: { 1: 185, 2: 200, 3: 215 },
    4: { 1: 210, 2: 230, 3: 250 },
    5: { 1: 230, 2: 250, 3: 270 },
    6: { 1: 260, 2: 280, 3: 300 },
  },
  move_in_move_out_cleaning: {
    1: { 1: 210, studio: 190 },
    2: { 1: 230, 2: 245, 3: 260 },
    3: { 1: 250, 2: 260, 3: 275 },
    4: { 1: 270, 2: 290, 3: 310 },
    5: { 1: 290, 2: 310, 3: 330 },
    6: { 1: 320, 2: 340, 3: 360 },
  },
};

export const frequencyMultipliers = {
  one_off: { multiplier: 1, discount: 0 },
  weekly: { multiplier: 1, discount: 0.05 },
  bi_weekly: { multiplier: 2, discount: 0.1 },
  monthly: { multiplier: 4, discount: 0.15 },
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
