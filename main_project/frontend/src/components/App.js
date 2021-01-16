import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./Home";
import Queue from "./Queue";

export default function App() {
    return (
        <Router>
            <Switch>
                <Route path="/queue">
                    <Queue />
                </Route>
                <Route path="/">
                    <Home />
                </Route>
            </Switch>
        </Router>
    );
}

class Yes extends Component {
    constructor(props) {
        super(props);
        this.state = {
            readAllData: [],
            readData: [],
            postData: {},
            id: ""
        };
        this.handleChange = this.handleChange.bind(this);
        //this.handleSubmit = this.handleSubmit.bind(this);
        this.CreateUserAPI = this.CreateUserAPI.bind(this);
        this.ReadAllUsersAPI = this.ReadAllUsersAPI.bind(this);
        this.ReadUserAPI = this.ReadUserAPI.bind(this);
        this.UpdateUserAPI = this.UpdateUserAPI.bind(this);
        this.DeleteUserAPI = this.DeleteUserAPI.bind(this);
    }

    componentDidMount() {
        //this.ReadAllUsersAPI();
    }

    handleChange(event) {
        const data = this.state.postData;
        if(event.target.name == "id") {
            this.setState({
                id: event.target.value
            })
            return
        }
        
        if(event.target.name == "status") {
            if(event.target.checked) {
                data["status"] = true;
            }
            else {
                data["status"] = false;
            }
        }
        else {
            if(!event.target.name && data.hasOwnProperty(event.target.name)) {
                delete data[event.target.name];
            }
            else {
                data[event.target.name] = event.target.value;
            }
        }
        this.setState({
            postData: data
        });
    }

    /*handleSubmit(event) {
        event.preventDefault();
    }*/

    CreateUserAPI() {
        console.log("Creating...");
        fetch("/api/users/", {
            method: "POST",
            body: JSON.stringify(this.state.postData),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
            if (response.status > 400) {
                console.log("Error in POST request");
            }
            return response.json();
        })
        .then(json => {
            console.log(json);
            this.ReadAllUsersAPI();
        });
    }

    ReadAllUsersAPI() {
        console.log("Reading...");
        fetch("/api/users/")
        .then(response => {
            if (response.status > 400) {
                console.log("Error in GET request");
            }
            return response.json();
        })
        .then(json => {
            console.log(json);
            this.setState({
                readAllData: json
            });
        });
    }

    ReadUserAPI() {
        console.log("Reading Single Entry...");
        fetch("/api/users/" + this.state.id + "/")
        .then(response => {
            if (response.status > 400) {
                console.log("Error in GET request");
            }
            return response.json();
        })
        .then(json => {
            console.log(json);
            this.setState({
                readData: json
            });
        });
    }

    UpdateUserAPI() {
        console.log("Updating...");
        fetch("/api/users/" + this.state.id + "/", {
            method: "PATCH",
            body: JSON.stringify(this.state.postData),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
            if (response.status > 400) {
                console.log("Error in PATCH request");
            }
            return response.json();
        })
        .then(json => {
            console.log(json);
            this.ReadAllUsersAPI();
        });
    }

    DeleteUserAPI() {
        console.log("Deleting...");
        fetch("/api/users/" + this.state.id + "/", {
            method: "DELETE"
        })
        .then(response => {
            console.log(response);
            this.ReadAllUsersAPI();
        });
    }

    render() {
        return (
            <div>
                <h1 className="display-1">Django application</h1>
                <h1 className="display-4">Welcome to the home page!</h1>
            </div>
        );
    }
}


const container = document.getElementById("app");
render(<App />, container);
