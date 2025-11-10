from flask import Flask, render_template_string
app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<title>Flask Docker App</title>
</head>
<body style="background: lightblue; text-align:center; padding-top:100px;">
<h1>✅ Flask inside Docker!</h1>
<p>This is working successfully!</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
