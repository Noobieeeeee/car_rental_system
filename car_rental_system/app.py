from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Route for the landing page
@app.route('/')
def home():
    return render_template('mainpage.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)