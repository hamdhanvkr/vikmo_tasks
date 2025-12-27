import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Orders() {
  const [orders, setOrders] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    let mounted = true
    async function fetchOrders() {
      setLoading(true)
      setError(null)
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/orders/')
        if (mounted) setOrders(res.data || [])
      } catch (err) {
        if (mounted) setError(err.message || 'Failed to load orders')
      } finally {
        if (mounted) setLoading(false)
      }
    }

    fetchOrders()
    return () => {
      mounted = false
    }
  }, [])

  return (
    <div>
      <h2>Orders</h2>

      {loading && <p>Loading orders...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}

      {!loading && !error && (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>ID</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Order #</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Status</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Total</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Dealer</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Items</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Created</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Updated</th>
            </tr>
          </thead>
          <tbody>
            {orders.map((o) => (
              <tr key={o.id}>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{o.id}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{o.order_number}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{o.status}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{o.total_amount}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{o.dealer}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{Array.isArray(o.items) ? o.items.length : 0}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{o.created_at}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{o.updated_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}
