import { BrowserRouter } from 'react-router';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import React from 'react'
import ReactDOM from 'react-dom/client'

import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
            <BrowserRouter>
                <ThemeProvider theme={createTheme()}>
                    <App />
                </ThemeProvider>
            </BrowserRouter>
    </React.StrictMode>,
)
