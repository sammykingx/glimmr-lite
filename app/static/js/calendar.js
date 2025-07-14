import { bookingData } from "./bookingData.js"; //passed
import { updateNextButton } from "./uiHelpers.js";

export let currentCalendarDate = new Date();

const maxBookingDate = new Date();
maxBookingDate.setDate(maxBookingDate.getDate() + 45);

// Initialize calendar for display
export function initializeCalendar() {
  updateCalendarDisplay();
}

// Get the current month and year
export function updateCalendarDisplay() {
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
export function generateCalendarDays() {
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

// Navigate calendar months backward
export function previousMonth() {
  currentCalendarDate.setMonth(currentCalendarDate.getMonth() - 1);
  updateCalendarDisplay();
}

// Navigate calendar months forward
export function nextMonth() {
  currentCalendarDate.setMonth(currentCalendarDate.getMonth() + 1);
  updateCalendarDisplay();
}

// Select date
export function selectDate(date) {
  bookingData.selectedDate = date.toDateString();
  updateCalendarDisplay();
  updateScheduleSummary();
  updateNextButton();
}

// Select time
export function selectTime(time, event) {
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
export function updateScheduleSummary() {
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
