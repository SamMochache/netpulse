import { Link, useNavigate } from 'react-router-dom';

function NavBar() {
  const token = localStorage.getItem('token');
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <nav className="navbar navbar-dark bg-dark px-3">
      <Link className="navbar-brand" to="/">NetPulse</Link>
      {token && <button className="btn btn-outline-light" onClick={handleLogout}>Logout</button>}
    </nav>
  );
}

export default NavBar;
