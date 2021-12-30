import xlsxwriter
import sympy
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.figure as figure

a, b, x, y = sympy.symbols("a b x y")

print("Beginning program")

lower = input("\nEnter lower bound: ")
upper = input("\nEnter upper bound: ")
num = input("\nEnter number of values: ")

# Array of a-values to plug into the bounds of the integral
a_values = np.linspace(int(lower), int(upper), int(num))

# Setting b equal to a constant of 1
b = 1

# Equation of the ellipse solved for y
# TODO: ellipse is a single value but "a" is an array, hence the error
ellipse = sympy.sqrt((b ** 2) * (1 - ((x ** 2) / (a ** 2))))

# Functions to be tested
test_functions = [(a * b * x), (((a * b) ** 2) * x), (((a * b) ** 3) * x), (((a * b) ** 4) * x), (((a * b) ** 5) * x)]

print("\nSolving for test functions")

# Equating ellipse and test_functions so their intersection can be symbolically solved for
equate = [sympy.Eq(ellipse, test_functions[0]), sympy.Eq(ellipse, test_functions[1]),
          sympy.Eq(ellipse, test_functions[2]),
          sympy.Eq(ellipse, test_functions[3]), sympy.Eq(ellipse, test_functions[4])]

# Array that holds the bounds of the integral solved symbolically
bounds_symbolic = []
integrand = []
for i in range(0, 5):
    bounds_symbolic.append(sympy.solve(equate[i], x))
    integrand.append(ellipse - test_functions[i])

# New array with a-values substituted into the bounds
bounds_ab = bounds_symbolic  # Right now this is redundant, might not be needed, but I don't know right now

# Substituting a_vals into bounds_ab

# Creating upper and lower bounds arrays for each function

bounds_1_up = []
bounds_1_low = []


function_1_integrand = []


print("\nSubstituting a-values into integrands...")

# This loop puts the array of a-values into the bounds and the integrand
for k in range(0, len(a_values)):
    # Substituting in the a-values from a-values array into the bounds

    bounds_1_up.append(-1 * (a_values[k] * sympy.sqrt(1 / (a_values[k] ** 4 + 1))))
    bounds_1_low.append(a_values[k] * sympy.sqrt(1 / (a_values[k] ** 4 + 1)))

    function_1_integrand.append(integrand[0].subs(a, a_values[k]))

function_1_area = []

print("\nIntegrating over all " + str(num) + " a-values...")

for q in range(0, len(a_values)):
    function_1_area.append(sympy.integrate(function_1_integrand[q], (x, bounds_1_low[q], bounds_1_up[q])))

# Plotting
x = a_values

y = function_1_area

figure, axes = plot.subplots()
axes.grid(True)
axes.plot(x, y)

axes.set(xlabel='a-value', ylabel='Area', title='A-values and Area TF 1, b=1')

plot.savefig("TF_actual.png")
plot.show()

# Writing data to an Excel file
print("\nWriting data to an Excel file")

# Creating a workbook and adding a worksheet
workbook = xlsxwriter.Workbook('data_ellipse_single.xlsx')

k = 0
row = 1
col = 0

worksheet = workbook.add_worksheet('(ab)x')
worksheet.write('A1', 'a-value')
worksheet.write('B1', 'Area')

for k in range(0, len(x)):
    worksheet.write_number(row, col, x[k])
    worksheet.write_number(row, col + 1, y[k])
    row += 1

workbook.close()

# Function fitting with data

print("\nProgram executed")
