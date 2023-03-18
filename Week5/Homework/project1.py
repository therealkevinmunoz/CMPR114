def collect_assesment():
    #check variable type
    try:
        property_value = float(input("What is the value of your property? "))
        return property_value
    except ValueError:
        print("Please enter a valid number")
        collect_assesment()

    
def get_assessment_value(value):
    assessment_value = value * .60
    return assessment_value

def get_tax_value(value):
    tax_value = (value / 100) * .72
    return tax_value

#main function to trigger all other functions
def main():
    property_value = collect_assesment()
    assessment_value = get_assessment_value(property_value)
    print(f"Assessment Value: ${assessment_value:.2f}")
    print(f"Tax Value: ${get_tax_value(assessment_value):.2f}")

#trigger main function
main()