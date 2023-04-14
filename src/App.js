import "./App.css";
import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Login from "./components/Login";
import NavbarComp from "./components/NavBarComp";
function App() {
  return (
    <div>
      <NavbarComp></NavbarComp>
      <h2 className="site-title">Placeholder Name</h2>
      <Login></Login>
    </div>
  );
}

export default App;
