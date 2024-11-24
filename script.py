names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0

average_cost = sum(estimated_insurance_costs) / len(estimated_insurance_costs)

for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    difference = insurance_cost - average_cost
    print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
    
    if insurance_cost > average_cost:
        print("The insurance cost for " + name + " is above average by " + str(difference) + " dollars.")
    elif insurance_cost < average_cost:
        print("The insurance cost for " + name + " is below average by " + str(-difference) + " dollars.")
    else:
        print("The insurance cost for " + name + " is equal to the average.")

