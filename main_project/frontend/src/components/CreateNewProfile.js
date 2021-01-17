import React from 'react'
import "./CreateNewProfile.css"
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import newProfileBackground from '../images/newProfileBackground.svg';
import { useHistory } from "react-router-dom";

const left = {
    background: '#97DDAB',
    borderRadius: 10,
    border: 0,
    color: 'black',
    height: 10,
    padding: '30px 130px',
    fontSize: 28,
    fontFamily: "RubikOne",
    textTransform: "capitalize"
};

const right = {
    background: '#AD8DB5',
    borderRadius: 10,
    border: 0,
    color: 'black',
    height: 10,
    padding: '30px 130px',
    fontSize: 28,
    fontFamily: "RubikOne",
    textTransform: "capitalize"
};

var sectionStyle = {
    height: "850px",
    backgroundImage: "url(" + newProfileBackground + ")",
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
}

export default function CreateNewProfile(props) {

    let history = useHistory()

    function handleClick() {
        let url = window.location.href;
        window.location.href = "http://127.0.0.1:8000/accounts/register/patient";
    }

    return (
        <section style={sectionStyle}>
            <div>
                <Grid container justify="center" spacing={8} style={{ paddingTop: '500px' }}>
                    <Grid key={0} item>
                        <Button style={left} onClick={handleClick}>
                            Patient
                        </Button>
                    </Grid>
                    <Grid key={1} item>
                        <Button style={right}>
                            Institution
                        </Button>
                    </Grid>
                </Grid>
            </div>

        </section>
    );
}
