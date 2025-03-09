import {
	BrowserRouter as Router,
	Routes,
	Route,
	useLocation,
	Navigate,
	useNavigate 
} from "react-router-dom";
import { useEffect } from "react";
import { Layout } from "antd";
import Login from "./login/login";
import Signup from "./signup/signup";
import Home from "./home/home";
import EmployeeForm from "./form/configemployee";
import ShiftSwap from "./shiftswap/shiftswap";
import Navbar from "./navbar/navbar";
import AddEmployeeRecord from "./add employee/addemplyee";
import ShiftConfiguration from "./form/configshifts";
import ViewEmployee from "./view/viewemployee";
import ProtectedRoute from "./protectedroute";
import ScheduleTable from "./schedule/scheduletable";

const { Content } = Layout;

const AppLayout = () => {
	const location = useLocation();
	const navigate = useNavigate();

	// Hide Navbar on Login and Signup pages
	const hideNavbar =
		location.pathname === "/login" ||
		location.pathname === "/signup";

	useEffect(() => {
		// Prevent back navigation to login/signup after authentication
		if (
			(localStorage.getItem("authToken") && location.pathname === "/login") ||
			(localStorage.getItem("authToken") && location.pathname === "/signup")
		) {
			navigate("/home", { replace: true });
		}

		// Disable back button navigation on login/signup
		const handleBackButton = () => {
			if (location.pathname === "/login" || location.pathname === "/signup") {
				navigate("/login", { replace: true });
			}
		};

		window.addEventListener("popstate", handleBackButton);
		return () => {
			window.removeEventListener("popstate", handleBackButton);
		};
	}, [location, navigate]);

	return (
		<Layout
			style={{
				minHeight: "100vh",
				backgroundColor: "#E0F7FA",
			}}
		>
			{!hideNavbar && <Navbar />}
			<Content
				style={{
					padding: "20px",
					marginTop: hideNavbar ? 0 : 64,
				}}
			>
				<Routes>
					<Route path="/login" element={<Login />} />
					<Route path="/signup" element={<Signup />} />
					<Route path="/" element={<Navigate to="/login" />} />
					<Route path="/home" element={<Home />} />
					<Route path="/employeeform" element={<EmployeeForm />} />
					<Route path="/shiftswap" element={<ShiftSwap />} />
					<Route path="/addemployeerecords" element={<AddEmployeeRecord />} />
					<Route path="/shiftdetails" element={<ShiftConfiguration />} />
					<Route path="/viewemployeedetails" element={<ViewEmployee />} />
					<Route path="/schedule" element={<ScheduleTable />} />
				</Routes>
			</Content>
		</Layout>
	);
};

function App() {
	return (
		<Router>
			<AppLayout />
		</Router>
	);
}

export default App;
