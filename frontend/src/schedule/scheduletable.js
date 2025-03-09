import React, { useEffect, useState } from "react";
import { Table, Input, Space, Button,Tag } from "antd";

// Define the light colors based on designation
const designationColors = {
  Cashier: "#ffe6cc", // Light Orange
  "Inventory Manager": "#e6ffe6", // Light Green
  Manager: "#cce6ff", // Light Blue
  "Customer Help": "#ffd9e6", // Light Pink
  "Cleaning Staff": "#e6e6ff", // Light Purple
  Supervisor: "#f2f2f2", // Light Gray
};


// const timeOfDayColors = {
//   Morning: "orange", // Color for Morning
//   Day: "blue",       // Color for Day
//   Evening: "purple", // Color for Evening
//   Night: "green",    // Color for Night
//   // Add more shifts or customize colors as needed
// };


// Reusable render function to handle shift-based color rendering with black text color
// Reusable render function to handle shift-based color rendering with black text color and dark background colors
const renderShiftTags = (shifts) => {
  return (
    <>
      {shifts &&
        shifts.map((shift) => {
          // Darker background colors for each shift
          let bgColor = "";
          switch (shift) {
            case "Morning":
              bgColor = "#D97706"; // Dark Orange
              break;
            case "Day":
              bgColor = "#B38E00"; // Dark Blue
              break;
            case "Evening":
              bgColor = "#6B21A8"; // Dark Purple
              break;
            case "Night":
              bgColor = "#065F46"; // Dark Green
              break;
            default:
              bgColor = "#000000"; // Default dark gray if not recognized
          }
          
          return (
            <Tag color={bgColor} key={shift} style={{ color: "white" }}> {/* Set text color to black */}
              {shift.toUpperCase()}
            </Tag>
          );
        })}
    </>
  );
};


const ScheduleTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState(""); // State for search input
  const [searchedData, setSearchedData] = useState(null); // State to store searched employee data

  useEffect(() => {
    fetch("http://127.0.0.1:8000/get-excel/") // Update with your API URL
      .then((response) => response.json())
      .then((result) => {
        
        const processedData = processEmployeeData(result.data);
        
        // Set the processed data into state
        setData(processedData);
        
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setLoading(false);
      });
  }, []);

  const processEmployeeData = (data) => {
    return data.map((employee) => {
      // Loop through each Day field (Day1 to Day7)
      for (let i = 1; i <= 7; i++) {
        const dayField = `Day${i}`;
        // Convert the Day field value into an array, trim spaces, and split by commas
        if (employee[dayField]) {
          employee[dayField] = employee[dayField]
            .split(",") // Split by comma
            .map((day) => day.trim()); // Trim spaces from each value
        }
      }
      return employee;
    });
  };
// tempResult = result.trim()
  // Handle search function for employee ID, name, or designation
  const handleSearch = (value) => {
    setSearchTerm(value); // Set the search term to input value
    if (!value) {
      setSearchedData(null); // If empty search term, reset the search result
      return;
    }

    // Filter data by employee ID, name, or designation
    const filteredData = data.filter(
      (item) =>
        item["Employee ID"].toString().includes(value) ||
        item["Employee Name"].toLowerCase().includes(value.toLowerCase()) ||
        item["Designation"].toLowerCase().includes(value.toLowerCase())
    );
    setSearchedData(filteredData);
  };

  // Handle sending email
  const handleSendMail = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/sendmail/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        alert("Mail sent successfully!");
      } else {
        alert("Failed to send mail.");
      }
    } catch (error) {
      console.error("Error sending mail:", error);
      alert("Error sending mail.");
    }
  };

  // Define columns for displaying employee details and schedule
  const columns = [
    { title: "Employee ID", dataIndex: "Employee ID", key: "Employee ID" },
    { title: "Employee Name", dataIndex: "Employee Name", key: "Employee Name" },
    { title: "Designation", dataIndex: "Designation", key: "Designation" },
    { title: "Working Hours", dataIndex: "Working Hours", key: "Working Hours" },
    { title: "Day1", dataIndex: "Day1", key: "Day1",render:  (Day1) => renderShiftTags(Day1),},
    { title: "Day2", dataIndex: "Day2", key: "Day2",render:  (Day2) => renderShiftTags(Day2),},
    { title: "Day3", dataIndex: "Day3", key: "Day3",render:  (Day3) => renderShiftTags(Day3), },
    { title: "Day4", dataIndex: "Day4", key: "Day4",render:  (Day4) => renderShiftTags(Day4), },
    { title: "Day5", dataIndex: "Day5", key: "Day5",render:  (Day5) => renderShiftTags(Day5),},
    { title: "Day6", dataIndex: "Day6", key: "Day6",render:  (Day6) => renderShiftTags(Day6), },
    { title: "Day7", dataIndex: "Day7", key: "Day7",render:  (Day7) => renderShiftTags(Day7), },
  ];


  
  // Define row class for styling based on designation
  const rowClassName = (record) => {
    const designation = record["Designation"];
    return designation && designationColors[designation]
      ? `custom-row-${designation.replace(/\s+/g, "-")}`
      : "";
  };

  return (
    <div style={{ padding: "20px" }}>
      <Space style={{ marginBottom: 16 }}>
        <Input
          placeholder="Search by Employee ID, Name, or Designation"
          value={searchTerm}
          onChange={(e) => handleSearch(e.target.value)} // Trigger search on input change
          style={{ width: "200px" }}
        />
      </Space>

      <Button
        type="primary"
        onClick={handleSendMail}
        style={{
          marginBottom: "16px",
          float: "right",
          padding: "12px 20px",
          fontSize: "16px",
          width: "15%",
          height: 50, // Reduced height
          fontSize: "1.1rem",
          borderRadius: 12,
          background: "linear-gradient(135deg, #36D1DC 0%, #5B86E5 100%)",
          border: "none",
          boxShadow: "0 4px 6px rgba(54, 209, 220, 0.3)",
          transition: "all 0.3s",
          padding: "0 25px",
        }}
      >
        Send Mail
      </Button>

      {/* Show searched data if available */}
      {searchedData && searchedData.length > 0 ? (
        <Table
          dataSource={searchedData} // Use filtered data
          columns={columns}
          rowKey="Employee ID"
          loading={loading}
          bordered
          rowClassName={rowClassName} // Assign class dynamically
          style={{ backgroundColor: "#ffffff" }}
        />
      ) : (
        <Table
          dataSource={data}
          columns={columns}
          rowKey="Employee ID"
          loading={loading}
          bordered
          rowClassName={rowClassName} // Assign class dynamically
          style={{ backgroundColor: "#ffffff" }}
        />
      )}

      {/* Inject styles dynamically */}
      <style>
        {Object.entries(designationColors)
          .map(
            ([designation, color]) =>
              `.custom-row-${designation.replace(/\s+/g, "-")} td { background-color: ${color} !important; }`
          )
          .join("\n")}
      </style>
    </div>
  );
};

export default ScheduleTable;
