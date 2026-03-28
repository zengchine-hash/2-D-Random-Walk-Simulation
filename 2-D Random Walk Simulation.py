import numpy as np
import matplotlib.pyplot as plt
def simulate_random_walk_2d(num_steps, num_simulations):
    squared_displacements = []    
    plt.figure(figsize=(10, 6))   
    for i in range(num_simulations):
        steps = np.random.choice(['up', 'down', 'left', 'right'], num_steps)      
        x = np.cumsum([1 if s == 'right' else -1 if s == 'left' else 0 for s in steps])
        y = np.cumsum([1 if s == 'up' else -1 if s == 'down' else 0 for s in steps])       
        final_r2 = x[-1]**2 + y[-1]**2
        squared_displacements.append(final_r2)
        if i < 10:
            plt.plot(x, y, alpha=0.6, label=f'Walk {i+1}')
    rms_displacement = np.sqrt(np.mean(squared_displacements))
    plt.title(f"2D Random Walk: {num_steps} Steps")
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.grid(True, linestyle='--')
    plt.show()
    return rms_displacement
N = 1000  #number of steps
sims = 500  # number of simulations
calculated_rms = simulate_random_walk_2d(N, sims)
theoretical_rms = np.sqrt(N)
print(f"steps (N): {N}")
print(f"experimental result RMS Displacement: {calculated_rms:.2f}")
print(f"calculated result (sqrt(N)): {theoretical_rms:.2f}")
print(f"diference: {abs(calculated_rms - theoretical_rms) / theoretical_rms:.2%}")
