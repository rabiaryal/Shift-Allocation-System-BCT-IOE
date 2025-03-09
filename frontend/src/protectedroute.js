import { Navigate } from "react-router-dom";

const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem("authToken"); // Or use another method to check auth

  return token ? children : <Navigate to="/login" />;
};

export default ProtectedRoute;
