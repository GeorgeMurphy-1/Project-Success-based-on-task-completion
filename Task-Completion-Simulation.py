import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to simulate task completion rates
def simulate_completion_rate(num_steps, dt, a, b, c, noise_type):
    # Initialize arrays to store time and completion rate
    time = np.zeros(num_steps)
    completion_rate = np.zeros(num_steps)

    # Initial values
    time[0] = 0
    completion_rate[0] = 0.2  # Initial completion rate (adjust as needed)

    # Generate Wiener process (Brownian motion)
    
    
    if noise_type == 'normal':
        dW = np.random.normal(0, np.sqrt(dt), 1)
    elif noise_type == 'brownian':
       
        dW = np.random.normal(0,np.random.standard_normal(1) * np.sqrt(dt), num_steps - 1)
    else:
        raise ValueError("Invalid noise type. Choose 'normal' or 'brownian'.")


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

# Create figure and axes
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the bottom to make room for sliders

# Plot the initial results
time, completion_rate = simulate_completion_rate(num_steps, dt, a, b, c, noise_type="brownian")
line, = ax.plot(time, completion_rate)
ax.set_title('Task Completion Rate Over Time')
ax.set_xlabel('Time')
ax.set_ylabel('Completion Rate')

# Add sliders for adjusting parameters
axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_c = plt.axes([0.25, 0.00, 0.65, 0.03], facecolor=axcolor)

s_a = Slider(ax_a, 'a', 0.01, 1.0, valinit=a)
s_b = Slider(ax_b, 'b', 0.01, 0.1, valinit=b)
s_c = Slider(ax_c, 'c', 0.01, 1.0, valinit=c)

def update(val):
    a = s_a.val
    b = s_b.val
    c = s_c.val
    time, completion_rate = simulate_completion_rate(num_steps, dt, a, b, c, noise_type="brownian")
    line.set_ydata(completion_rate)
    fig.canvas.draw_idle()

s_a.on_changed(update)
s_b.on_changed(update)
s_c.on_changed(update)

plt.show()