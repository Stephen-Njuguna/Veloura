import React from 'react';
import Layout from './components/Navbar/Layout';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Store from './pages/Store';
import Product from './pages/Product';
import VendorProducts from './pages/VendorProducts';
import Cart from './pages/Cart';
import LoginSignup from './pages/LoginSignup';
import shop from './pages/shop';
import ShopCategory from './pages/ShopCategory';

function App() {
  return (
    <div className="container">
      <div>
      <BrowserRouter>
  <Routes>
    <Route element={<Layout />}>
    <Route path="/" element={<shop/>} />
    <Route path="/men" element={<ShopCategory category='men' />} />
    <Route path="/women" element={<ShopCategory category='women' />} />
    <Route path="/kids" element={<ShopCategory category='kids' />} />
    <Route path="/store" element={<Store />} />
    <Route path="/product/:id" element={<Product />} />
    <Route path="/store/:slug/products" element={<VendorProducts />} />
    <Route path="/cart" element={<Cart />} />
    <Route path="/login" element={<LoginSignup />} />
  </Route>
</Routes>
      </BrowserRouter>
      </div>
    </div>
  );
}


export default App;
