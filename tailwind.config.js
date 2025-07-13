/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: "#024522",
        secondary: "#bcb330",
        tertiary: "#f2f2f2",
      },
    },
  },
  plugins: [],
};