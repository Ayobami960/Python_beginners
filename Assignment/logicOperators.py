# University  Tilcareer list of course
cars = ['BUSINESS MANAGEMENT', 'FRONTEND DEVELOPMENT', 'BACKEND DEVELOPMENT', 'FULL STACK', 'CYBER SECURITY', 'PYTHON']

model1 = 'ewmf'
model2 = 'enfkw'
model3 = 'DATA ANALYST'

# Decision- making using logical operators
if model1 in cars and model2 in cars:
    print("Both course are in the program.")
else:
    print("course are not available in this section")

if model1 in cars or model3 in cars:
    print("At least one course is in the program.")
else:
    print("no course selected in model1 and model2")
    
if model3 not in cars:
    print("data analyst is not in the program.")
else:
    print("invalid")
