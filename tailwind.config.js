module.exports = {
  purge: [`public/**/*.html`],
  theme: {
    container: {
      center: true,
    },
    extend: {},
    fontFamily: {
      sans: ["IBM Plex Mono", "monospace"],
    },
  },
  variants: {},
  plugins: [
    function ({ addComponents }) {
      addComponents({
        ".container": {
          maxWidth: "100%",
          "@screen sm": {
            maxWidth: "640px",
          },
          "@screen md": {
            maxWidth: "860px",
          },
          "@screen lg": {
            maxWidth: "860px",
          },
          "@screen xl": {
            maxWidth: "900px",
          },
        },
      });
    },
  ],
};
