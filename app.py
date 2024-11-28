from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data for consultants and conversion rates
CONSULTANTS = ['Chris', 'Max']
CONVERSION_RATES = {'GBP': 1, 'USD': 0.79, 'EUR': 0.86}

# HTML template with embedded Python
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Perm Pipeline</title>
    <style>
        /* Add your CSS styles here */
    </style>
</head>
<body>
    <div class="header">
        <h1>Perm Pipeline</h1>
        <nav class="navigation">
            <a href="/" class="nav-item">Home</a>
            <a href="/pipeline" class="nav-item active">Perm Pipeline</a>
            <!-- Add other navigation items -->
        </nav>
    </div>
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>Consultant</th>
                    <th>Client Name</th>
                    <th>Role</th>
                    <!-- Add other headers -->
                </tr>
            </thead>
            <tbody id="pipelineBody">
                <!-- Dynamic content will be inserted here -->
            </tbody>
        </table>
    </div>

    <!-- Modal HTML -->
    <div id="candidateModal" class="modal" style="display:none;">
        <!-- Modal content -->
    </div>

    <script type="text/javascript">
        const CONSULTANTS = {{ consultants }};
        const CONVERSION_RATES = {{ conversion_rates }};
        
        function addRow() {
            // JavaScript function to add a new row
        }

        function calculateFees(row) {
            // JavaScript function to calculate fees
        }
        
        // Additional JavaScript functions
    </script>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_template, consultants=CONSULTANTS, conversion_rates=CONVERSION_RATES)

if __name__ == '__main__':
    app.run(debug=True)
