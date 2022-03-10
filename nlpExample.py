import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
model = pyo.ConcreteModel()
model.x=pyo.Var(initialize=-2, bounds=(-5,5))
model.y=pyo.Var(initialize=-2, bounds=(-5,5))
x=model.x
y=model.y
model.obj=pyo.Objective(expr=cos(x+1)+cos(x)*cos(y), sense=maximize)
opt=SolverFactory('ipopt', executable='C:\\Ipopt-3.10.1-win64-intel11.1\\bin\\ipopt.exe')
opt.solve(model)
model.pprint()
print('x=', pyo.value(x))
print('y=', pyo.value(y))