from math import sin, cos, tanh, pi, sqrt

def u1(X):
    return 0.600*sin(X[1]) + cos(X[0]) + 3.00

def v1(X):
    return 3.70*sin(1.30*X[0]*X[1]/pi) - 1.80*sin(1.70*X[0]) - 1.30*cos(2.10*X[1]) + 5.20

def p(X):
    return 50.0*sin(X[0]**2 + X[1]**2) + 25.0

def rho1(X):
    return 0.500*sin(X[0]**2 + X[1]**2) + 0.750

def vfrac1(X):
    return -0.500*sin(X[0]**2 + X[1]**2) + 0.900

def forcing_u1(X):
    return -(-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*(0.600*sin(X[1]) + cos(X[0]) + 3.00)*sin(X[0]) + 0.600*(-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*(3.70*sin(1.30*X[0]*X[1]/pi) - 1.80*sin(1.70*X[0]) - 1.30*cos(2.10*X[1]) + 5.20)*cos(X[1]) + 100.*(-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*X[0]*cos(X[0]**2 + X[1]**2) + (3.36700000000000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 2.14200000000000*cos(1.70*X[0]) + 0.420*cos(X[1]))*X[1]*cos(X[0]**2 + X[1]**2) + (-2.24466666666667*X[0]*cos(1.30*X[0]*X[1]/pi)/pi - 0.933333333333333*sin(X[0]) - 1.27400000000000*sin(2.10*X[1]))*X[0]*cos(X[0]**2 + X[1]**2) - 0.707106781000000*(-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750) - (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(-4.37710000000000*X[0]*X[1]*sin(1.30*X[0]*X[1]/pi)/pi**2 + 3.36700000000000*cos(1.30*X[0]*X[1]/pi)/pi - 0.420*sin(X[1])) - (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(2.91806666666667*X[0]*X[1]*sin(1.30*X[0]*X[1]/pi)/pi**2 - 2.24466666666667*cos(1.30*X[0]*X[1]/pi)/pi - 0.933333333333333*cos(X[0]))

def forcing_v1(X):
    return (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*(0.600*sin(X[1]) + cos(X[0]) + 3.00)*(4.81*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 3.06*cos(1.70*X[0])) + (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*(4.81*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 2.73*sin(2.10*X[1]))*(3.70*sin(1.30*X[0]*X[1]/pi) - 1.80*sin(1.70*X[0]) - 1.30*cos(2.10*X[1]) + 5.20) + 100.*(-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*X[1]*cos(X[0]**2 + X[1]**2) + (3.36700000000000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 2.14200000000000*cos(1.70*X[0]) + 0.420*cos(X[1]))*X[0]*cos(X[0]**2 + X[1]**2) + (4.48933333333333*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 0.466666666666667*sin(X[0]) + 2.54800000000000*sin(2.10*X[1]))*X[1]*cos(X[0]**2 + X[1]**2) - 0.707106781000000*(-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750) - (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(-4.37710000000000*X[1]**2*sin(1.30*X[0]*X[1]/pi)/pi**2 + 3.64140000000000*sin(1.70*X[0])) - (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(-5.83613333333333*X[0]**2*sin(1.30*X[0]*X[1]/pi)/pi**2 + 5.35080000000000*cos(2.10*X[1]))

def forcing_rho1(X):
    return (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.600*sin(X[1]) + cos(X[0]) + 3.00)*X[0]*cos(X[0]**2 + X[1]**2) + (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(3.70*sin(1.30*X[0]*X[1]/pi) - 1.80*sin(1.70*X[0]) - 1.30*cos(2.10*X[1]) + 5.20)*X[1]*cos(X[0]**2 + X[1]**2) - (0.500*sin(X[0]**2 + X[1]**2) + 0.750)*(0.600*sin(X[1]) + cos(X[0]) + 3.00)*X[0]*cos(X[0]**2 + X[1]**2) - (0.500*sin(X[0]**2 + X[1]**2) + 0.750)*(3.70*sin(1.30*X[0]*X[1]/pi) - 1.80*sin(1.70*X[0]) - 1.30*cos(2.10*X[1]) + 5.20)*X[1]*cos(X[0]**2 + X[1]**2) + (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*(4.81*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 2.73*sin(2.10*X[1])) - (-0.500*sin(X[0]**2 + X[1]**2) + 0.900)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*sin(X[0]) + (0.500*sin(X[0]**2 + X[1]**2) + 0.750)*((0.275*sin(3.00*X[0]*X[1]/pi) - 2.00*sin(7.50*X[0]) + cos(X[1]) - 1.00)*X[1]*cos(X[0]**2 + X[1]**2) + (0.500*sin(X[0]**2 + X[1]**2) + 0.100)*(0.825*X[0]*cos(3.00*X[0]*X[1]/pi)/pi - sin(X[1]))) + (0.500*sin(X[0]**2 + X[1]**2) + 0.750)*((0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*X[0]*cos(X[0]**2 + X[1]**2) + (0.500*sin(X[0]**2 + X[1]**2) + 0.100)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0])))

def velocity1(X):
   return [u1(X), v1(X)]

def forcing_velocity1(X):
   return [forcing_u1(X), forcing_v1(X)]

def u2(X):
    return 0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900

def v2(X):
    return 0.275*sin(3.00*X[0]*X[1]/pi) - 2.00*sin(7.50*X[0]) + cos(X[1]) - 1.00

def rho2(X):
    return 3.00

def vfrac2(X):
    return 0.500*sin(X[0]**2 + X[1]**2) + 0.100

def forcing_u2(X):
    return 100.*(0.500*sin(X[0]**2 + X[1]**2) + 0.100)*X[0]*cos(X[0]**2 + X[1]**2) + (1.50*sin(X[0]**2 + X[1]**2) + 0.300)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900) + (1.50*sin(X[0]**2 + X[1]**2) + 0.300)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.275*sin(3.00*X[0]*X[1]/pi) - 2.00*sin(7.50*X[0]) + cos(X[1]) - 1.00) - (-0.495*X[0]*cos(3.00*X[0]*X[1]/pi)/pi - 0.384*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.648*sin(0.600*X[0]) + 0.600*sin(X[1]))*X[0]*cos(X[0]**2 + X[1]**2) - (-0.288*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.742500000000000*X[1]*cos(3.00*X[0]*X[1]/pi)/pi - 13.5*cos(7.50*X[0]) + 0.378*cos(0.700*X[1]))*X[1]*cos(X[0]**2 + X[1]**2) - (0.500*sin(X[0]**2 + X[1]**2) + 0.100)*(1.48500000000000*X[0]*X[1]*sin(3.00*X[0]*X[1]/pi)/pi**2 - 0.307200000000000*X[1]**2*cos(0.800*X[0]*X[1]/pi)/pi**2 - 0.495*cos(3.00*X[0]*X[1]/pi)/pi - 0.388800000000000*cos(0.600*X[0])) - (0.500*sin(X[0]**2 + X[1]**2) + 0.100)*(-0.230400000000000*X[0]**2*cos(0.800*X[0]*X[1]/pi)/pi**2 - 2.22750000000000*X[0]*X[1]*sin(3.00*X[0]*X[1]/pi)/pi**2 + 0.742500000000000*cos(3.00*X[0]*X[1]/pi)/pi - 0.264600000000000*sin(0.700*X[1])) - 1.06066017150000*sin(X[0]**2 + X[1]**2) - 0.212132034300000

def forcing_v2(X):
    return 100.*(0.500*sin(X[0]**2 + X[1]**2) + 0.100)*X[1]*cos(X[0]**2 + X[1]**2) + (1.50*sin(X[0]**2 + X[1]**2) + 0.300)*(0.825*X[1]*cos(3.00*X[0]*X[1]/pi)/pi - 15.0*cos(7.50*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900) + (1.50*sin(X[0]**2 + X[1]**2) + 0.300)*(0.825*X[0]*cos(3.00*X[0]*X[1]/pi)/pi - sin(X[1]))*(0.275*sin(3.00*X[0]*X[1]/pi) - 2.00*sin(7.50*X[0]) + cos(X[1]) - 1.00) - (0.990*X[0]*cos(3.00*X[0]*X[1]/pi)/pi + 0.192*X[1]*sin(0.800*X[0]*X[1]/pi)/pi + 0.324*sin(0.600*X[0]) - 1.20*sin(X[1]))*X[1]*cos(X[0]**2 + X[1]**2) - (-0.288*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.742500000000000*X[1]*cos(3.00*X[0]*X[1]/pi)/pi - 13.5*cos(7.50*X[0]) + 0.378*cos(0.700*X[1]))*X[0]*cos(X[0]**2 + X[1]**2) - (0.500*sin(X[0]**2 + X[1]**2) + 0.100)*(-0.230400000000000*X[0]*X[1]*cos(0.800*X[0]*X[1]/pi)/pi**2 - 2.22750000000000*X[1]**2*sin(3.00*X[0]*X[1]/pi)/pi**2 - 0.288*sin(0.800*X[0]*X[1]/pi)/pi + 101.250000000000*sin(7.50*X[0])) - (0.500*sin(X[0]**2 + X[1]**2) + 0.100)*(-2.97*X[0]**2*sin(3.00*X[0]*X[1]/pi)/pi**2 + 0.153600000000000*X[0]*X[1]*cos(0.800*X[0]*X[1]/pi)/pi**2 + 0.192*sin(0.800*X[0]*X[1]/pi)/pi - 1.20*cos(X[1])) - 1.06066017150000*sin(X[0]**2 + X[1]**2) - 0.212132034300000

def velocity2(X):
   return [u2(X), v2(X)]

def forcing_velocity2(X):
   return [forcing_u2(X), forcing_v2(X)]

def forcing_vfrac2(X):
    return (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*X[0]*cos(X[0]**2 + X[1]**2) + (0.275*sin(3.00*X[0]*X[1]/pi) - 2.00*sin(7.50*X[0]) + cos(X[1]) - 1.00)*X[1]*cos(X[0]**2 + X[1]**2) + (0.500*sin(X[0]**2 + X[1]**2) + 0.100)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0])) + (0.500*sin(X[0]**2 + X[1]**2) + 0.100)*(0.825*X[0]*cos(3.00*X[0]*X[1]/pi)/pi - sin(X[1]))

