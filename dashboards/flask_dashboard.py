from flask import Flask, render_template_string
import pandas as pd
import xml.etree.ElementTree as ET
import re

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Test Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Robot Framework Test Dashboard</h1>
    <h2>Summary</h2>
    <div id="chart"></div>
    <h2>Test Details</h2>
    {{ table|safe }}
    <h2>Error Log Extract</h2>
    {{ errors|safe }}
    <script>
        var data = [{
            values: {{ values }},
            labels: {{ labels }},
            type: 'pie'
        }];
        Plotly.newPlot('chart', data);
    </script>
</body>
</html>
"""

def parse_robot_output(file_path="output.xml"):
    tree = ET.parse(file_path)
    root = tree.getroot()

    test_cases = []
    for suite in root.iter("suite"):
        for test in suite.iter("test"):
            name = test.attrib.get("name")
            status = test.find("status").attrib.get("status")
            test_cases.append({"TestCase": name, "Status": status})

    df = pd.DataFrame(test_cases)
    summary = df["Status"].value_counts()
    labels = list(summary.index)
    values = list(summary.values)

    return df.to_html(classes="table table-striped"), labels, values

def parse_log(file_path="log.html"):
    # Simplified: extract ERROR lines from Robot Framework log.html
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            errors = re.findall(r"ERROR.*", content)
    except FileNotFoundError:
        errors = ["No log.html found"]

    df = pd.DataFrame(errors, columns=["Error Lines"])
    return df.to_html(classes="table table-striped")

@app.route("/")
def dashboard():
    table, labels, values = parse_robot_output()
    errors = parse_log()
    return render_template_string(TEMPLATE, table=table, labels=labels, values=values, errors=errors)

if __name__ == "__main__":
    app.run(debug=True)
