import axios from "axios";

const logout = async () => {
    try {
        const refreshToken = localStorage.getItem("refresh_token"); // Retrieve refresh token from storage

        if (!refreshToken) {
            console.error("No refresh token found");
            return;
        }

        await axios.post("http://127.0.0.1:8000/logout/", {
            refresh_token: refreshToken
        }, {
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("access_token")}`
            }
        });

        // Clear tokens from localStorage
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");

        alert("Logout successful");
        window.location.href = "/login"; // Redirect to login page
    } catch (error) {
        console.error("Logout failed:", error.response?.data || error.message);
    }
};
