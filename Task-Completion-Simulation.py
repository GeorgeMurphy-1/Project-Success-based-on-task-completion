import numpy as np
import matplotlib.pyplot as plt

# Function to simulate task completion rates
def simulate_completion_rate(num_steps, dt, a, b, c):
    # Initialize arrays to store time and completion rate
    time = np.zeros(num_steps)
    completion_rate = np.zeros(num_steps)

    # Initial values
    time[0] = 0
    completion_rate[0] = 1  # Initial completion rate (adjust as needed)

    # Generate Wiener process (Brownian motion)
    dW = np.random.normal(0, np.sqrt(dt), num_steps - 1)

    # Simulation loop
    for i in range(1, num_steps):
        # Deterministic part of the growth rate
        mu = a + b * time[i - 1]

        # Volatility term
        sigma = c * completion_rate[i - 1]

        # Stochastic differential equation
        dP = mu * completion_rate[i - 1] * (1 - completion_rate[i - 1]) * dt + sigma * completion_rate[i - 1] * (1 - completion_rate[i - 1]) * dW[i - 1]

        # Update time and completion rate
        time[i] = time[i - 1] + dt
        completion_rate[i] = completion_rate[i - 1] + dP

    return time, completion_rate

# Simulation parameters
num_steps = 1000
dt = 0.1
a = 0.1
b = 0.02
c = 0.1

# Run the simulation
time, completion_rate = simulate_completion_rate(num_steps, dt, a, b, c)

# Plot the results
plt.plot(time, completion_rate)
plt.title('Task Completion Rate Over Time')
plt.xlabel('Time')
plt.ylabel('Completion Rate')
plt.show()

