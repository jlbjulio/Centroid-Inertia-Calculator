# Final Project – Analisis de datos y toma de decisiones


**Data Analysis of UR3 CobotOps**

This project focuses on clustering analysis of the UR3 CobotOps dataset. The dataset includes multidimensional time series data from the UR3 cobot, providing information on operational parameters and failures for machine learning in robotics and automation.

The project employs clustering techniques to analyze the UR3 CobotOps dataset. The main methodology includes:

- Data preprocessing: handling missing values, data normalization, and encoding categorical variables.
- Clustering: applying various clustering algorithms to identify patterns and anomalies.
- Visualization: creating visualizations to interpret clustering results.

The parameters in the UR3 CobotOps dataset are directly related to the cobot’s operation and performance.

1. **Electrical Currents**:
   - Indicate the energy consumption of the motors at each joint.
   - Can help detect irregularities or inefficiencies in movement.

2. **Temperatures**:
   - Monitor the thermal condition of motors and components.
   - Crucial to prevent overheating and ensure optimal performance.

3. **Joint Speeds (J0–J5)**:
   - Represent the movement of each of the six joints.
   - Important for analyzing movement patterns and efficiency.

4. **Gripper Current**:
   - Related to the energy used by the end-effector (gripper).
   - Can indicate gripping force and interaction with objects.

5. **Operation Cycle Count**:
   - Records how many times the cobot has performed its programmed tasks.
   - Useful for scheduling maintenance and analyzing life cycle.

6. **Protective Stops**:
   - Log when safety features of the cobot are activated.
   - Critical to ensure safe operation around humans.

7. **Grip Losses**:
   - Indicate instances when the gripper failed to hold an object.
   - Important for quality control and task success rate analysis.

These parameters collectively provide a comprehensive view of the cobot’s operational status, performance, and potential issues. They are crucial for:
- Performance optimization  
- Predictive maintenance  
- Safety monitoring  
- Quality control in industrial processes  

---

### Temperatures J0, J1, J2, J3, J4, J5:

- These are the temperatures of each of the six joints of the cobot.
- J0 to J5 represent the six robot joints, from the base to the end-effector.
- Measuring the temperature of each joint is crucial to detect overheating and prevent damage.

### Speed J0, J1, J2, J3, J4, J5:

- These are the rotational speeds of each joint.
- Indicate how fast each joint is moving at a given time.
- Important for analyzing motion dynamics and operational efficiency.

### Current J0, J1, J2, J3, J4, J5:

- Refers to the electrical current consumed by each joint’s motor.
- Provides insight into how much effort each motor is exerting.
- Useful for detecting anomalies in energy consumption or potential mechanical faults.

---

### In the UR3 cobot, typically:

- J0: Rotating base  
- J1: "Shoulder" – first main joint  
- J2: "Elbow" – second main joint  
- J3: First "wrist" joint  
- J4: Second "wrist" joint – usually allows rotation  
- J5: Third "wrist" joint – typically allows final effector rotation  

---

## Clustering Graphs (K-Means, Hierarchical, and DBSCAN)

- **X-axis**: PCA Component 1  
- **Y-axis**: PCA Component 2  

**Interpretation**: These values do not represent "better" or "worse" outcomes. They are simply coordinates in a 2D space that represent the two main features extracted from the original data. Points that are closer together in this space are more similar in the original dataset.

---

## Elbow Method Plot

- **X-axis**: Number of clusters  
- **Y-axis**: SSE (Sum of Squared Errors)  

**Interpretation**: Lower SSE values are generally better, as they indicate lower variation within clusters. However, the goal is to find an "elbow" in the curve, where increasing the number of clusters no longer significantly reduces SSE. This inflection point suggests the optimal number of clusters.

---

## DBSCAN K-Distance Graph

- **X-axis**: Data points ordered by distance  
- **Y-axis**: Epsilon (distance)  

**Interpretation**: There is no "best" value here. The goal is to identify a "knee" in the curve, similar to the elbow method. This knee suggests a good value for the epsilon parameter in DBSCAN, which defines the maximum distance between two samples for them to be considered neighbors.

---

## Time Series Plot

- **X-axis**: Index (time)  
- **Y-axis**: Variable value (temperature or current)  

**Interpretation**:  
- For **temperatures**: Lower values are generally better, as high temperatures may indicate overheating or inefficiency.  
- For **currents**: Interpretation depends on the robot's context. Consistent values within the expected range are typically better. Peaks or very high values may indicate an issue.
