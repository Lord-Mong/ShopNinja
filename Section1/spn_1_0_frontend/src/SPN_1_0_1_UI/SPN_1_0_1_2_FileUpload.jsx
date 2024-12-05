// ===========================
// SPN_1_0_1_2_FileUpload
// Section: Core Setup
// Component: FrontEnd
// Module: UI Components
// Unit: File Upload
// Purpose: Provide a UI for uploading CSV files and selecting spreadsheet type.
// Input: CSV file and type selection.
// Output: File data sent to API for processing.
// ===========================

import React from 'react';

export default function FileUpload({ onUpload }) {
    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            onUpload(file);
        }
    };

    return (
        <div>
            <label htmlFor="file-upload">Upload CSV File</label>
            <input id="file-upload" type="file" accept=".csv" onChange={handleFileChange} />
        </div>
    );
}
