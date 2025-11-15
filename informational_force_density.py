# Informational Force Density Verification (vOmega Law 33)

import numpy as np

# Synthetic informational field rho(x)
N = 400
x = np.linspace(0, 1, N)
dx = x[1] - x[0]

# Example informational potential A(x)
A = np.exp(-((x - 0.4)**2) / 0.01)

# Force density f_info = - dA/dx
def grad(f):
    return (np.roll(f, -1) - np.roll(f, 1)) / (2*dx)

f_info = -grad(A)

# Check equilibrium condition: integral f_info dx ≈ 0 (balanced forces)
integral = np.sum(f_info) * dx

print("Force density sample:", f_info[:10])
print("Integral of force density (should be ~0):", integral)
