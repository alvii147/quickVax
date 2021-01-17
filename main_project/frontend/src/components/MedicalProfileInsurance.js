import React from 'react'
import Checkbox from '@material-ui/core/Checkbox';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import '../App.css'

const header = {
    fontFamily: 'RubikOne',
    color: 'black',
    textAlign: 'center'
}

const header2 = {
    fontFamily: 'RubikOne',
    color: 'black',
    fontSize: 30,
    marginTop: 55
}

const header3 = {
    fontFamily: 'RubikOne',
    color: 'black',
    fontSize: 20
}

const checkboxText = {
    fontSize: 20,
    color: 'black',
    marginTop: 7
}

const subscriptText = {
    fontSize: 14,
    fontFamily: 'RubikOne',
    color: 'black',
    marginTop: 70
}


export default function MedicalProfileInsurance() {

    const [checked, setChecked] = React.useState(true);

    // const handleChange = (event) => {
    //     setChecked(event.target.checked);
    // };

    return (
        <div>
            <h1 style={header}>Medical Profile</h1>
            <Grid container spacing={8}>
                <Grid key={0} item>
                    <Grid container justify="left" spacing={2}>
                        <Grid key={0} item>
                            <p style={header2}>Sex</p>
                        </Grid>
                        <Grid key={1} item>
                            <p style={subscriptText}>(gender assigned at birth)</p>
                        </Grid>
                    </Grid>
                    <Grid item xs={12}>
                        <Grid container>
                            <Grid key={0} item>
                                <Checkbox
                                    defaultChecked
                                    color="primary"
                                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                                />
                            </Grid>
                            <Grid key={1} item>
                                <p style={checkboxText}>Female</p>
                            </Grid>
                        </Grid>
                        <Grid container>
                            <Grid key={0} item>
                                <Checkbox
                                    defaultChecked
                                    color="primary"
                                    inputProps={{ 'aria-label': 'secondary checkbox' }}
                                />
                            </Grid>
                            <Grid key={1} item>
                                <p style={checkboxText}>Male</p>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>

                <Grid key={1} item>
                    <Grid container justify="left">
                        <div style={header2}>Race</div>
                        <Grid container spacing={3}>
                            <Grid key={0} item>
                                <Grid container justify="left">
                                    <Grid key={0} item>
                                        <Checkbox
                                            defaultChecked
                                            color="primary"
                                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                                        />
                                    </Grid>
                                    <Grid key={1} item>
                                        <p style={checkboxText}>Asian</p>
                                    </Grid>
                                </Grid>
                                <Grid container justify="left">
                                    <Grid key={0} item>
                                        <Checkbox
                                            defaultChecked
                                            color="primary"
                                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                                        />
                                    </Grid>
                                    <Grid key={1} item>
                                        <p style={checkboxText}>Black/African American</p>
                                    </Grid>
                                </Grid>
                                <Grid container justify="left">
                                    <Grid key={0} item>
                                        <Checkbox
                                            defaultChecked
                                            color="primary"
                                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                                        />
                                    </Grid>
                                    <Grid key={1} item>
                                        <p style={checkboxText}>Pacific Islanders</p>
                                    </Grid>
                                </Grid>
                            </Grid>
                            <Grid key={1} item>
                                <Grid container justify="left">
                                    <Grid key={0} item>
                                        <Checkbox
                                            defaultChecked
                                            color="primary"
                                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                                        />
                                    </Grid>
                                    <Grid key={1} item>
                                        <p style={checkboxText}>White</p>
                                    </Grid>
                                </Grid>
                                <Grid container justify="left">
                                    <Grid key={0} item>
                                        <Checkbox
                                            defaultChecked
                                            color="primary"
                                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                                        />
                                    </Grid>
                                    <Grid key={1} item>
                                        <p style={checkboxText}>Hispanic</p>
                                    </Grid>
                                </Grid>
                                <Grid container justify="left">
                                    <Grid key={0} item>
                                        <Checkbox
                                            defaultChecked
                                            color="primary"
                                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                                        />
                                    </Grid>
                                    <Grid key={1} item>
                                        <p style={checkboxText}>First Nations</p>
                                    </Grid>
                                </Grid>
                            </Grid>
                            <Grid key={2} item>
                                <Grid container justify="left" spacing={2}>
                                    <Grid key={0} item>
                                        <p style={checkboxText}>Other:</p>
                                    </Grid>
                                    <Grid key={1} item>
                                        <TextField
                                            id="standard-helperText"
                                            size="small"
                                        />
                                    </Grid>
                                </Grid>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>

            </Grid>
        </div>
    );
}
