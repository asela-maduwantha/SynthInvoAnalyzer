// Navbar.js
import React, { useState } from "react";
import "./navbar.css";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className={`navbar-container ${isOpen ? "open" : ""}`}>
      <div className={`toggle ${isOpen ? "open" : ""}`} onClick={toggleSidebar}>
        <i className="bi bi-list"></i>
      </div>
      <div className="row-element">
        <div className="row-icon">
          <i className="bi bi-grid-fill"></i>
        </div>
        <div className="row-text">{isOpen ? "Dashboard" : ""}</div>
      </div>

      <div class="row-element">
        <div class="row-icon">
          <i class="bi bi-receipt"></i>
        </div>
        <div class="row-text">{isOpen ? "Invoices" : ""}</div>
      </div>
      <div class="row-element">
        <div class="row-icon">
          <i class="bi bi-building-fill-down"></i>
        </div>
        <div class="row-text">{isOpen ? "Suppliers" : ""}</div>
      </div>
      <div class="row-element">
        <div class="row-icon">
          <i class="bi bi-graph-up-arrow"></i>
        </div>
        <div class="row-text">{isOpen ? "Analitics" : ""}</div>
      </div>
      <div class="row-element">
        <div class="row-icon">
          <i class="bi bi-person-fill-gear"></i>
        </div>
        <div class="row-text">{isOpen ? "Account Settings" : ""}</div>
      </div>
      <div class="row-element">
        <div class="row-icon">
          <i class="bi bi-box-arrow-right"></i>
        </div>
        <div class="row-text">{isOpen ? "Logout" : ""}</div>
      </div>
    </div>
  );
};

export default Navbar;
