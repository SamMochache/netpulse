// frontend/src/App.jsx
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import NavBar from './components/NavBar';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));

  // Listen for storage changes to update token state
  useEffect(() => {
    const handleStorageChange = () => {
      setToken(localStorage.getItem('token'));
    };

    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, []);

  // Update token state when localStorage changes within the same tab
  useEffect(() => {
    const checkToken = () => {
      const currentToken = localStorage.getItem('token');
      if (currentToken !== token) {
        setToken(currentToken);
      }
    };

    const interval = setInterval(checkToken, 1000);
    return () => clearInterval(interval);
  }, [token]);

  return (
    <Router>
      <NavBar token={token} setToken={setToken} />
      <div className="container mt-4">
        <Routes>
          <Route path="/login" element={token ? <Navigate to="/" /> : <Login />} />
          <Route path="/" element={token ? <Dashboard /> : <Navigate to="/login" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;