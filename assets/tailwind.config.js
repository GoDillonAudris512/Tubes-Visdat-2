module.exports = {
    content: ["./assets/**/*.{html,js}", "./components/**/*.py", "./**/*.py"],
    theme: {
        extend: {
            colors: {
                primary: "#2C3E50",
                secondary: "#FF5A5F",
                success: "#27ae60",
                danger: "#e74c3c",
                info: "#3498db",
            },
            fontFamily: {
                sans: ["Open Sans", "sans-serif"],
            },
        },
    },
    plugins: [],
};
