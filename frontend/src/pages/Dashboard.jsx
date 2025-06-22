// frontend/src/pages/Dashboard.jsx
import { useState, useEffect } from 'react';
import axios from 'axios';

const API = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

function Dashboard() {
  const [subnet, setSubnet] = useState('192.168.1.0/24');
  const [taskId, setTaskId] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [scanLoading, setScanLoading] = useState(false);
  const token = localStorage.getItem('token');

  const handleScan = async () => {
    setScanLoading(true);
    try {
      console.log('Starting scan for subnet:', subnet);
      const res = await axios.post(`${API}/api/trigger-scan/`, 
        { subnet }, 
        {
          headers: { 
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json'
          }
        }
      );
      console.log('Scan response:', res.data);
      setTaskId(res.data.task_id);
      alert(`Scan started! Task ID: ${res.data.task_id}`);
      
      // Refresh results after a short delay
      setTimeout(() => {
        fetchResults();
      }, 2000);
      
    } catch (err) {
      console.error('Scan error:', err.response?.data || err.message);
      if (err.response?.status === 403) {
        alert('Access denied. You need admin privileges to run scans.');
      } else {
        alert(`Scan failed: ${err.response?.data?.error || err.message}`);
      }
    } finally {
      setScanLoading(false);
    }
  };

  const fetchResults = async () => {
    setLoading(true);
    try {
      console.log('Fetching scan results...');
      const res = await axios.get(`${API}/api/scan-results/`, {
        headers: { 
          Authorization: `Token ${token}`,
          'Content-Type': 'application/json'
        }
      });
      console.log('Results:', res.data);
      setResults(res.data);
    } catch (error) {
      console.error('Fetch results error:', error.response?.data || error.message);
      alert(`Failed to fetch results: ${error.response?.data?.detail || error.message}`);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchResults();
  }, []);

  return (
    <div>
      <h2>Network Scanner</h2>
      <div className="input-group mb-3">
        <input 
          className="form-control" 
          value={subnet} 
          onChange={e => setSubnet(e.target.value)}
          placeholder="Enter subnet (e.g., 192.168.1.0/24)"
        />
        <button 
          className="btn btn-primary" 
          onClick={handleScan}
          disabled={scanLoading}
        >
          {scanLoading ? 'Scanning...' : 'Start Scan'}
        </button>
      </div>
      
      {taskId && (
        <div className="alert alert-info">
          Current Task ID: {taskId}
        </div>
      )}
      
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Previous Scan Results</h4>
        <button 
          className="btn btn-secondary btn-sm" 
          onClick={fetchResults}
          disabled={loading}
        >
          {loading ? 'Loading...' : 'Refresh'}
        </button>
      </div>
      
      {loading && <div className="text-center">Loading results...</div>}
      
      {results.length === 0 && !loading ? (
        <div className="alert alert-info">No scan results found.</div>
      ) : (
        <ul className="list-group">
          {results.map((scan, index) => (
            <li key={index} className="list-group-item">
              <div className="d-flex justify-content-between align-items-start">
                <div>
                  <strong>Subnet: {scan.subnet}</strong>
                  <small className="text-muted d-block">
                    {new Date(scan.timestamp).toLocaleString()}
                  </small>
                </div>
                <span className="badge bg-primary">
                  {scan.results?.length || 0} hosts
                </span>
              </div>
              
              {scan.results && scan.results.length > 0 ? (
                <ul className="mt-2">
                  {scan.results.map((host, i) => (
                    <li key={i} className="mb-1">
                      <strong>{host.ip}</strong>
                      {host.hostname && ` (${host.hostname})`}
                      <span className={`badge ms-2 ${host.state === 'up' ? 'bg-success' : 'bg-warning'}`}>
                        {host.state}
                      </span>
                    </li>
                  ))}
                </ul>
              ) : (
                <div className="text-muted mt-2">No hosts found in this scan.</div>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Dashboard;