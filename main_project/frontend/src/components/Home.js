import React from 'react'
import { useHistory } from "react-router-dom"
import "./Home.css"
import backgrd from '../images/backgrd.svg';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';

const top = {
    background: '#3D5A80',
    borderRadius: 10,
    border: 0,
    color: 'white',
    height: 15,
    padding: '30px 53px',
    fontSize: 28,
    fontFamily: "RubikOne",
    textTransform: "capitalize"
};

const bottom = {
    background: '#EE6C4D',
    borderRadius: 10,
    border: 0,
    color: 'white',
    height: 15,
    padding: '30px 130px',
    fontSize: 28,
    fontFamily: "RubikOne",
    textTransform: "capitalize"
};

const topText = {
    fontFamily: "RubikOne",
    textTransform: "capitalize",
    fontSize: 30,
    color: "#3D5A80"
}

const bottomText = {
    fontFamily: "RubikOne",
    textTransform: "capitalize",
    fontSize: 30,
    color: "#EE6C4D"
}

var sectionStyle = {
    height: "850px",
    backgroundImage: "url(" + backgrd + ")",
    backgroundPosition: 'center',
    // backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
}


export default function Home(props) {
    let history = useHistory()

    function handleClick() {
        history.push("/queue")
    }

    function medicalClick() {
        history.push("/medicalProfileInsurance")
    }

    return (
        <section style={sectionStyle}>
            <div>
                <Grid container justify="center" spacing={8} style={{ paddingTop: '500px' }}>
                    <Grid key={0} item>
                        <p style={topText}>Step 1:</p>
                    </Grid>
                    <Grid key={1} item>
                        <Button style={top} onClick={medicalClick}>
                            Complete Medical Profile
                        </Button>
                    </Grid>
                </Grid>
                <Grid container justify="center" spacing={8}>
                    <Grid key={0} item>
                        <p style={bottomText}>Step 2:</p>
                    </Grid>
                    <Grid key={1} item>
                        <Button style={bottom} onClick={handleClick}>
                            Join the Queue
                        </Button>
                    </Grid>
                </Grid>
            </div>

        </section>

    );
}

{/* <div class="center">
            <button onClick={handleClick}>Join the Queue</button>
        </div> */}