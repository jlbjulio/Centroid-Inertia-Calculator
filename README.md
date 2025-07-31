# Centroid and Moment of Inertia Calculator

This project is a web application designed to calculate the centroid and moment of inertia of systems composed of multiple geometric shapes. It allows the user to add different shapes, define their characteristics, and visualize the results both graphically and numerically.

Link to view the project: [Centroid and Moment of Inertia Calculator](https://jlbjulio.github.io/Centroid-Inertia-Calculator)

## Technologies Used

- HTML  
- CSS  
- JavaScript (no frameworks)  
- Canvas for drawing on the Cartesian plane

## Main Features

- **Selection of basic geometric shapes**:
  - Circle  
  - Semicircle  
  - Quarter circle  
  - Rectangle  
  - Equilateral triangle  
  - Right triangle

- **Customization of parameters**:
  - Dimensions (radius, base, height, etc.)  
  - Position on the X and Y axes  
  - Direction or quadrant (for shapes like semicircles and quarter circles)  
  - Type of shape (solid or hollow)

- **System configuration**:
  - Definition of Cartesian plane boundaries  
  - Choice of axis for moment of inertia calculation (centroid or bottom-left corner)

- **Additional features**:
  - Automatic drawing on the plane, scaled accordingly  
  - Ability to add multiple shapes, delete individual shapes, or clear the entire system  
  - Visualization of the total centroid of the composed system  
  - Calculation of total area, composite centroid, and total moment of inertia with respect to the selected axis

## How to Use

1. Open the `index.html` file in any modern browser.  
2. Set the maximum X and Y values to define the size of the plane.  
3. Select a shape and fill in the required fields.  
4. Click the “Draw Shape” button to add it to the system.  
5. Repeat the process to add more shapes if desired.  
6. Enter the reference point and select the axis for the moment of inertia calculation.  
7. Click “Calculate Centroid and Moment of Inertia” to display the results.

## Considerations

- Units are relative to the system defined by the user.  
- Hollow shapes subtract their contribution from the total centroid and moment of inertia.  
- The Cartesian plane is dynamically generated based on the user-defined X and Y values.

## Possible Improvements

- Add new geometric shapes  
- Enable exporting results to PDF or CSV  
- Improve UI with external libraries  
- Save and load previous configurations

## Author

This repository was developed as part of the **Mecánica** course by **Julio Lara**, from the **Licenciatura en Ingeniería de Sistemas y Computación** career at the **Universidad Tecnológica de Panamá (UTP)**.

---

> **Note**: This project was originally developed in Spanish. The README is written in English for documentation and sharing purposes.

