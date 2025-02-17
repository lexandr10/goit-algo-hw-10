from pulp import LpMaximize, LpProblem, LpVariable


model = LpProblem(name="production-optimization", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
juice = LpVariable(name="Juice", lowBound=0, cat="Integer")


model += lemonade + juice, "Total Production"


model += (2 * lemonade + 1 * juice <= 100, "Water Constraint")
model += (1 * lemonade <= 50, "Sugar Constraint")
model += (1 * lemonade <= 30, "Lemon Juice Constraint")
model += (2 * juice <= 40, "Fruit Puree Constraint")

model.solve()

print(f"Optimal production:")
print(f"Lemonade: {int(lemonade.varValue)} units")
print(f"Fruit Juice: {int(juice.varValue)} units")
