# Import the linear solver wrapper,
from pulp import LpMaximize, LpProblem, LpVariable
import csv

print('\tStarting /home/duck/scripts/solver.py…')
path = '/home/duck/data'

model = LpProblem(name='Bathing_Friends', sense=LpMaximize)

# x = ducks and y = fish

x = LpVariable(name='ducks', lowBound=0)
y = LpVariable(name='fish', lowBound=0)

#adding constraints for linear equation

model += (x <= 400, 'time_constraint_duck')
model += (y <= 300, 'time_constraint_fish')
model += (y <= 400 - 0.8 * x, 'rubber_pellet_constraint')

objective_func = 5*x + 4*y
model += objective_func

print('Calculating optimal profit…')
status = model.solve()
profit = model.objective.value()

result_fish = 0
result_duck = 0
for var in model.variables():
    if var.name == 'ducks' :
        result_duck = var.value()
    elif var.name == 'fish' :
        result_fish = var.value()

print('Finished calculating optimal profit!')
print('Creating csv document with results… (You can find the results in …/data/csv_result_documents)')
row_list = [['production_quantity_ducks', 'production_quantity_fish', 'profit'],
             [result_duck, result_fish, profit]]
with open(path + '/csv_result_documents/bathing_firends_res1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

print('CSV File saved!')

#adding estimated demand constraints to linear equation
model += (y <= 50, 'estimated_fish_sell')
model += (x <= 150, 'estimated_ducks_sell')

print('Calculating optimal profit…')
status = model.solve()
profit = model.objective.value()

result_fish = 0
result_duck = 0
for var in model.variables():
    if var.name == 'ducks' :
        result_duck = var.value()
    elif var.name == 'fish' :
        result_fish = var.value()

print('Finished calculating optimal profit!')
print('Creating csv document with estimated demand constraints… (You can find the results in '
      '…/data/csv_result_documents)')
row_list = [['production_quantity_ducks', 'production_quantity_fish', 'profit'],
             [result_duck, result_fish, profit]]
with open(path + '/csv_result_documents/bathing_firends_res2_with_estimated_demands.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

print('CSV File saved!')
print('\tFinished /home/duck/scripts/solver.py!')