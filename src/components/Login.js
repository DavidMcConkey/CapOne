import React, { Component, useState, useEffect } from "react";
import Form from "./LoginForm";
export default class Login extends Component {
  render() {
    // const [user, setUser] = (useState < User) | (null > null);

    // useEffect(() => {
    //   (async () => {
    //     try {
    //       const resp = await httpClient.get("//localhost:5000/@me");
    //       setUser(resp.data);
    //     } catch (e) {
    //       console.log("Not authenticated!");
    //     }
    //   })();
    // });
    return (
      <div>
        <Form></Form>
      </div>
    );
  }
}
