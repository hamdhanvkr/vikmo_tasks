import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function Products() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    let mounted = true
    async function fetchProducts() {
      setLoading(true)
      setError(null)
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/products/')
        if (mounted) setProducts(res.data || [])
      } catch (err) {
        if (mounted) setError(err.message || 'Failed to load products')
      } finally {
        if (mounted) setLoading(false)
      }
    }

    fetchProducts()
    return () => {
      mounted = false
    }
  }, [])

  return (
    <div>
      <h2>Products</h2>

      {loading && <p>Loading products...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}

      {!loading && !error && (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>ID</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>SKU</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Name</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Price</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Active</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Created</th>
              <th style={{ border: '1px solid #ddd', padding: '8px' }}>Updated</th>
            </tr>
          </thead>
          <tbody>
            {products.map((p) => (
              <tr key={p.id}>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{p.id}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{p.sku}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{p.name}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{p.price}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{p.is_active ? 'Yes' : 'No'}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{p.created_at}</td>
                <td style={{ border: '1px solid #ddd', padding: '8px' }}>{p.updated_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}
