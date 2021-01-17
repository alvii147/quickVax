import React from 'react'
import { useHistory } from "react-router-dom"
import "./Home.css"

export default function Home(props) {
    let history = useHistory()

    function handleClick() {
        if (props.isAuth) {
            history.push("/queue")
        } else {
            let url = window.location.href
            window.location.href = url + "accounts/register/patient"
        }
    }

    return (
        <div class="center">
            <button onClick={handleClick}>Join the Queue</button>
        </div>
    );
}
