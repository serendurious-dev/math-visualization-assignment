#================================================
# MATHEMATICAL VISUALIZATION ASSIGNMENT
#================================================


# Required Libraries
import numpy as np
import matplotlib.pyplot as plt

#================================================
# TASK 1 - Mathematical Function Visualization
#================================================

print("=" * 50)
print("TASK 1 - Mathematical Function Visualization")
print("=" * 50)

# Validation for minimum number of points
points = 500

if points < 200:
    print("Error: At least 200 points are required.")
    exit()
    
# Generate x values

x = np.linspace(-10, 10, points)

# Functions
y1= x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

# Create Figure
plt.figure(figsize=(10, 6))

# Plot Functions

plt.plot(x, y1, label= "y = x", linestyle = "-")
plt.plot(x, y2, label= "y = x^2", linestyle= "--")
plt.plot(x, y3, label="y = sin(x)", linestyle=":")
plt.plot(x, y4, label = "y = e^(-0.1x) cos(x)", marker= ".", markevery=25)

# Labels and formatting

plt.title("Mathematical Function Visualization")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()
plt.grid(True)

# Save Image
plt.savefig("function_plot.png")
print("function_plot.png saved successfully.")

plt.show()

#================================================
# TASK 2 - Own Function
#================================================

print("\n" + "=" * 50)
print("TASK 2 - Own Equation")
print("=" * 50)

# Smooth x values

x2 = np.linspace(-10, 10, 1000)

# Mixed Equation
# Combines cubic growth and wave behavior

y_custom = 0.02 * (x2**3) - 0.5 * (x2**2) + np.sin(2 * x2) + 5

# Create Figure
plt.figure(figsize= (10,6))
plt.plot(x2, y_custom, linewidth = 2, label = "Custom Equation")
plt.title("Custom Mathematical Equation")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()

# Save Image
plt.savefig("own_equation.png")
print("own_equation.png saved successfully.")
plt.show()

#================================================
# TASK 3 - Student Score Visualization
#================================================

print("\n" + "=" * 50)
print("TASK 3 - Student Score Visualization")
print("=" * 50)

# Data Set
students= ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
midterm = [85, 72, 90, 66, 78, 92, 60, 74, 88, 95]
final = [80, 70, 94, 68, 75, 90, 65, 72, 84, 96]

# Dataset Validation
if len(students) != len(midterm) or len(midterm)!= len(final):
    print("Error: Dataset lengths do not match.")
    exit()

# Calculate total scores
total = []
for i in range (len(students)):
    #Score validation
    if midterm[i] < 0 or midterm[i] > 100:
        print(f"Invalid midterm score for {students[i]}")
        exit()
        
    if final[i] < 0 or final[i] > 100:
        print(f"Invalid final score fpr {students[i]}")
        exit()
    
    total_score = 0.4 * midterm[i] + 0.6 * final[i]
    total.append(total_score)
    
#================================================
# A. Scatter Plot
#================================================

plt.figure(figsize=(8, 6))
plt.scatter(midterm, final)
plt.title("Midterm vs Final Scores")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")
plt.grid(True)
plt.savefig("score_scatter.png")
print("score_scatter.png saved successfully.")
plt.show()

#================================================
# B. Histogram
#================================================

plt.figure(figsize=(8,6))
plt.hist(total, bins=5)
plt.title("Distribution of Total Score")
plt.xlabel("Total Score")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("score_histogram.png")
print("score_histogram.png saved successfully.")
plt.show()

#================================================
# C. Bar Chart
#================================================

plt.figure(figsize=(10, 6))
plt.bar(students, total)
plt.title("Student Total Scores")
plt.xlabel("Students")
plt.ylabel("Total Score")
plt.grid(True, axis="y")
plt.savefig("score_bar_chart.png")
print("score_bar_chart.png saved successfully.")
plt.show()

#================================================
# TASK 4 - Best-Fit Line / Prediction
#================================================

print("\n" + "=" * 50)
print("TASK 4 - Best-Fit Line / Prediction")
print("=" * 50)

# Best-Fit Line
slope, intercept = np.polyfit(midterm, final, 1)
# Prediction Line
prediction_line = slope * np.array(midterm) + intercept
# Create Plot
plt.figure(figsize=(8,6))
#Original Data
plt.scatter(midterm, final, label = "Original Data")

# Best-fit line
plt.plot(midterm, prediction_line, linestyle="--", label= "Best-Fit Line")

plt.title("Midterm vs Final Score Prediction")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")
plt.legend()
plt.grid(True)

# Save Image
plt.savefig("score_prediction.png")
print("score_prediction.png saved successfully.")
plt.show()

#================================================
# Prediction Examples
#================================================

prediction_inputs = [50, 75, 100]
print("\nPrediction Examples:")

for score in prediction_inputs:
    predicted_final = slope * score + intercept

    #Keep predictions realistic
    predicted_final = max(0, min(100, predicted_final))
    print(f"Predicted final score for midterm " f"{score}: {predicted_final: .2}")
    
#================================================
# FINAL SUMMARY
#================================================

print("\n" + "=" * 50)
print("All tasks completed successfully.")
print("Generated Files:")
print("- function_plot.png")
print("- own_equation.png")
print("- score_scatter.png")
print("- score_histogram.png")
print("- score_bar_chart.png")
print("- score_prediction.png")
print("=" * 50)