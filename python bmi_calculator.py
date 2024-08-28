def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """Determine the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    
    category = get_bmi_category(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Based on your BMI, you are classified as: {category}")
    
    if category == "Underweight":
        print("Consider consulting with a healthcare provider for a diet plan to reach a healthier weight.")
    elif category == "Normal weight":
        print("Keep up the good work! Maintain a healthy lifestyle with balanced nutrition and regular exercise.")
    elif category == "Overweight":
        print("Consider a balanced diet and regular physical activity to help reduce your weight.")
    else:  
        print("It's recommended to seek advice from a healthcare provider to develop a plan for achieving a healthier weight.")

if __name__ == "__main__":
    main()
