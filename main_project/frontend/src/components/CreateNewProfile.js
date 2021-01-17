import React from 'react'
import "./CreateNewProfile.css"
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import newProfileBackground from '../images/newProfileBackground.svg';

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
    // backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
}

export default function CreateNewProfile() {

    return (
        <section style={sectionStyle}>
            <div>
                <Grid container justify="center" spacing={8} style={{ paddingTop: '500px' }}>
                    <Grid key={0} item>
                        <Button style={left}>
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
