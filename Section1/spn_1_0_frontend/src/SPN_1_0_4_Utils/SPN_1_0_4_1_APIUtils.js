// ===========================
// SPN_1_0_4_1_APIUtils
// Section: Core Setup
// Component: FrontEnd
// Module: Utils
// Unit: API Utilities
// Purpose: Helper functions for interacting with the Flask back-end API.
// Input: API endpoint and request payload.
// Output: API response data.
// ===========================

import axios from 'axios';

export const uploadCSV = async (file, type) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('type', type);

    return axios.post('/api/upload_csv', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
    });
};
