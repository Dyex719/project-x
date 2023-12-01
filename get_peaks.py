import matplotlib.pyplot as plt
import pickle
from scipy.signal import find_peaks
import numpy as np

pickle_file_path = 'data.pkl'

# Read the data from the pickle file
with open(pickle_file_path, 'rb') as pickle_file:
    data = pickle.load(pickle_file)

# print('Loaded data:', loaded_data)

# time_points = [entry['start_time'] for entry in data] + [data[-1]['end_time']]
# values = [entry['value'] for entry in data] + [data[-1]['value']]

# plt.plot(time_points, values, 'b-', label='Data Line')

# plt.xlabel('Time')
# plt.ylabel('Value')
# plt.title('Continuous Line Graph of Data')
# plt.legend()
# plt.show()

time_points = [entry['start_time'] for entry in data] + [data[-1]['end_time']]
values = [entry['value'] for entry in data] + [data[-1]['value']]

# Create a numpy array for time_points and values
time_array = np.array([0.0] + time_points)
values_array = np.array([0.0] + values)

# Define the interval duration
interval_duration = 10.0  # seconds

peaks, _ = find_peaks(values_array, height=0.0)
valleys, _ = find_peaks(-values_array, height=0.0)

# Plot the line graph with smaller red circles for peaks and smaller blue circles for valleys
plt.plot(time_array, values_array, label='Data')
plt.plot(time_array[peaks], values_array[peaks], 'ro', label='Peaks', markersize=3)
plt.plot(time_array[valleys], values_array[valleys], 'yo', label='Valleys', markersize=3)
plt.title('Peaks and Valleys for Each 10-second Interval')
plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()