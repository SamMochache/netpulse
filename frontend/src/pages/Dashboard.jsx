import { useState, useEffect } from 'react';
import axios from 'axios';

const API = import.meta.env.VITE_API_BASE_URL;

function Dashboard() {
  const [subnet, setSubnet] = useState('192.168.1.0/24');
  const [taskId, setTaskId] = useState('');
  const [results, setResults] = useState([]);
  const token = localStorage.getItem('token');

  const handleScan = async () => {
    try {
      const res = await axios.post(`${API}/api/trigger-scan/`, { subnet }, {
        headers: { Authorization: `Token ${token}` }
      });
      setTaskId(res.data.task_id);
    } catch (err) {
      alert('Scan failed. Are you an admin?');
    }
  };

  const fetchResults = async () => {
    try {
      const res = await axios.get(`${API}/api/scan-results/`, {
        headers: { Authorization: `Token ${token}` }
      });
      setResults(res.data);
    } catch {
      alert('Failed to fetch results');
    }
  };

  useEffect(() => {
    fetchResults();
  }, [taskId]);

  return (
    <div>
      <h2>Network Scanner</h2>
      <div className="input-group mb-3">
        <input className="form-control" value={subnet} onChange={e => setSubnet(e.target.value)} />
        <button className="btn btn-primary" onClick={handleScan}>Start Scan</button>
      </div>
      <h4>Previous Scan Results</h4>
      <ul className="list-group">
        {results.map((scan, index) => (
          <li key={index} className="list-group-item">
            <strong>{scan.subnet}</strong> @ {new Date(scan.timestamp).toLocaleString()}
            <ul>
              {scan.results.map((host, i) => (
                <li key={i}>
                  {host.ip} ({host.hostname}) - {host.state}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
