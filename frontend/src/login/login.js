import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import {
	Form,
	Input,
	Button,
	Checkbox,
	Card,
	Typography,
	Space,
	Spin,
	message,
} from "antd";
import {
	LockOutlined,
	UserOutlined,
	GoogleOutlined,
} from "@ant-design/icons";
import { motion } from "framer-motion";

const { Title, Text } = Typography;

const Login = () => {
	const [loading, setLoading] = useState(false);
	const navigate = useNavigate();

	const handleLogin = async (values) => {
		setLoading(true);
		message.loading({
			content: "Logging in...",
			key: "login",
		});

		// Temporary Credentials
		// const tempManagerID = "1234";
		// const tempPassword = "123456";

		// if (
		// 	values.managerID === tempManagerID &&
		// 	values.password === tempPassword
		// ) {
		// 	message.success({
		// 		content: "Logged in with temporary credentials!",
		// 		key: "login",
		// 	});
		// 	localStorage.setItem("authToken", "tempToken");
		// 	navigate("/home");
		// 	setLoading(false);
		// 	return;
		// }

		try {
			const response = await axios.post(
				"http://127.0.0.1:8000/api/auth/login",
				{
					ManagerID: values.managerID,
					password: values.password,
				}
			);

			console.log(response.data); // Debug API response

			if (response.data.status) {
				alert("Login successful!");
				localStorage.setItem("authStatus", "true"); // Store authentication status
				navigate("/home");
			} else {
				alert(
					response.data.message ||
						"Invalid Manager ID or Password"
				);
			}
		} catch (err) {
			alert("Network Error: Unable to reach the server.");
		} finally {
			setLoading(false);
		}
	};

	return (
		<div
			style={{
				position: "fixed",
				top: 0,
				left: 0,
				width: "100vw",
				height: "100vh",
				display: "flex",
				justifyContent: "center",
				alignItems: "center",
				background:
					"linear-gradient(135deg, #74EBD5 0%, #9FACE6 100%)",
			}}
		>
			<motion.div
				initial={{ scale: 0.9 }}
				animate={{ scale: 1 }}
				transition={{ duration: 0.3 }}
			>
				<Card
					style={{
						width: 420,
						padding: "30px",
						textAlign: "center",
						borderRadius: "12px",
						boxShadow: "0px 10px 30px rgba(0, 0, 0, 0.1)",
						background: "#ffffff",
					}}
				>
					<Title
						level={2}
						style={{ marginBottom: "10px", color: "#333" }}
					>
						Welcome Back
					</Title>
					<Text type="secondary">
						Please enter your login details
					</Text>

					<Form
						name="login-form"
						onFinish={handleLogin}
						layout="vertical"
						style={{ marginTop: "20px" }}
					>
						<Form.Item
							name="managerID"
							rules={[
								{
									required: true,
									message: "Please enter your Manager ID!",
								},
								{
									pattern: /^[0-9]{4}$/,
									message:
										"Manager ID must be exactly 4 digits!",
								},
							]}
						>
							<Input
								prefix={<UserOutlined />}
								placeholder="Enter 4-digit Manager ID"
								maxLength={4}
							/>
						</Form.Item>

						<Form.Item
							name="password"
							rules={[
								{
									required: true,
									message: "Please enter your password!",
								},
							]}
						>
							<Input.Password
								prefix={<LockOutlined />}
								placeholder="Password"
							/>
						</Form.Item>

						<div
							style={{
								display: "flex",
								justifyContent: "space-between",
								alignItems: "center",
								marginBottom: "15px",
							}}
						>
							<a href="/forgot-password">
								Forgot password?
							</a>
						</div>

						<Form.Item>
							<Button
								type="primary"
								htmlType="submit"
								loading={loading}
								block
								style={{
									height: "40px",
									fontSize: "16px",
									background: "#002855",
									borderColor: "#1890ff",
									boxShadow:
										"0px 4px 10px rgba(0, 0, 0, 0.2)",
									borderBottom: "1px solid #004080",
								}}
							>
								{loading ? <Spin /> : "Sign in"}
							</Button>
						</Form.Item>
					</Form>

					<Space
						direction="vertical"
						size="small"
						style={{ marginTop: "15px" }}
					>
						<Text type="secondary">
							Don't have an account?{" "}
							<a href="/signup">Sign up</a>
						</Text>
					</Space>
				</Card>
			</motion.div>
		</div>
	);
};

export default Login;
