// ===========================
// SPN_1_0_1_1_Table
// Section: Core Setup
// Component: FrontEnd
// Module: UI Components
// Unit: Table
// Purpose: Display tabular data with sorting and filtering capabilities.
// Input: Data to display and column configurations.
// Output: Rendered table displaying provided data.
// ===========================

import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

export default function CustomTable({ columns, data }) {
    return (
        <TableContainer component={Paper}>
            <Table>
                <TableHead>
                    <TableRow>
                        {columns.map((col) => (
                            <TableCell key={col.field}>{col.headerName}</TableCell>
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {data.map((row, index) => (
                        <TableRow key={index}>
                            {columns.map((col) => (
                                <TableCell key={col.field}>{row[col.field]}</TableCell>
                            ))}
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}
