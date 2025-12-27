import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Dealers() {
  const [dealers, setDealers] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    let mounted = true
    async function fetchDealers() {
      setLoading(true)
      setError(null)
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/dealers/')
        if (mounted) setDealers(res.data || [])
      } catch (err) {
        if (mounted) setError(err.message || 'Failed to load dealers')
      } finally {
        if (mounted) setLoading(false)
      }
    }

    fetchDealers()
    return () => {
      mounted = false
    }
  }, [])

  return (
    <div>
      <h2>Dealers</h2>

      {loading && <p>Loading dealers...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}

      {!loading && !error && (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>ID</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Code</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Name</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Email</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Phone</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Address</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Created</th>
            </tr>
          </thead>
          <tbody>
            {dealers.map((d) => (
              <tr key={d.id}>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{d.id}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{d.dealer_code}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{d.name}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{d.email}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{d.phone}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{d.address}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{d.created_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}
