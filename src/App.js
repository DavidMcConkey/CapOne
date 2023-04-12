import "./App.css";
import React, { useState, useEffect } from "react";
import Button from "@mui/material/Button";
function App() {
  // const [data, setData] = useState([{}]);

  // useEffect(() => {
  //   fetch("/home")
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setData(data);
  //       console.log(data);
  //     });
  // }, []);
  return (
    <div>
      <Button variant="contained">Start now!</Button>
    </div>
  );
}

export default App;
