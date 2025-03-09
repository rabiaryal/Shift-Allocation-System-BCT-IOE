import React, { useEffect, useState } from "react";
import {
  Card,
  Row,
  Col,
  Typography,
  Button,
  Tag,
  message,
  Modal,
  Input,
  Form,
  Select,
} from "antd";
import {
  UserOutlined,
  ClockCircleOutlined,
  MailOutlined,
  IdcardOutlined,
  DeleteOutlined,
  StarFilled,
  EditOutlined,
} from "@ant-design/icons";

const { Title, Text } = Typography;

const EmployeeView = () => {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(false);
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [selectedEmployee, setSelectedEmployee] = useState(null);
  const [searchQuery, setSearchQuery] = useState(""); // New state for search query
  const [form] = Form.useForm();

  const fetchEmployees = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/api/employees/");
      const data = await response.json();
      setEmployees(data);
    } catch (error) {
      console.error("Error fetching employees:", error);
      message.error("Failed to fetch employee records.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/employees/${id}/`, {
        method: "DELETE",
      });
      if (response.ok) {
        setEmployees(employees.filter((emp) => emp.e_id !== id));
        message.success("Employee deleted successfully.");
      } else {
        message.error("Failed to delete employee.");
      }
    } catch (error) {
      console.error("Error deleting employee:", error);
      message.error("Error deleting employee. Please try again.");
    }
  };

  const handleEdit = (employee) => {
    setSelectedEmployee(employee);
    form.setFieldsValue(employee); // Pre-fill form fields with selected employee details
    setIsModalVisible(true);
  };

  const handleUpdate = async () => {
    try {
      const values = await form.validateFields();
      const response = await fetch(
        `http://127.0.0.1:8000/api/employees/${selectedEmployee.e_id}/`,
        {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(values),
        }
      );
      if (response.ok) {
        setEmployees((prevEmployees) =>
          prevEmployees.map((emp) =>
            emp.e_id === selectedEmployee.e_id ? { ...emp, ...values } : emp
          )
        );
        message.success("Employee updated successfully.");
        setIsModalVisible(false);
      } else {
        message.error("Failed to update employee.");
      }
    } catch (error) {
      console.error("Error updating employee:", error);
      message.error("Error updating employee. Please try again.");
    }
  };

  const getPriorityStars = (priority) => {
    return Array.from({ length: 5 }, (_, index) => (
      <StarFilled
        key={index}
        style={{
          color: index < priority / 2 ? "#ffc107" : "#e0e0e0",
          fontSize: "16px",
          marginRight: 2,
        }}
      />
    ));
  };

  const designationColor = {
    Manager: "#ff4d4f",
    "Cleaning Staff": "#1890ff",
    "Inventory Manager": "#52c41a",
    Supervisor: "#fa8c16",
    Cashier: "#13c2c2",
    "Customer Help": "#eb2f96",
  };

  // Filter employees based on the search query
  const filteredEmployees = employees.filter((employee) =>
    employee.e_name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    employee.e_id.toString().includes(searchQuery) ||
    employee.designation.toLowerCase().includes(searchQuery.toLowerCase()) // Include designation in the search
  );

  return (
    <div style={{ padding: "24px" }}>
      <Title level={2} style={{ color: "#2d3436", marginBottom: "24px" }}>
        👥 Employee Records
      </Title>

      {/* Search Bar */}
      <Input
        placeholder="Search by Employee ID, Name, or Designation"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        style={{ marginBottom: "16px", width: "300px" }}
      />

      {filteredEmployees.length === 0 ? (
        <p style={{ textAlign: "center", fontSize: "16px" }}>
          {loading ? "Loading employees..." : "No employee records found."}
        </p>
      ) : (
        filteredEmployees.map((emp) => (
          <Card
            key={emp.e_id}
            style={{
              marginBottom: 8,
              borderRadius: 12,
              boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
              borderLeft: `4px solid ${
                designationColor[emp.designation] || "#000"
              }`,
            }}
            bodyStyle={{ padding: "16px" }}
            hoverable
          >
            <Row align="middle" gutter={[16, 16]} justify="space-between">
              <Col flex="200px">
                <div style={{ display: "flex", alignItems: "center" }}>
                  <UserOutlined style={{ fontSize: "18px", marginRight: 8 }} />
                  <Text strong style={{ fontSize: "16px" }}>
                    {emp.e_name}
                  </Text>
                </div>
              </Col>

              <Col>
                <Tag
                  icon={<IdcardOutlined />}
                  color={designationColor[emp.designation]}
                  style={{
                    borderRadius: 12,
                    padding: "4px 12px",
                  }}
                >
                  {emp.designation}
                </Tag>
              </Col>

              <Col flex="250px">
                <div style={{ display: "flex", alignItems: "center" }}>
                  <MailOutlined
                    style={{ fontSize: "16px", color: "#ff4d4f", marginRight: 8 }}
                  />
                  <Text type="secondary">{emp.e_gmail}</Text>
                </div>
              </Col>

              <Col>
                <div style={{ display: "flex", alignItems: "center" }}>
                  <ClockCircleOutlined
                    style={{ fontSize: "16px", color: "#fa8c16", marginRight: 8 }}
                  />
                  <Text strong>{emp.no_of_hours_worked}</Text>
                  <Text type="secondary" style={{ marginLeft: 4 }}>
                    hours
                  </Text>
                </div>
              </Col>

              <Col>
                <div style={{ display: "flex", alignItems: "center" }}>
                  {getPriorityStars(emp.e_priority)}
                </div>
              </Col>

              <Col>
                <Button
                  shape="circle"
                  icon={<EditOutlined />}
                  onClick={() => handleEdit(emp)}
                  style={{ marginRight: "20px" }}
                />
                <Button
                  danger
                  shape="circle"
                  icon={<DeleteOutlined />}
                  onClick={() => handleDelete(emp.e_id)}
                  style={{
                    boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
                  }}
                />
              </Col>
            </Row>
          </Card>
        ))
      )}

      {/* Edit Employee Modal */}
      <Modal
        title="Edit Employee"
        open={isModalVisible}
        onCancel={() => setIsModalVisible(false)}
        onOk={handleUpdate}
        okText="Update"
      >
        <Form form={form} layout="vertical">
          <Form.Item
            label="Employee Name"
            name="e_name"
            rules={[{ required: true, message: "Please enter name" }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Email"
            name="e_gmail"
            rules={[{ required: true, message: "Please enter email" }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Hours Worked"
            name="no_of_hours_worked"
            rules={[{ required: true, message: "Enter hours" }]}
          >
            <Input type="number" />
          </Form.Item>
          <Form.Item
            label="Designation"
            name="designation"
            rules={[{ required: true, message: "Please select designation" }]}
          >
            <Select>
              <Select.Option value="Manager">Manager</Select.Option>
              <Select.Option value="Cleaning Staff">Cleaning Staff</Select.Option>
              <Select.Option value="Inventory Manager">Inventory Manager</Select.Option>
              <Select.Option value="Supervisor">Supervisor</Select.Option>
              <Select.Option value="Cashier">Cashier</Select.Option>
              <Select.Option value="Customer Help">Customer Help</Select.Option>
            </Select>
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default EmployeeView;
