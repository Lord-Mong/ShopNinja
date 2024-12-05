// ===========================
// SPN_1_0_2_1_Index
// Section: Core Setup
// Component: FrontEnd
// Module: Pages
// Unit: Main Entry Point
// Purpose: Render the Import/Export Page with ThemeProvider.
// Input: None
// Output: Styled application rendering.
// ===========================
import React from 'react';
import ReactDOM from 'react-dom';
import ImportExport from './SPN_1_0_2_Pages/SPN_1_0_2_1_ImportExport';
import { ThemeProvider, createTheme } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        primary: { main: '#1976d2' },
        secondary: { main: '#424242' },
    },
    typography: {
        fontFamily: 'Arial, sans-serif',
    },
});

ReactDOM.render(
    <React.StrictMode>
        <ThemeProvider theme={theme}>
            <ImportExport />
        </ThemeProvider>
    </React.StrictMode>,
    document.getElementById('root')
);
