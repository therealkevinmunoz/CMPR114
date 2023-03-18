def collect_sales():
    #check variable type
    try:
        sales_value = float(input("What are your total sales for this month? "))
        return sales_value
    except ValueError:
        print("Please enter a valid number")
        collect_sales()

    
def get_state_tax(value):
    state_tax = value * .05
    return state_tax

def get_county_tax(value):
    county_tax = value * 0.025
    return county_tax

#main function to trigger all other functions
def main():
    sales_value = collect_sales()
    state_tax = get_state_tax(sales_value)
    county_tax = get_county_tax(sales_value)
    #display values to user
    print(f"Total Sales: ${sales_value:.2f}")
    print(f"State Tax: ${state_tax:.2f}")
    print(f"County Tax: ${county_tax:.2f}")

#trigger main function
main()