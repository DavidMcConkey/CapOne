import React, { Component, useState } from "react";
import httpClient from "../../httpClient.js";
import Button from "@mui/material/Button";
import "../../styles/SignUp.css";
const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [restID, setRestID] = useState("");

  const logInUser = async () => {
    console.log(email, password, restID);

    try {
      const resp = await httpClient.post("/login", {
        email,
        password,
        restID,
      });

      window.location.href = "/";
    } catch (e) {
      if (e.response.status === 401) {
        alert("Invalid credentials!");
      }
    }
  };

  return (
    <div className="login-form">
      <form>
        <label htmlFor="" className="form-label"></label>
        <input
          type="email"
          className="form-control"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <label htmlFor="body" className="form-label"></label>
        <input
          type="password"
          className="form-control"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <label htmlFor="body" className="form-label"></label>
        <input
          className="form-control"
          placeholder="Restaurant ID"
          value={restID}
          onChange={(e) => setRestID(e.target.value)}
          required
        />
        <Button
          onClick={(e) => logInUser()}
          variant="contained"
          className="btn btn-primary mt-2"
        >
          Sign In
        </Button>
      </form>
    </div>
  );
};

export default Login;
