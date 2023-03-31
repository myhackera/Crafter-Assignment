import csv

# Function to calculate total revenue
def calculate_total_revenue(file_name):
    total_revenue = 0
    d = {
            '1': 'January', 
            '2': 'February', 
            '3': 'March', 
            '4': 'April', 
            '5': 'May', 
            '6': 'June', 
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        }
    with open(file_name) as csv_file:
        csv_read = csv.DictReader(csv_file)
        for r in csv_read:
            print("Total Profit Generated in month of "+ d[r['month_number']] + " is", int(r['total_profit']))
            total_revenue += int(r['total_profit'])
            
    
    return total_revenue


if __name__ == '__main__':
    file_name = './company-sales.csv'
    revenue = calculate_total_revenue(file_name)
    print(f"Total revenue generated from FY23 sales: ${revenue:.2f}")

'''
Output :

Total Profit Generated in month of January is 211000
Total Profit Generated in month of February is 183300 
Total Profit Generated in month of March is 224700    
Total Profit Generated in month of April is 222700    
Total Profit Generated in month of May is 209600      
Total Profit Generated in month of June is 201400     
Total Profit Generated in month of July is 295500     
Total Profit Generated in month of August is 361400   
Total Profit Generated in month of September is 234000
Total Profit Generated in month of October is 266700
Total Profit Generated in month of November is 412800
Total Profit Generated in month of December is 300200
Total revenue generated from FY23 sales: $3123300.00

'''
