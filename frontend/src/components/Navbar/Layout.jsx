import React from 'react'
import Navbar from './Navbar';
import { Outlet, useLocation } from 'react-router-dom';

const Layout = () => {
  const location = useLocation();
  const hideNavBarPaths = ['/login', '/signup']; // add any routes where NavBar shouldn't appear
  const shouldHideNavBar = hideNavBarPaths.includes(location.pathname);

  return (
    <>
      {!shouldHideNavBar && <Navbar />}
      <main>
        <Outlet />
      </main>
    </>
  );
};

export default Layout;
