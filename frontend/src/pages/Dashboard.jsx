import { useState } from 'react';
import axios from 'axios';

function Dashboard() {
  const [subnet, setSubnet] = useState('192.168.1.0/24');
  const [taskId, setTaskId] = useState('');
  const [loading, setLoading] = useState(false);

  const handleScan = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('token');
      const res = await axios.post('http://localhost:8000/api/trigger-scan/', { subnet }, {
        headers: {
          Authorization: `Token ${token}`
        }
      });
      setTaskId(res.data.task_id);
    } catch (err) {
      alert('Scan failed. Are you an admin?');
    }
    setLoading(false);
  };

  return (
    <div>
      <h2>Network Scanner</h2>
      <div className="input-group mb-3">
        <input className="form-control" value={subnet} onChange={e => setSubnet(e.target.value)} />
        <button className="btn btn-primary" onClick={handleScan}>
          {loading ? "Scanning..." : "Start Scan"}
        </button>
      </div>
      {taskId && <p>Scan task started with ID: <strong>{taskId}</strong></p>}
    </div>
  );
}

export default Dashboard;
