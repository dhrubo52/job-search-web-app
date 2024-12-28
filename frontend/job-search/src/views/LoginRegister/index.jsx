import { useState } from 'react';
import { Box, Tabs, Tab, Input, InputLabel, Button } from '@mui/material';
import { styled } from '@mui/material/styles';

const Container = styled(Box)({
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    width: '100vw',
    border: '5px solid red',
});

const LoginRegisterContainer = styled(Box)({
    display: 'flex',
    flexDirection: 'column',
    height: '70%',
    minHeight: '300px',
    maxHeight: '700px',
    width: '30%',
    minWidth: '300px',
    maxWidth: '500px',
    border: '2px solid green',
});

const StyledTab = styled(Tab)({
    textTransform: 'none',
    fontSize: '20px',
});

const DetailsContainer = styled(Box)({
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start',
    height: '100%',
    border: '2px solid orange',
    padding: '20px 20px',
});

const StyledInputLabel = styled(InputLabel)((props)=>({
    marginTop: props.marginTop ? props.marginTop : '0',
    fontSize: '16px',
    fontWeight: 'bold',
}));

const StyledInput = styled(Input)(({theme})=>({
    border: `1px solid ${theme.palette.primary.main}`,
    borderRadius: theme.spacing(1),                         // this is 8px
    width: '100%',
    padding: `0 ${theme.spacing(2)}`,                       // this is 16px 
}));

const StyledButton = styled(Button)({
    width: '150px',
    marginTop: '32px',
});

const LoginRegister = () => {
    const [tab, setTab] = useState(0);

    const handleTabChange = (event, value) => {
        setTab(value);
    }

    return (
        <Container>
            <LoginRegisterContainer>
                <Box>
                    <Tabs value={tab} variant='fullWidth' onChange={handleTabChange}>
                        <StyledTab label='Login' />
                        <StyledTab label='Register' />
                    </Tabs>
                </Box>
                <DetailsContainer>
                    <StyledInputLabel>
                        Email:
                    </StyledInputLabel>
                    <StyledInput 
                        disableUnderline
                    />

                    <StyledInputLabel
                        marginTop='16px'
                    >
                        Password:
                    </StyledInputLabel>
                    <StyledInput 
                        type='password'
                        disableUnderline
                    />

                    <StyledButton variant='contained'>
                        Log In
                    </StyledButton>
                </DetailsContainer>
            </LoginRegisterContainer>
        </Container>
    )
}

export default LoginRegister;