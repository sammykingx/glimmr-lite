import defaultTheme from "tailwindcss/defaultTheme";
import forms from "@tailwindcss/forms";
import typography from "@tailwindcss/typography";
import aspectRatio from "@tailwindcss/aspect-ratio";
import daisyui from "daisyui";

/** @type {import('tailwindcss').Config} */
export default {
  content: ["./app/**/*.{html,js}"],
  safelist: [
    "bg-primary",
    "text-primary",
    "border-primary",
    "bg-secondary",
    "text-secondary",
    "border-secondary",
    "bg-tertiary",
    "text-tertiary",
    "border-tertiary",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#024522",
        secondary: "#bcb330",
        tertiary: "#f2f2f2",

        // Custom colors
        // gray: {
        //   50: "#fafafa",
        //   900: "#111827",
        // },
      },
      fontFamily: {
        sans: ["Inter", ...defaultTheme.fontFamily.sans], // unify fonts
        heading: ["Poppins", ...defaultTheme.fontFamily.sans], // premium template heading font
      },
      spacing: {
        128: "32rem",
        144: "36rem",
      },
      borderRadius: {
        "4xl": "2rem",
      },
    },
  },
  plugins: [forms, typography, aspectRatio, daisyui],
  darkMode: "class", // for multi-theme support (light/dark)
};
