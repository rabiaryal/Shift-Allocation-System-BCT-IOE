import React, { useState } from "react";
import { Card, Form, Input, TimePicker, Row, Col, Typography, InputNumber, Button } from "antd";
import { ClockCircleOutlined, UserAddOutlined, ScheduleOutlined, SaveOutlined } from "@ant-design/icons";
import moment from "moment";

const { Title } = Typography;

const ShiftConfiguration = () => {
    const [shifts, setShifts] = useState([]);

    const handleShiftCountChange = (count) => {
        const newShifts = Array.from({ length: count }, (_, index) => ({
            name: `Shift #${index + 1}`,
            time: [moment("09:00", "HH:mm"), moment("17:00", "HH:mm")]
        }));
        setShifts(newShifts);
    };

    const handleShiftDetailChange = (index, field, value) => {
        const updatedShifts = [...shifts];
        updatedShifts[index][field] = value;
        setShifts(updatedShifts);
    };

    const saveShifts = () => {
        // You can call your API here to save the shifts
        console.log("Shifts to save:", shifts);
    };

    return (
        <>
            <Title level={3} style={{ marginBottom: 16 }}>
                <ClockCircleOutlined style={{ marginRight: 8, color: "#1890ff" }} /> Shift Configurations
            </Title>

            <Row gutter={24} style={{ marginBottom: 24 }}>
                <Col span={8}>
                    <Form.Item label="Number of Shifts Per Day">
                        <InputNumber
                            min={1}
                            max={5}
                            onChange={handleShiftCountChange}
                            style={{ width: "100%" }}
                            placeholder="Enter shift count"
                            prefix={<ScheduleOutlined style={{ color: "rgba(0,0,0,.25)" }} />}
                        />
                    </Form.Item>
                </Col>
            </Row>

            {shifts.map((shift, index) => (
                <Card
                    key={index}
                    style={{ marginBottom: 24, borderRadius: 8 }}
                    title={`Shift #${index + 1}`}
                    extra={<ClockCircleOutlined style={{ color: "#1890ff" }} />}
                >
                    <Row gutter={24}>
                        <Col span={12}>
                            <Form.Item label="Shift Name">
                                <Input
                                    placeholder="e.g., Morning Shift"
                                    onChange={(e) => handleShiftDetailChange(index, "name", e.target.value)}
                                    value={shift.name}
                                    prefix={<UserAddOutlined style={{ color: "rgba(0,0,0,.25)" }} />}
                                />
                            </Form.Item>
                        </Col>
                        <Col span={12}>
                            <Form.Item label="Shift Timing">
                                <TimePicker.RangePicker
                                    format="HH:mm"
                                    onChange={(time) => handleShiftDetailChange(index, "time", time)}
                                    value={shift.time}
                                    style={{ width: "100%" }}
                                />
                            </Form.Item>
                        </Col>
                    </Row>
                </Card>
            ))}

            {shifts.length > 0 && (
                <Button type="primary" icon={<SaveOutlined />} onClick={saveShifts}>
                    Save Shifts
                </Button>
            )}
        </>
    );
};

export default ShiftConfiguration;
