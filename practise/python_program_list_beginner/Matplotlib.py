import numpy as np

import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
face_cream_sales = [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900]
facewash_sales = [1500, 1200, 1340, 1130, 1740, 1550, 1430, 1800, 2100, 1760, 1800, 2100]

# Bar width
bar_width = 0.35

# Positions of the bars on the x-axis
r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]

# Create the bar chart
plt.bar(r1, face_cream_sales, color='blue', width=bar_width, edgecolor='grey', label='Face Cream')
plt.bar(r2, facewash_sales, color='green', width=bar_width, edgecolor='grey', label='Face Wash')

# Add labels
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Face Cream and Face Wash Sales Data')
plt.xticks([r + bar_width/2 for r in range(len(months))], months)
plt.legend()

# Show the plot
plt.show()