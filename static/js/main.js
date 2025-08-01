/**
 * Student Management System - Main JavaScript
 * This file contains custom JavaScript code for the Student Management System
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    initTooltips();
    
    // Initialize DataTables
    initDataTables();
    
    // Initialize any charts present on the page
    initCharts();
    
    // Initialize sidebar toggle functionality
    initSidebarToggle();
    
    // Form validation
    initFormValidation();
    
    // Handle student deletion
    handleStudentDeletion();
    
    // Handle file uploads
    handleFileUploads();
    
    // Initialize dashboard components
    initDashboard();
});

/**
 * Initialize Bootstrap tooltips
 */
function initTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Initialize DataTables for student lists and other tables
 */
function initDataTables() {
    const studentTable = document.getElementById('studentTable');
    if (studentTable) {
        $(studentTable).DataTable({
            language: {
                search: "_INPUT_",
                searchPlaceholder: "Search students...",
            },
            responsive: true,
            pagingType: "simple_numbers",
            // Customize as needed
            columnDefs: [
                { orderable: false, targets: -1 } // Disable sorting on action column (last column)
            ],
            order: [[1, 'asc']], // Default sort by name (column index 1)
            lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]]
        });
    }
    
    // Initialize other tables as needed
    const attendanceTable = document.getElementById('attendanceTable');
    if (attendanceTable) {
        $(attendanceTable).DataTable({
            responsive: true,
            pagingType: "simple_numbers",
            order: [[0, 'desc']] // Default sort by date (newest first)
        });
    }
}

/**
 * Initialize charts using Chart.js
 */
function initCharts() {
    // Initialize attendance chart if it exists
    initAttendanceChart();
    
    // Initialize performance chart if it exists
    initPerformanceChart();
    
    // Initialize dashboard stats chart if it exists
    initDashboardStatsChart();
}

/**
 * Initialize attendance doughnut chart
 */
function initAttendanceChart() {
    const attendanceChart = document.getElementById('attendanceChart');
    if (attendanceChart) {
        const ctx = attendanceChart.getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Present', 'Late', 'Excused', 'Absent'],
                datasets: [{
                    data: [85, 8, 4, 3],
                    backgroundColor: ['#1cc88a', '#f6c23e', '#36b9cc', '#e74a3b'],
                    hoverBackgroundColor: ['#17a673', '#dda20a', '#2c9faf', '#be3c30'],
                    hoverBorderColor: "rgba(234, 236, 244, 1)",
                }],
            },
            options: {
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                cutout: '70%',
            },
        });
    }
}

/**
 * Initialize student performance line chart
 */
function initPerformanceChart() {
    const performanceChart = document.getElementById('performanceChart');
    if (performanceChart) {
        const ctx = performanceChart.getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                datasets: [{
                    label: "Average Score",
                    lineTension: 0.3,
                    backgroundColor: "rgba(78, 115, 223, 0.05)",
                    borderColor: "rgba(78, 115, 223, 1)",
                    pointRadius: 3,
                    pointBackgroundColor: "rgba(78, 115, 223, 1)",
                    pointBorderColor: "rgba(78, 115, 223, 1)",
                    pointHoverRadius: 3,
                    pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
                    pointHoverBorderColor: "rgba(78, 115, 223, 1)",
                    pointHitRadius: 10,
                    pointBorderWidth: 2,
                    data: [86, 82, 88, 75, 90, 85, 92, 88, 85, 92, 90, 95],
                }],
            },
            options: {
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: false,
                        max: 100,
                        min: 50,
                        ticks: {
                            stepSize: 10
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }
}

/**
 * Initialize dashboard stats area chart
 */
function initDashboardStatsChart() {
    const dashboardStatsChart = document.getElementById('dashboardStatsChart');
    if (dashboardStatsChart) {
        const ctx = dashboardStatsChart.getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["Class 9", "Class 10", "Class 11", "Class 12"],
                datasets: [{
                    label: "Students",
                    backgroundColor: "#4e73df",
                    hoverBackgroundColor: "#2e59d9",
                    borderColor: "#4e73df",
                    data: [325, 290, 255, 230],
                }],
            },
            options: {
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }
}

/**
 * Initialize sidebar toggle functionality
 */
function initSidebarToggle() {
    const sidebarToggle = document.getElementById('sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function(e) {
            e.preventDefault();
            document.body.classList.toggle('sidebar-toggled');
            document.querySelector('.sidebar').classList.toggle('toggled');
        });
    }
}

/**
 * Initialize form validation
 */
function initFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        }, false);
    });
    
    // Custom validation for file inputs (size limit, etc.)
    const fileInputs = document.querySelectorAll('input[type="file"]');
    Array.from(fileInputs).forEach(input => {
        input.addEventListener('change', function() {
            validateFileSize(this);
        });
    });
}

/**
 * Validate file size
 */
function validateFileSize(fileInput) {
    const maxSize = 2 * 1024 * 1024; // 2MB
    
    if (fileInput.files.length > 0) {
        const fileSize = fileInput.files[0].size;
        if (fileSize > maxSize) {
            alert('File size exceeds 2MB limit. Please choose a smaller file.');
            fileInput.value = ''; // Clear the input
        }
    }
}

/**
 * Handle student deletion confirmation
 */
function handleStudentDeletion() {
    const deleteButtons = document.querySelectorAll('.delete-student-btn');
    Array.from(deleteButtons).forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this student? This action cannot be undone.')) {
                e.preventDefault();
            }
        });
    });
}

/**
 * Handle file uploads with preview
 */
function handleFileUploads() {
    const profilePictureInput = document.getElementById('id_profile_picture');
    if (profilePictureInput) {
        profilePictureInput.addEventListener('change', function() {
            displayImagePreview(this);
        });
    }
    
    // Handle bulk import preview
    const bulkImportInput = document.getElementById('bulk_import_file');
    if (bulkImportInput) {
        bulkImportInput.addEventListener('change', function() {
            displayFileInfo(this);
        });
    }
}

/**
 * Display image preview after selection
 */
function displayImagePreview(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const previewContainer = document.createElement('div');
            previewContainer.className = 'mt-2 mb-3';
            previewContainer.id = 'image-preview-container';
            
            // Create image element
            const image = document.createElement('img');
            image.src = e.target.result;
            image.className = 'img-thumbnail';
            image.style.height = '100px';
            previewContainer.appendChild(image);
            
            // Remove existing preview if any
            const existingPreview = document.getElementById('image-preview-container');
            if (existingPreview) {
                existingPreview.remove();
            }
            
            // Add new preview
            input.parentNode.insertBefore(previewContainer, input.nextSibling);
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}

/**
 * Display file information after selection
 */
function displayFileInfo(input) {
    if (input.files && input.files[0]) {
        const fileInfo = document.getElementById('file-info');
        if (fileInfo) {
            const fileName = input.files[0].name;
            const fileSize = (input.files[0].size / 1024).toFixed(2) + ' KB';
            fileInfo.innerHTML = `Selected file: <strong>${fileName}</strong> (${fileSize})`;
        }
    }
}

/**
 * Initialize dashboard-specific functionality
 */
function initDashboard() {
    // Update real-time date and time display
    const dateTimeDisplay = document.getElementById('current-datetime');
    if (dateTimeDisplay) {
        updateDateTime(dateTimeDisplay);
        setInterval(function() {
            updateDateTime(dateTimeDisplay);
        }, 60000); // Update every minute
    }
    
    // Initialize dashboard notifications
    initNotifications();
}

/**
 * Update date and time display
 */
function updateDateTime(element) {
    const now = new Date();
    const options = { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    element.textContent = now.toLocaleDateString('en-US', options);
}

/**
 * Initialize notifications system
 */
function initNotifications() {
    // Mark notifications as read
    const notificationItems = document.querySelectorAll('.notification-item');
    notificationItems.forEach(item => {
        item.addEventListener('click', function() {
            this.classList.remove('unread');
            // Update notification count
            updateNotificationCount();
        });
    });
    
    // Mark all notifications as read
    const markAllReadBtn = document.getElementById('mark-all-read');
    if (markAllReadBtn) {
        markAllReadBtn.addEventListener('click', function(e) {
            e.preventDefault();
            notificationItems.forEach(item => {
                item.classList.remove('unread');
            });
            updateNotificationCount();
        });
    }
}

/**
 * Update notification count display
 */
function updateNotificationCount() {
    const unreadCount = document.querySelectorAll('.notification-item.unread').length;
    const countBadge = document.querySelector('.notification-badge');
    
    if (countBadge) {
        if (unreadCount > 0) {
            countBadge.textContent = unreadCount;
            countBadge.classList.remove('d-none');
        } else {
            countBadge.classList.add('d-none');
        }
    }
}

/**
 * Print specific sections of the page
 */
function printSection(elementId) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const originalContent = document.body.innerHTML;
    const printContent = element.innerHTML;
    
    document.body.innerHTML = `
        <div style="padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <h1>Student Management System</h1>
            </div>
            ${printContent}
        </div>
    `;
    
    window.print();
    document.body.innerHTML = originalContent;
    
    // Reinitialize components after restoring content
    document.addEventListener('DOMContentLoaded', function() {
        initTooltips();
        initDataTables();
        initCharts();
    });
}

/**
 * Export table data to Excel
 */
function exportTableToExcel(tableID, filename = '') {
    const table = document.getElementById(tableID);
    if (!table) return;
    
    const wb = XLSX.utils.table_to_book(table, { sheet: "Sheet JS" });
    XLSX.writeFile(wb, filename || 'export.xlsx');
}

/**
 * Export table data to PDF
 */
function exportTableToPDF(tableID, filename = '') {
    const table = document.getElementById(tableID);
    if (!table) return;
    
    const doc = new jsPDF('l', 'pt', 'a4');
    doc.autoTable({ html: `#${tableID}` });
    doc.save(filename || 'export.pdf');
}

/**
 * Export table data to CSV
 */
function exportTableToCSV(tableID, filename = '') {
    const table = document.getElementById(tableID);
    if (!table) return;
    
    const rows = table.querySelectorAll('tr');
    let csv = [];
    
    for (let i = 0; i < rows.length; i++) {
        const row = [], cols = rows[i].querySelectorAll('td, th');
        for (let j = 0; j < cols.length; j++) {
            // Remove HTML and get text content
            let cellText = cols[j].innerText.replace(/(\r\n|\n|\r)/gm, "").replace(/"/g, '""');
            row.push('"' + cellText + '"');
        }
        csv.push(row.join(','));
    }
    
    // Download CSV file
    downloadCSV(csv.join('\n'), filename);
}

/**
 * Download CSV file
 */
function downloadCSV(csv, filename) {
    const csvFile = new Blob([csv], { type: "text/csv" });
    const downloadLink = document.createElement("a");
    
    // File name
    downloadLink.download = filename || 'export.csv';
    
    // Create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);
    
    // Hide download link
    downloadLink.style.display = "none";
    
    // Add the link to DOM
    document.body.appendChild(downloadLink);
    
    // Click download link
    downloadLink.click();
    
    // Clean up
    document.body.removeChild(downloadLink);
} 