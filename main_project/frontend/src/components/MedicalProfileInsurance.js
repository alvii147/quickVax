import React from 'react'
import Checkbox from '@material-ui/core/Checkbox';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import FormLabel from '@material-ui/core/FormLabel';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import RadioGroup from '@material-ui/core/RadioGroup';
import Radio from '@material-ui/core/Radio';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        height: 140,
        width: 100,
    },
    control: {
        padding: theme.spacing(2),
    },
}));

export default function MedicalProfileInsurance() {

    const [checked, setChecked] = React.useState(true);

    // const handleChange = (event) => {
    //     setChecked(event.target.checked);
    // };

    const [spacing, setSpacing] = React.useState(2);
    const classes = useStyles();

    // const handleChange = (event) => {
    //     setSpacing(Number(event.target.value));
    // };

    return (
        <div>
            <h1 style={{ color: 'white' }}>easter egg</h1>
            <h1 style={{ color: 'white' }}>easter egg 2 :))</h1>
            <h1 style={{ color: 'Black' }}>Medical Profile</h1>
            <h2>Sex (gender assigned at birth)</h2>
            <Grid item xs={12}>
                <Grid container justify="left" spacing={spacing}>
                    <Grid key={0} item>
                        <Checkbox
                            defaultChecked
                            color="primary"
                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                        />
                    </Grid>
                    <Grid key={1} item>
                        Female
                    </Grid>
                </Grid>
                <Grid container justify="left" spacing={spacing}>
                    <Grid key={0} item>
                        <Checkbox
                            defaultChecked
                            color="primary"
                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                        />
                    </Grid>
                    <Grid key={1} item>
                        Male
                    </Grid>
                </Grid>
            </Grid>
            <Checkbox
                defaultChecked
                color="primary"
                inputProps={{ 'aria-label': 'secondary checkbox' }}
            />
        </div>
    );
}
