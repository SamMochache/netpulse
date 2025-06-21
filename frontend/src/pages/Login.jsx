import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const API = import.meta.env.VITE_API_BASE_URL;

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(`${API}/api-token-auth/`, { username, password });
      localStorage.setItem('token', res.data.token);
     // Log what the backend returns

      navigate('/');
    } catch {
      alert('Login failed');
    }
  };

  return (
    <div className="card p-4">
      <h3>Login</h3>
      <form onSubmit={handleLogin}>
        <div className="mb-3">
          <label>Username</label>
          <input className="form-control" value={username} onChange={e => setUsername(e.target.value)} />
        </div>
        <div className="mb-3">
          <label>Password</label>
          <input type="password" className="form-control" value={password} onChange={e => setPassword(e.target.value)} />
        </div>
        <button className="btn btn-primary" type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
