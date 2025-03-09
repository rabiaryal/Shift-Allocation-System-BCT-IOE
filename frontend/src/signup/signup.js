import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Form, Input, Button, Card, Typography, Space, message } from "antd";
import { LockOutlined, UserOutlined, MailOutlined } from "@ant-design/icons";
import { motion } from "framer-motion";

const { Title, Text } = Typography;

const Signup = () => {
	const [loading, setLoading] = useState(false);
	const navigate = useNavigate();

	const handleSignup = async (values) => {
		setLoading(true);
		message.loading({ content: "Creating account...", key: "signup" });

		try {
			console.log("Signing up with", values.userName, values.email, values.password);
			message.success({ content: "Account created successfully! Redirecting to login...", key: "signup" });
			setTimeout(() => navigate("/login"), 1000);
		} catch (err) {
			message.error({ content: "Error signing up. Please try again.", key: "signup" });
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
				background: "linear-gradient(135deg, #74EBD5 0%, #9FACE6 100%)",
			}}
		>
			<motion.div initial={{ scale: 0.9 }} animate={{ scale: 1 }} transition={{ duration: 0.3 }}>
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
					<Title level={2} style={{ marginBottom: "10px", color: "#333" }}>
						Create an Account
					</Title>
					<Text type="secondary">Enter your details to sign up</Text>

					<Form name="signup-form" onFinish={handleSignup} layout="vertical" style={{ marginTop: "20px" }}>
						<Form.Item name="userName" rules={[{ required: true, message: "Please enter your username!" }]}> 
							<Input prefix={<UserOutlined />} placeholder="Username" />
						</Form.Item>

						<Form.Item name="email" rules={[{ required: true, message: "Please enter your email!" }, { type: "email", message: "Please enter a valid email!" }]}>
							<Input prefix={<MailOutlined />} placeholder="Email address" />
						</Form.Item>

						<Form.Item name="password" rules={[{ required: true, message: "Please enter your password!" }]}> 
							<Input.Password prefix={<LockOutlined />} placeholder="Password" />
						</Form.Item>

						<Form.Item>
							<Button type="primary" htmlType="submit" loading={loading} block style={{ height: "40px", fontSize: "16px", background: "#1890ff", borderColor: "#1890ff" }}>
								Sign Up
							</Button>
						</Form.Item>
					</Form>

					<Space direction="vertical" size="small">
						<Text type="secondary">
							Already have an account? <a href="/login">Login</a>
						</Text>
					</Space>
				</Card>
			</motion.div>
		</div>
	);
};

export default Signup;
