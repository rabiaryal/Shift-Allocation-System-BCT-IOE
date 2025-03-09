import React, { useRef, useState } from "react";

import "antd/dist/reset.css";
import {
	Form,
	Input,
	Button,
	Typography,
	InputNumber,
	Row,
	Col,
	Card,
	Select,
	notification,
} from "antd";
import {
	UserOutlined,
	MailOutlined,
	IdcardOutlined,
	ClockCircleOutlined,
	SolutionOutlined,
	StarOutlined,
} from "@ant-design/icons";

const { Title } = Typography;
const { Option } = Select;

const AddEmployeeRecord = () => {
	const [form] = Form.useForm();
	const [loading, setLoading] = useState(false);
	const isAddingAnother = useRef(false);
	const [toast, setToast] = useState(null); 

	
	const [api, contextHolder] = notification.useNotification();

	const handleSubmit = async (values) => {
		setLoading(true);
		try {
			const response = await fetch("http://127.0.0.1:8000/api/employees/", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(values),
			});
	
			const data = await response.json();
	
			if (response.ok) {
				api.success({
					message: "Success",
					description: "Employee added successfully!",
					placement: "topRight",
				});
				if (isAddingAnother.current) {
					form.resetFields();
					isAddingAnother.current = false;
				}
			} else {
				// Extract detailed error messages
				const errorMessages = Object.keys(data)
					.map((key) => `${key}: ${data[key].join(", ")}`)
					.join("\n");
	
				api.error({
					message: "Error",
					description: errorMessages || "Failed to add employee",
					placement: "topRight",
				});
			}
		} catch (error) {
			api.error({
				message: "Error",
				description: "Error adding employee. Please try again.",
				placement: "topRight",
			});
		} finally {
			setLoading(false);
		}
	};
	

	const handleAddAnother = () => {
		isAddingAnother.current = true;
		form.submit();
	};

	const handleReset = () => {
		form.resetFields();
		setToast({ type: "info", message: "Form Cleared", description: "The form has been reset successfully." });
	};

	const priorityOptions = Array.from(
		{ length: 11 },
		(_, index) => 10 - index
	);
	return (
		<div
			style={{
				width: "100vw",
				minHeight: "100vh",
				display: "flex",
				justifyContent: "center",
				alignItems: "flex-start", // Change from center to flex-start
				paddingTop: "60px", // Adjust as needed
			}}
		>
			<Card
				style={{
					width: "90%",
					maxWidth: 1200,
					padding: "20px",
					boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
				}}
			>
				<Title
					level={2}
					style={{
						textAlign: "center",
						marginBottom: "24px",
					}}
				>
					Enter the New Employee Details
				</Title>
				<Form
					form={form}
					layout="horizontal"
					onFinish={handleSubmit}
				>
					<Row gutter={[24, 16]}>
						<Col xs={24} sm={12} md={8}>
							<Form.Item
								label="Employee ID"
								name="e_id"
								rules={[
									{
										required: true,
										message: "Please enter employee ID",
										pattern: new RegExp(/^[A-Z0-9]+$/),
										message:
											"Invalid ID format (letters and numbers only)",
									},
								]}
							>
								<InputNumber
									prefix={<IdcardOutlined />}
									style={{ width: "100%" }}
									min={1}
									max={9999}
									placeholder="E-1234"
								/>
							</Form.Item>
						</Col>

						<Col xs={24} sm={12} md={8}>
							<Form.Item
								label="Full Name"
								name="e_name"
								rules={[
									{
										required: true,
										message: "Please enter employee name",
										min: 3,
										message:
											"Name must be at least 3 characters",
									},
								]}
							>
								<Input
									prefix={<UserOutlined />}
									placeholder="John Doe"
									allowClear
								/>
							</Form.Item>
						</Col>

						<Col xs={24} sm={12} md={8}>
							<Form.Item
								label="Hours Worked"
								name="no_of_hours_worked"
								rules={[
									{
										required: true,
										message: "Please enter hours worked",
									},
								]}
							>
								<InputNumber
									prefix={<ClockCircleOutlined />}
									style={{ width: "100%" }}
									min={0}
									max={80}
									step={0.5}
									decimalSeparator="."
									formatter={(value) => `${value}h`}
									parser={(value) => value.replace("h", "")}
								/>
							</Form.Item>
						</Col>

						<Col xs={24} sm={12} md={8}>
							<Form.Item
								label="Designation"
								name="designation"
								rules={[
									{
										required: true,
										message: "Please select designation",
									},
								]}
							>
								<Select
									placeholder="Select role"
									options={[
										{
											value: "Cashier",
											label: "Cashier",
										},
										{
											value: "Cleaner",
											label: "Cleaning Staff",
										},
										{
											value: "Manager",
											label: "Manager",
										},
										{
											value: "Inventory Manager",
											label: "Inventory Manager",
										},
										{
											value: "Customer Help",
											label: "Customer Help",
										},
										{
											value: "Supervisor",
											label: "Supervisor",
										},
									]}
									suffixIcon={<SolutionOutlined />}
								/>
							</Form.Item>
						</Col>

						<Col xs={24} sm={12} md={8}>
							<Form.Item
								label="Work Email"
								name="e_gmail"
								rules={[
									{
										type: "email",
										required: true,
										message:
											"Please enter valid email address",
									},
								]}
							>
								<Input
									prefix={<MailOutlined />}
									placeholder="john@company.com"
									allowClear
								/>
							</Form.Item>
						</Col>

						<Col xs={24} sm={12} md={8}>
							<Form.Item
								label="Priority Level"
								name="e_priority"
								rules={[
									{
										required: true,
										message: "Please select priority level",
									},
									{
										type: "number",
										min: 0,
										max: 10,
										message:
											"Priority must be between 0-10",
									},
								]}
							>
								<Select
									placeholder="Select priority level"
									suffixIcon={<StarOutlined />}
									showSearch
									optionFilterProp="children"
								>
									{priorityOptions.map((value) => (
										<Option key={value} value={value}>
											{value} -{" "}
											{value === 10
												? "Highest Priority"
												: value === 0
												? "Lowest Priority"
												: `Priority Level ${10 - value}`}
										</Option>
									))}
								</Select>
							</Form.Item>
						</Col>
					</Row>

					<Row
						justify="center"
						gutter={16}
						style={{ marginTop: 32 }}
					>
						<Col>
							<Button
								type="primary"
								htmlType="submit"
								style={{
									marginLeft: "10px",
									background:
										"linear-gradient(135deg, #36D1DC 0%, #5B86E5 100%)",

									fontSize: "18px",
									padding: "12px 24px",
								}}
								size="large"
								loading={loading}
								disabled={loading}
							>
								Add Employee
							</Button>
						</Col>
						<Col>
							<Button
								type="default"
								size="large"
								onClick={handleAddAnother}
								loading={loading}
								disabled={loading}
							>
								Add Another
							</Button>
						</Col>
						<Col>
							<Button
								type="dashed"
								size="large"
								onClick={handleReset}
								danger
							>
								Clear Form
							</Button>
						</Col>
					</Row>
				</Form>
			</Card>
		</div>
	);
};

export default AddEmployeeRecord;
