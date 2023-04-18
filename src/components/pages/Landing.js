import React, { Component } from "react";
import Button from "@mui/material/Button";
import "../styles/SignUp.css";
import RouterComp from "../router";
export default class Landing extends Component {
  render() {
    <RouterComp />;
    return (
      <div className="landing">
        <h2>ScheduleIt</h2>
        <Button
          href="/login"
          variant="contained"
          className="btn btn-primary mt-2"
        >
          Login
        </Button>
        <Button
          href="/register"
          variant="contained"
          className="btn btn-primary mt-2"
        >
          Register
        </Button>
      </div>
    );
  }
}
