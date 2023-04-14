import React, { Component } from "react";
import {
  Navbar,
  NavDropdown,
  Form,
  FormControl,
  Button,
  Nav,
} from "react-bootstrap";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import BookOffs from "./BookOffs";
import Schedule from "./Schedule";
import Dashboard from "./Dashboard";
import SignUp from "./SignUp";

export default class NavbarComp extends Component {
  render() {
    return (
      <Router>
        <div>
          <Navbar bg="light" variant={"light"} expand="lg">
            <Navbar.Brand href="#">Placeholder!</Navbar.Brand>
            <Navbar.Toggle aria-controls="navbarScroll" />
            <Navbar.Collapse id="navbarScroll">
              <Nav
                className="mr-auto my-2 my-lg-0"
                style={{ maxHeight: "100px" }}
                navbarScroll
              >
                <Nav.Link as={Link} to="/dashboard">
                  Dashboard
                </Nav.Link>
                <Nav.Link as={Link} to="/schedule">
                  Schedule
                </Nav.Link>
                <Nav.Link as={Link} to="/bookoffs">
                  Book-Offs
                </Nav.Link>
                <Nav.Link as={Link} to="/sign-up">
                  Sign-Up
                </Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Navbar>
        </div>
        <div>
          <Routes>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/schedule" element={<Schedule />} />
            <Route path="/bookoffs" element={<BookOffs />} />
            <Route path="/sign-up" element={<SignUp />} />
          </Routes>
        </div>
      </Router>
    );
  }
}
