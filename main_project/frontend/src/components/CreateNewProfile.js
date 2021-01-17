import React from 'react'
import "./CreateNewProfile.css"
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import { createMuiTheme } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';
import newProfileBackground from '../images/newProfileBackground.svg';
import { withStyles } from '@material-ui/core/styles';

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

const StyledButton = withStyles({
    root: {
        background: '#97DDAB',
        borderRadius: 3,
        border: 0,
        color: 'black',
        height: 60,
        width: 347,
        padding: '300 347px',
    },
    label: {
        textTransform: 'capitalize',
        size: 35
    },
})(Button);

// const theme = createMuiTheme({
//     palette: {
//         primary: {
//             // pale green
//             main: "#97DDAB",
//         },
//         secondary: {
//             // soft purple
//             main: '#AD8DB5',
//         },
//     },
// });

var sectionStyle = {
    height: "850px",
    backgroundImage: "url(" + newProfileBackground + ")",
    backgroundPosition: 'center',
    // backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
}

// const styles = {
//     root: {
//       borderRadius: 3,
//       border: 0,
//       color: 'white',
//       height: 48,
//       padding: '0 30px',
//       boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
//     },
// };

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
