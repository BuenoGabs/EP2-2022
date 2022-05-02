from  math import * 
def haversine(raio,omega1,lambda1,omega2,lambda2):
    omega1_r = radians(omega1)
    lambda1_r = radians(lambda1)
    omega2_r = radians(omega2)
    lambda2_r = radians(lambda2)
    d1 = sin(omega2_r-omega1_r/2)**2 + cos(omega1_r) * cos(omega2_r) * sin(lambda2_r-lambda1_r/2)**2
    d2 = sqrt(d1)
    distancia = 2*raio*asin(d2)
    return degrees(distancia)
