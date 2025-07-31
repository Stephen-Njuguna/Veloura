import React from 'react'
import './Navbar.css'
import logo from '../Assets/images.jpg'
import cart from '../Assets/cart_icon.png'
import { useState } from 'react'
import { Link } from 'react-router-dom';


const Navbar = () => {

    const [menu, setMenu] = useState("shop")

  return (
    <div className='navbar'>
      <div className="nav-logo">
      <Link to='/' style={{ textDecoration: 'none'}}>
          <img src={logo} alt="Valoure Shop logo" style={{ cursor: 'pointer' }} />
        <p>Valoure Shop</p>
        </Link> 
      </div>
      <ul className='nav-menu'>
        <li onClick={() => setMenu('shop')}> <Link to='/' style={{ textDecoration: 'none'}}> Shop </Link> {menu === "shop" ? <hr /> : null}</li>
        <li onClick={() => setMenu('men')}> <Link to='/men' style={{ textDecoration: 'none'}}> Men </Link> {menu === "men" ? <hr /> : null}</li>
        <li onClick={() => setMenu('women')}> <Link to='/women' style={{ textDecoration: 'none' }}>Women</Link> {menu === "women" ? <hr /> : null}</li>
        <li onClick={() => setMenu('kids')}> <Link to='/kids' style={{ textDecoration: 'none' }}>Kids</Link> {menu === "kids" ? <hr /> : null}</li>
      </ul>
      <div className="nav-login-cart">
        <button> <Link to='/login' style={{ textDecoration: 'none'}}>Login </Link></button> 
         <Link to='/cart'> <img src={cart} alt="cart" /> </Link>   
        <div className="nav-cart-count">0</div>

      </div>
    </div>
  )
}

export default Navbar
