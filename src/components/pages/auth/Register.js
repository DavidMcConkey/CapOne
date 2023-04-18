import React, { Component, useState } from "react";
import httpClient from "../../httpClient";
import Button from "@mui/material/Button";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [restID, setRestID] = useState("");

  const registerUser = async () => {
    console.log(email, password, restID);

    try {
      const resp = await httpClient.post("/register", {
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
      <h3>Create an account!</h3>
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
          onClick={(e) => registerUser()}
          variant="contained"
          className="btn btn-primary mt-2"
        >
          Create Account!
        </Button>
      </form>
    </div>
  );
};

export default Register;
