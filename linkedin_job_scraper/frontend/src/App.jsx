import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const App = () => {
  const [jobs, setJobs] = useState([]);
  const [vizData, setVizData] = useState({});
  const [loading, setLoading] = useState(false);
  const [keywords, setKeywords] = useState('Python Developer');
  const [location, setLocation] = useState('India');

  const fetchViz = async () => {
    try {
      const res = await axios.get('http://localhost:8000/api/viz/');
      setVizData(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleScrape = async () => {
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/api/scrape/', {
        keywords,
        location,
        num_jobs: 10
      });
      setJobs(res.data);
      await fetchViz();
    } catch (err) {
      alert('Error scraping jobs. Make sure the backend is running and you have internet.');
    } finally {
      setLoading(false);
    }
  };

  const chartData = {
    labels: Object.keys(vizData),
    datasets: [
      {
        label: 'Jobs per Company',
        data: Object.values(vizData),
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>LinkedIn Job Scraper Dashboard</h1>
      <div style={{ marginBottom: '20px' }}>
        <input
          value={keywords}
          onChange={(e) => setKeywords(e.target.value)}
          placeholder="Keywords"
          style={{ padding: '8px', marginRight: '10px' }}
        />
        <input
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          placeholder="Location"
          style={{ padding: '8px', marginRight: '10px' }}
        />
        <button
          onClick={handleScrape}
          disabled={loading}
          style={{ padding: '8px 16px', backgroundColor: '#0077b5', color: 'white', border: 'none', cursor: 'pointer' }}
        >
          {loading ? 'Scraping...' : 'Start Scraping'}
        </button>
      </div>

      <div style={{ display: 'flex', gap: '20px' }}>
        <div style={{ flex: 1 }}>
          <h2>Job Listings</h2>
          <div style={{ maxHeight: '500px', overflowY: 'auto', border: '1px solid #ddd', padding: '10px' }}>
            {jobs.length === 0 && <p>No jobs found yet. Try scraping!</p>}
            {jobs.map((job, index) => (
              <div key={index} style={{ borderBottom: '1px solid #eee', paddingBottom: '10px', marginBottom: '10px' }}>
                <h3 style={{ margin: '0 0 5px 0' }}>{job.Title}</h3>
                <p style={{ margin: '0', color: '#666' }}>{job.Company} - {job.Location}</p>
                <small>Posted: {job['Post Date']}</small>
              </div>
            ))}
          </div>
        </div>

        <div style={{ flex: 1 }}>
          <h2>Visualization</h2>
          {Object.keys(vizData).length > 0 ? (
            <Bar data={chartData} options={{ responsive: true, plugins: { legend: { position: 'top' }, title: { display: true, text: 'Job Frequency by Company' } } }} />
          ) : (
            <p>No visualization data available.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;
