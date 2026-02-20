from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>RegApp - Kubernetes Deployment</title>
        <style>
            body {
                background-color: #0f172a;
                color: white;
                text-align: center;
                font-family: Arial, sans-serif;
                margin-top: 100px;
            }
            h1 {
                color: #38bdf8;
            }
            .box {
                background: #1e293b;
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Python App Successfully Deployed!</h1>
            <p>This application is running inside Kubernetes.</p>
            <p>Container Port: 5000</p>
            <p>Deployed via ECR + EKS</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)