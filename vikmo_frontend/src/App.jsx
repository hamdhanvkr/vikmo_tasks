import { useState } from 'react'
import './App.css'
import Orders from './Pages/orders'
import Products from './Pages/products'
import Dealers from './Pages/dealers'

function App() {
  const [page, setPage] = useState('home')

  function renderPage() {
    switch (page) {
      case 'orders':
        return <Orders />
      case 'products':
        return <Products />
      case 'dealers':
        return <Dealers />
      default:
        return (
          <div>
            <h1>Welcome</h1>
            <p>Select a page using the buttons above.</p>
          </div>
        )
    }
  }

  return (
    <div className="app-container">
      <div className="nav-buttons">
        <button onClick={() => setPage('orders')}>Orders</button>
        <button onClick={() => setPage('products')}>Products</button>
        <button onClick={() => setPage('dealers')}>Dealers</button>
      </div>

      <main className="page-view">{renderPage()}</main>
    </div>
  )
}

export default App
