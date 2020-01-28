import matplotlib.pyplot as plt
import plottingFunctions as pltFuncts
import membershipFunctions as membFuncts

# Defining the input axis Domain.
inputDomain = { 'xmin' : -8, 'xmax' : 45 }
inputDomain = pltFuncts.getAxisValues(inputDomain, 0.1)

# Defining the output axis Domain.
outputDomainValues = { 'xmin' : -0.5, 'xmax' : 5 }
outputDomain = pltFuncts.getAxisValues(outputDomainValues, 0.5)

#Input Membership functions values.
frozen  =   { 'a' : 0,  'b' : 6  }
cold    =   { 'a' : 4,  'b' : 10,   'c' : 16 }
mild    =   { 'a' : 10, 'b' : 18,   'c' : 26 }
warm    =   { 'a' : 20, 'b' : 26,   'c' : 32 }
hot     =   { 'a' : 30, 'b' : 36 }

#Input Membership functions values.
low     = { 'a' : 0, 'b' : 1, 'c' : 2 }
medium  = { 'a' : 1, 'b' : 2, 'c' : 3 }
high    = { 'a' : 2, 'b' : 3, 'c' : 4 }

x = 14

print(membFuncts.linearFunction(frozen, x, False))
print(membFuncts.triangleFunction(cold, x))
print(membFuncts.triangleFunction(mild, x))
print(membFuncts.triangleFunction(warm, x))
print(membFuncts.linearFunction(hot, x))

fig, ax = plt.subplots()
ax.plot( inputDomain, pltFuncts.linearFunction( frozen, inputDomain, False ), label="Frozen",    color = 'indigo'    )
ax.plot( inputDomain, pltFuncts.triangleFunction( cold,   inputDomain ),      label="Cold",      color = 'blue'      )
ax.plot( inputDomain, pltFuncts.triangleFunction( mild,   inputDomain ),      label="Mild",      color = 'green'     )
ax.plot( inputDomain, pltFuncts.triangleFunction( warm,   inputDomain ),      label="Warm",      color = 'gold'      )
ax.plot( inputDomain, pltFuncts.linearFunction(   hot,    inputDomain ),      label="Hot",       color = 'red'       )
ax.legend()
plt.show()

plt.plot( outputDomain, pltFuncts.triangleFunction( low,   outputDomain ),      label="Low",      color = 'blue'     )
plt.plot( outputDomain, pltFuncts.triangleFunction( medium,   outputDomain ),   label="Medium",   color = 'green'    )
plt.plot( outputDomain, pltFuncts.triangleFunction( high,   outputDomain ),     label="High",     color = 'red'      )
plt.legend()
plt.show()
