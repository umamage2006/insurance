from sklearn.linear_model import LinearRegression

def generate_recommendations(age, income, health_expenses, savings_goal, current_investment, data):
    # Train a simple Linear Regression model to predict future health expenses
    X = data[['age', 'income']].values
    y = data['health_expenses'].values
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict future health expenses based on user input
    future_health_expenses = model.predict([[age, income]])[0]
    
    # Generate health insurance recommendation
    if future_health_expenses > health_expenses:
        health_plan = "Consider upgrading your health insurance."
    else:
        health_plan = "Your current health insurance is sufficient."
    
    # Financial recommendations
    future_investment = current_investment * 1.05  # Assuming 5% growth
    if future_investment < savings_goal:
        investment_plan = "Increase monthly savings to reach your goal."
    else:
        investment_plan = "You're on track to meet your financial goals."
    
    return {
        'health_plan': health_plan,
        'investment_plan': investment_plan,
        'predicted_health_expenses': future_health_expenses,
        'future_investment': future_investment
    }
