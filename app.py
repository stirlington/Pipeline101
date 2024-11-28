from flask import Flask, render_template_string

app = Flask(__name__)

# HTML content as a multi-line string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Combined Recruitment Pipeline Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .header {
            background-color: #007BFF;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .navigation {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .nav-item {
            color: white;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        .nav-item:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        .nav-item.active {
            background-color: rgba(255, 255, 255, 0.2);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Combined Recruitment Pipeline Tracker</h1>
        <nav class="navigation">
            <a href="#" class="nav-item">Home</a>
            <a href="#" class="nav-item active">Perm Pipeline</a>
            <a href="#" class="nav-item">Contractor Pipeline</a>
            <a href="#" class="nav-item">Perm Offers</a>
            <a href="#" class="nav-item">Contractor Offers</a>
            <a href="#" class="nav-item">Rejected/Failed</a>
            <a href="#" class="nav-item">Invoiced</a>
            <a href="#" class="nav-item">Stats</a>
        </nav>
    </div>

    <div class="table-container">
        <h2>Perm Pipeline</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Consultant</th>
                    <th>Client Name</th>
                    <th>Role</th>
                    <th>Candidate</th>
                    <th>Fee %</th>
                    <th>Fee (£)</th>
                    <th>Probability %</th>
                    <th>Probability Fee (£)</th>
                    <th>VAT</th>
                    <th>Est. Invoice Month</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody id="pipelineBody"></tbody>
        </table>
        <button onclick="addRow()" class="add-row-button">Add New Row</button>
    </div>

    <script>
        const CONSULTANTS = ['Chris', 'Max'];

        function addRow() {
            const tbody = document.getElementById('pipelineBody');
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><select class="consultant"><option value="">Select Consultant</option>${CONSULTANTS.map(consultant => `<option value="${consultant}">${consultant}</option>`).join('')}</select></td>
                <td><input type="text" class="client-name"></td>
                <td><input type="text" class="role"></td>
                <td><input type="text" class="candidate"></td>
                <td><input type="number" class="fee-percent"></td>
                <td class="fee">£0.00</td>
                <td><input type="number" class="probability"></td>
                <td class="probability-fee">£0.00</td>
                <td><select class="vat"><option value="Yes">Yes</option><option value="No">No</option></select></td>
                <td><input type="text" class="invoice-month"></td>
                <td><button onclick="deleteRow(this)">Delete</button></td>`;
            tbody.appendChild(row);
        }

        function deleteRow(button) {
            const row = button.closest('tr');
            row.remove();
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
