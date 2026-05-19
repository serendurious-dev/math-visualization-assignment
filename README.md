Mathematical Visualization Assignment
 
 ~Student Information

      Course: Open Source Software
      Assignment: Mathematical Visualization Assignment
      Language Used: Python
      Libraries Used: NumPy, Matplotlib
      IDE Used: Visual Studio Code (VS Code)
                      
~Project Description

  This project exhibits the concepts of mathematical visualization and elementary data analysis.
  It utilizes NumPy and Matplotlib to generate all possible graphs and visualizations.

The features in this project include:

     Mathematical function plotting
     Custom equation plotting
     Student score analysis
     Predicting the best-fit line through linear regression

 The program automatically generates image files of all possible plots.

     ~ Libraries Used
       -NumPy
        It is utilized to perform calculations in order to generate numbers, construct arrays, and for calculating the best-fit line using polyfit().
    
     -Matplotlib
     It is employed to create plots such as scatters, histograms and bar-charts and to save all the plots as image files.

 ~ How to Run the Project
   
   Step 1 — Install Required Libraries
   Open terminal in VS Code and run:
   
     pip install numpy matplotlib
   
   Step 2 — Run the Program
   
     python math_visualization.py

 ~ Generated Output Files
 
    These image files would be generated automatically after the program is executed

                | File Name              | Description                               |
                | ---------------------- | ----------------------------------------- |
                |  function_plot.png     | Visualization of 4 mathematical functions |
                |  own_equation.png      | Graph of custom mathematical equation     |
                |  score_scatter.png     | Scatter plot of midterm vs final scores   |
                |  score_histogram.png   | Histogram of total scores                 |
                |  score_bar_chart.png   | Bar chart of student total scores         |
                |  score_prediction.png  | Best-fit prediction graph                 |

 ~ Task Explanation

     - Task 1- Mathematical Function Visualization
           This section visualizes four mathematical functions on a single graph:

                    y = x
                    y = x²
                    y = sin(x)
                    y = e^(-0.1x) cos(x)

            Different line styles, markers, labels, legends, and grids are used to improve readability.
            Improvements:
                    Added validation to check for at least a minimum amount of points
                    Increased figure size appropriately
                    Added several different plot styles
                    Formatted properly

    - Task 2 - Custom Equation Visualization
          Custom equation was created using:

                    Polynomial terms
                    Trigonometric terms

          Equation used:
                    y = 0.02x³ - 0.5x² + sin(2x) + 5
          With this equation we have a smooth curve using both the movement of a wave and a polynomial growth.
          Improvements:
                     Smooth curve using 1000 points
                     Good looking chart with 1000 points
                     Styling improved

    - Task 3 — Student Score Visualization

          A dataset of 10 students was analyzed using different graph types.

          Total Score Formula
                    Total = 0.4 × Midterm + 0.6 × Final

          Graphs Generated
                    Scatter Plot
                    Histogram
                    Bar Chart
          Improvements:
                    Dataset validation
                    Score range validation
                    Improved graph spacing

    - Task 4 — Best-Fit Line Prediction

          Linear regression was implemented using:

                    np.polyfit(midterm, final, 1)

          The graph compares:

                    Original student data
                    Predicted best-fit line

          The program also predicts final scores for:

                    Midterm = 50
                    Midterm = 75
                    Midterm = 100
          Improvements:
                    Prediction value validation
                    Cleaner graph formatting
                    Better visualization

  ~ Why Visualization is important
          Visualization can enhance a user's understanding of numerical and mathematical information. Graphs and charts allow for easy analysis of patterns, correlations and trends as opposed to dealing with just figures alone. For instance:

        Scatter plots allow us to visualize correlations between variables.
        Histograms are used to illustrate score distributions.
        Best-fit lines are used to predict future events.

  ~ Most Useful Visualization
  
      The graph most useful in this project is the Best-Fit Prediction Graph as it shows the trend of Mid-term versus Final score and at the same time it predicts what the upcoming score might be by performing a linear regression. Thus the graph represents both display of data and application of it in prediction.

~ The Use of NumPy and Matplotlib
        
        -NumPy
          NumPy offers mathematical computation as well as a collection of functions for numerical analysis. The following functions among others are valuable:

                    Array manipulation
                    Computation of functions
                    Data generation
                    Linear regression
                    
        -Matplotlib
          Matplotlib is used to graphically represent the data. This includes:

                    plotting functions
                    configuration of the plots
                    labels, legend...
                    Saving figures
                    Included Validations

  ~ Various validations have been implemented in the project to ensure robustness:
  
                Check on the minimum number of points for the prediction
                Checking for a sufficient number of points in the dataset
                Validation of the range of scores for each student
                Adjustment for the prediction range
  ~ Screeshots

          Function Visualization
          <img width="1000" height="600" alt="function_plot" src="https://github.com/user-attachments/assets/f7de35ce-dc09-48d1-abc0-e8457ca244cf" />

          Best-Fit Prediction

          <img width="800" height="600" alt="score_prediction" src="https://github.com/user-attachments/assets/9e20a127-62ea-4f6e-8d53-04bd04ec80b4" />


  ~ Conclusion
  
    In this project, an example has been presented showing the applications of Python in mathematical visualization and elementary data analysis with the help of NumPy and Matplotlib.

    The assignment assisted in gaining better understanding of:
              Plotting of graphs
              Numerical computation
              Data visualization
              Linear regression
              Concepts of Python
