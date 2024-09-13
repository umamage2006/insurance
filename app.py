from flask import Flask, render_template, request
from models import generate_recommendations
import pandas as pd

app = Flask(__name__)

# Load sample data from CSV (this can later be replaced by real-time data)
data = pd.read_csv("templates/data/sample_data.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    # Get the input values from the form
    age = int(request.form['age'])
    income = float(request.form['income'])
    health_expenses = float(request.form['health_expenses'])
    savings_goal = float(request.form['savings_goal'])
    current_investment = float(request.form['current_investment'])
    
    # Get recommendations using AI/ML model
    recommendations = generate_recommendations(age, income, health_expenses, savings_goal, current_investment, data)
    
    return render_template('index.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
