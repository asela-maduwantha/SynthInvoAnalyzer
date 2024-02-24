import React from "react";
import "../Header/header.css";
import Logo from "../../assets/logo.svg";

const Header = () => {
  return (
    <div class="header">
      <div class="header-box">
        <div class="logo">
          <img src={Logo} alt="Logo not available"></img>
        </div>
        <div class="header-btns">
          <button type="button" class="login-btn">
            Login
          </button>
          <button type="button" class="signup-btn">
            Signup
          </button>
        </div>
      </div>
    </div>
  );
};

export default Header;
