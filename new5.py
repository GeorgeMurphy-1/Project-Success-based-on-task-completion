import numpy as np
import matplotlib.pyplot as plt

# Function to simulate task completion rates
def simulate_completion_rate(num_steps, dt, a, b, c, noise_type='normal'):
    # Initialize arrays to store time and completion rate
    time = np.zeros(num_steps)
    completion_rate = np.zeros(num_steps)

    # Initial values
    time[0] = 0
    completion_rate[0] = 0.1  # Initial completion rate (adjust as needed)

    # Simulation loop
    for i in range(1, num_steps):
        # Deterministic part of the growth rate
        mu = a + b * time[i - 1]

        # Volatility term
        sigma = c * completion_rate[i - 1]

        # Generate noise based on the selected noise type
        if noise_type == 'normal':
            dW = np.random.normal(0, np.sqrt(dt), 1)
        elif noise_type == 'brownian':
            dW = np.random.standard_normal(1) * np.sqrt(dt)
        else:
            raise ValueError("Invalid noise type. Choose 'normal' or 'brownian'.")

        # Stochastic differential equation
        dP = mu * completion_rate[i - 1] * (1 - completion_rate[i - 1]) * dt + sigma * completion_rate[i - 1] * (1 - completion_rate[i - 1]) * dW

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
time, completion_rate = simulate_completion_rate(num_steps, dt, a, b, c, noise_type="brownian")

# Plot the results
plt.plot(time, completion_rate)
plt.title('Task Completion Rate Over Time')
plt.xlabel('Time')
plt.ylabel('Completion Rate')
plt.show()
