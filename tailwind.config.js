/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",   // global templates
    "./tradingapp/templates/**/*.html", // app templates
    "./tradingapp/**/*.py",    // if you want safelist inside python
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
