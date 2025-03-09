import React, { useState, useEffect } from "react";
import { Layout, Menu, ConfigProvider } from "antd";
import { Link, useLocation, useNavigate } from "react-router-dom";
import {
	HomeOutlined,
	FormOutlined,
	SwapOutlined,
	UserAddOutlined,
	LogoutOutlined,
	EyeOutlined,
} from "@ant-design/icons";
import axios from "axios";

const { Header } = Layout;

const Navbar = () => {
	const location = useLocation();
	const navigate = useNavigate();
	const [selectedKey, setSelectedKey] = useState(location.pathname);

	useEffect(() => {
		setSelectedKey(location.pathname);
	}, [location]);

	// Logout function
	const logout = async () => {
		try {
			const accessToken = localStorage.getItem("access_token");
			if (!accessToken) {
				console.warn("No access token found, forcing logout...");
				handleForcedLogout();
				return;
			}
	
			await axios.post(
				"http://127.0.0.1:8000/api/auth/logout/",
				{}, 
				{
					headers: {
						Authorization: `Bearer ${accessToken}`,
						"Content-Type": "application/json",
					},
				}
			);
	
			// Clear tokens from localStorage
			localStorage.removeItem("access_token");
			localStorage.removeItem("refresh_token");
	
			alert("Logout successful");
			
			// Replace history to prevent going back
			navigate("/login", { replace: true });
	
			// Reload the page to clear any cached session
			window.location.reload();
		} catch (error) {
			console.error("Logout failed:", error.response?.data || error.message);
			handleForcedLogout();
		}
	};
	
	// Force logout even if the API fails
	const handleForcedLogout = () => {
		localStorage.removeItem("access_token");
		localStorage.removeItem("refresh_token");
		
		// Ensure navigation history is cleared
		navigate("/login", { replace: true });
	
		// Reload to clear cache
		window.location.reload();
	};
	

	// Menu items array
	const menuItems = [
		{ key: "/", label: "Home", icon: <HomeOutlined />, link: "/home" },
		{ key: "/employeeform", label: "Generate", icon: <FormOutlined />, link: "/employeeform" },
		{ key: "/shiftswap", label: "Shift Swap", icon: <SwapOutlined />, link: "/shiftswap" },
		{ key: "/addemployeerecords", label: "Add Employee", icon: <UserAddOutlined />, link: "/addemployeerecords" },
		{ key: "/schedule", label: "View Report", icon: <EyeOutlined />, link: "/schedule" },
	];

	return (
		<ConfigProvider
			theme={{
				components: {
					Menu: {
						itemHoverBg: "#003366",
						itemHoverColor: "#fff",
						itemSelectedColor: "#fff",
						itemSelectedBg: "#004080",
						colorText: "#d9e8ff",
					},
				},
			}}
		>
			<Header
				style={{
					position: "fixed",
					width: "100%",
					zIndex: 1000,
					top: 0,
					left: 0,
					padding: 0,
					background: "linear-gradient(135deg,rgb(10, 27, 113) 0%,rgb(10, 77, 46) 100%)",
					boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.2)",
					borderBottom: "1px solid #004080",
					fontFamily: "Poppins, sans-serif",
				}}
			>
				<div
					style={{
						maxWidth: 1200,
						margin: "0 auto",
						padding: "0 24px",
						display: "flex",
						alignItems: "center",
						justifyContent: "space-between",
					}}
				>
					{/* Logo */}
					<div
						className="logo"
						style={{
							fontSize: 22,
							fontWeight: 700,
							color: "#fff",
							marginRight: "32px",
							transition: "0.3s",
							cursor: "pointer",
						}}
					>
						<Link to="/home" style={{ textDecoration: "none", color: "#fff" }}>
							SAS
						</Link>
					</div>

					{/* Navigation Menu */}
					<Menu
						mode="horizontal"
						selectedKeys={[selectedKey]}
						onClick={(e) => setSelectedKey(e.key)}
						style={{
							background: "transparent",
							borderBottom: "none",
							flex: 1,
							color: "#d9e8ff",
						}}
					>
						{menuItems.map((item) => (
							<Menu.Item key={item.key} icon={item.icon}>
								<Link to={item.link} style={{ color: "inherit", textDecoration: "none" }}>
									{item.label}
								</Link>
							</Menu.Item>
						))}

						{/* Logout Button */}
						<Menu.Item
							key="/logout"
							icon={<LogoutOutlined style={{ fontSize: "14px" }} />}
							style={{
								color: "#fff",
								fontWeight: 500,
								marginLeft: "auto",
								fontSize: "12px",
								display: "flex",
								alignItems: "center",
								justifyContent: "center",
								background: "transparent",
								cursor: "pointer",
							}}
							onClick={logout}
						>
							Log Out
						</Menu.Item>
					</Menu>
				</div>
			</Header>
		</ConfigProvider>
	);
};

export default Navbar;
