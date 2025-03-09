import React from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "antd";
import { PlusCircleOutlined, TeamOutlined } from "@ant-design/icons";

const Home = () => {
    const navigate = useNavigate();

    return (
        <div
            style={{
                display: "flex",
                justifyContent: "space-between", // Buttons at both ends
                alignItems: "flex-start", // Align to top
                minHeight: "100vh",
                background: "#f0f2f5",
                padding: "5%",
                position: "relative",
                paddingTop: "10%", // Move buttons slightly up
            }}
        >
            <Button
                type="primary"
                icon={<PlusCircleOutlined style={{ fontSize: "1.875rem" }} />} // Increased by 25%
                onClick={() => navigate("/addemployeerecords")}
                size="large"
                style={{
                    width: "31.25%", // Increased by 25%
                    height: "109.375px", // Increased by 25%
                    fontSize: "1.71875rem", // Increased by 25%
                    borderRadius: 12,
                    background: "linear-gradient(135deg, #36D1DC 0%, #5B86E5 100%)",
                    border: "none",
                    boxShadow: "0 4px 6px rgba(54, 209, 220, 0.3)",
                    transition: "all 0.3s",
                }}
                onMouseEnter={(e) => {
                    e.target.style.transform = "translateY(-2px)";
                    e.target.style.boxShadow = "0 6px 8px rgba(54, 209, 220, 0.4)";
                }}
                onMouseLeave={(e) => {
                    e.target.style.transform = "translateY(0)";
                    e.target.style.boxShadow = "0 4px 6px rgba(54, 209, 220, 0.3)";
                }}
            >
                Add New Employee
            </Button>

            <Button
                type="primary"
                icon={<TeamOutlined style={{ fontSize: "1.875rem" }} />} // Increased by 25%
                onClick={() => navigate("/viewemployeedetails")}
                size="large"
                style={{
                    width: "31.25%", // Increased by 25%
                    height: "109.375px", // Increased by 25%
                    fontSize: "1.71875rem", // Increased by 25%
                    borderRadius: 12,
                    background: "linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%)",
                    border: "none",
                    boxShadow: "0 4px 6px rgba(255, 107, 107, 0.3)",
                    transition: "all 0.3s",
                }}
                onMouseEnter={(e) => {
                    e.target.style.transform = "translateY(-2px)";
                    e.target.style.boxShadow = "0 6px 8px rgba(255, 107, 107, 0.4)";
                }}
                onMouseLeave={(e) => {
                    e.target.style.transform = "translateY(0)";
                    e.target.style.boxShadow = "0 4px 6px rgba(255, 107, 107, 0.3)";
                }}
            >
                View Employee Records
            </Button>
        </div>
    );
};

export default Home;
