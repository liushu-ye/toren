/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          primary: '#007bff',
        },
      },
      borderRadius: {
        panel: '0.25rem',
      },
    },
  },
  plugins: [],
}