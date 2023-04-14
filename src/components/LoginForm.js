import React, { Component, useState } from "react";
import APIService from "./APIService";
import Button from "@mui/material/Button";
import "./styles/SignUp.css";
const Form = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [restID, setRestID] = useState("");

  const insertArticle = () => {
    APIService.InsertArticle({ username, password, restID })
      .then((response) => props.insertedArticle(response))
      .catch((error) => console.log("error", error));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    insertArticle();
    setUsername("");
    setPassword("");
    setRestID("");
  };

  return (
    <div className="login-form">
      <form onSubmit={handleSubmit}>
        <label htmlFor="" className="form-label"></label>
        <input
          type="text"
          className="form-control"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
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
        <Button variant="contained" className="btn btn-primary mt-2">
          Sign In
        </Button>
      </form>
    </div>
  );
};

export default Form;
