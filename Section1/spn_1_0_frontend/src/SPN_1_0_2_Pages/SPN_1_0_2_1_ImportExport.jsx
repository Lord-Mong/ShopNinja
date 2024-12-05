// ===========================
// SPN_1_0_2_1_ImportExport
// Section: Core Setup
// Component: FrontEnd
// Module: Pages
// Unit: Import/Export Page
// Purpose: UI for CSV import/export workflows.
// Input: User actions for file uploads and downloads.
// Output: Display uploaded data in a table and handle export requests.
// ===========================

import React, { useState } from 'react';
import FileUpload from '../SPN_1_0_1_UI/SPN_1_0_1_2_FileUpload';
import Table from '../SPN_1_0_1_UI/SPN_1_0_1_1_Table';
import { saveAs } from 'file-saver';

export default function ImportExport() {
    const [tableData, setTableData] = useState([]);
    const [columns, setColumns] = useState([]);

    try {
        const handleFileUpload = (file) => {
            const reader = new FileReader();

            reader.onload = (event) => {
                const csvContent = event.target.result;
                processCSV(csvContent);
            };

            reader.readAsText(file);
        };

        const processCSV = (csvContent) => {
            const rows = csvContent.split('\n').filter((row) => row.trim() !== '');
            const headers = rows[0].split(',');

            const data = rows.slice(1).map((row) => {
                const values = row.split(',');
                return headers.reduce((acc, header, index) => {
                    acc[header.trim()] = values[index]?.trim() || '';
                    return acc;
                }, {});
            });

            setColumns(headers.map((header) => ({ field: header, headerName: header })));
            setTableData(data);
        };

        const exportCSV = () => {
            const headers = columns.map((col) => col.headerName).join(',');
            const rows = tableData.map((row) =>
                columns.map((col) => row[col.field] || '').join(',')
            );

            const csvContent = [headers, ...rows].join('\n');
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });

            saveAs(blob, 'exported_data.csv');
        };

        return (
            <div>
                <h1>Import/Export CSV</h1>
                <FileUpload onUpload={handleFileUpload} />
                {tableData.length > 0 && (
                    <>
                        <Table data={tableData} columns={columns} />
                        <button onClick={exportCSV}>Export CSV</button>
                    </>
                )}
            </div>
        );
    } catch (error) {
        console.error('Error in ImportExport:', error);
        return <h1>An error occurred. Check the console for details.</h1>;
    }
}
