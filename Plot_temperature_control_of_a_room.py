import matplotlib.pyplot as plt
import plottingFunctions as pltFuncts
import membershipFunctions as membFuncts


# Defining the x axis range.

xaxis = { 'xmin' : -8, 'xmax' : 45 }
xrange = pltFuncts.getAxisValues(xaxis, 0.1)

#Membership functions values.
frozen  =   { 'a' : 0,  'b' : 6 }
cold    =   { 'a' : 4,  'b' : 10,   'c' : 16 }
mild    =   { 'a' : 10, 'b' : 18,   'c' : 26 }
warm    =   { 'a' : 20, 'b' : 26,   'c' : 32 }
hot     =   { 'a' : 30, 'b' : 36 }

x = 21

print(membFuncts.linearFunction(frozen, x, False))
print(membFuncts.triangleFunction(cold, x))
print(membFuncts.triangleFunction(mild, x))
print(membFuncts.triangleFunction(warm, x))
print(membFuncts.linearFunction(hot, x))

fig, ax = plt.subplots()
ax.plot( xrange, pltFuncts.linearFunction( frozen, xrange, False ), label="Frozen",    color = 'indigo'    )
ax.plot( xrange, pltFuncts.triangleFunction( cold,   xrange ),      label="Cold",      color = 'blue'      )
ax.plot( xrange, pltFuncts.triangleFunction( mild,   xrange ),      label="Mild",      color = 'green'     )
ax.plot( xrange, pltFuncts.triangleFunction( warm,   xrange ),      label="Warm",      color = 'gold'      )
ax.plot( xrange, pltFuncts.linearFunction(   hot,    xrange ),      label="Hot",       color = 'red'       )
ax.plot( xrange, pltFuncts.linearFunction(   hot,    xrange ),      label="Hot",       color = 'red'       )
ax.legend()

plt.show()