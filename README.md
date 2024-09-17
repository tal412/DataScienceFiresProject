Extra files could be found here:

https://drive.google.com/drive/folders/1E_-Ta-2n7AAjbvnPNihClhqBPWo_dfkK?usp=sharing

# Wildfire Cause Prediction Project

This project is focused on predicting the cause of wildfires in the United States using machine learning techniques. The goal is to build a model that can accurately predict the cause of a wildfire, with a focus on minimizing prediction errors based on the AUC-ROC metric.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Description](#data-description)
- [Approach](#approach)
- [Modeling](#modeling)
- [Feature Engineering](#feature-engineering)
- [Results](#results)
- [Future Work](#future-work)
- [Contributors](#contributors)

## Project Overview

Wildfires pose a serious threat to environments and populations, and the ability to predict their cause can help in both prevention and response efforts. This project leverages a dataset containing information about wildfires across the United States, with the aim to build a model that can classify the cause of each fire into categories such as lightning, campfire, arson, and other human-related or natural causes.

## Data Description

The dataset used for this project includes multiple features for each wildfire incident, such as:
- **Geographical Information**: Coordinates (latitude, longitude), state.
- **Temporal Information**: Date and time of discovery and containment.
- **Size**: Estimated size of the fire in acres.
- **Cause**: The known cause of the fire (e.g., lightning, campfire, arson).
- **Environmental Conditions**: Weather conditions such as temperature, precipitation at the time of the fire.
- **Surrounding Features**: Distance from natural reserves, camping sites, population centers, and infrastructure like railroads and powerlines.

## Approach

1. **Data Cleaning & Exploration**: 
   - Initial examination and cleaning of the dataset involved removing unnecessary features (e.g., unique identifiers) and handling missing values.
   - Certain features with a high proportion of missing data, such as `CONT_DATE` and `CONT_TIME`, were removed or imputed with averages where necessary.

2. **Feature Engineering**:
   - Added spatial features such as the distance from the nearest natural park, camping sites, and populated areas.
   - Weather data such as average daily temperature, maximum/minimum temperatures, and precipitation were also integrated from external weather databases.
   - Time-related features, including proximity to holidays, were considered to better capture fire causes like fireworks or campfire-related incidents.
   
3. **Modeling & Evaluation**:
   - Various machine learning models were tested, including:
     - K-Nearest Neighbors (KNN)
     - Random Forest Classifier (RFC)
     - Gradient Boosting Classifier
   - The models were evaluated primarily based on AUC-ROC to optimize classification performance.
   
## Feature Engineering

Significant efforts were made to create features that would enhance the predictive power of the model, including:
- **Spatial Features**: Calculating the distance of each fire to important geographical landmarks like camping areas, population centers, and railroads.
- **Weather Data**: Incorporated historical weather data for each fire event to examine the correlation between environmental factors and fire causes.
- **Temporal Features**: Added time-based features such as the day of the year, proximity to major holidays (e.g., 4th of July), and seasonality.

## Modeling

Several machine learning models were trained and evaluated:
- **Baseline Models**: Initial models such as K-Nearest Neighbors (KNN) and Random Forest were used to set a benchmark.
- **Advanced Models**: Gradient Boosting Classifier was used for improved accuracy.
- **Cross-Validation**: All models were evaluated using k-fold cross-validation to ensure robustness.

### Best Performing Model
- **Random Forest Classifier** with hyperparameter tuning provided the best results, achieving a high AUC-ROC score.
  
## Results

The project successfully identified key factors contributing to wildfire causes, and the models demonstrated good predictive performance. Spatial features like the distance from natural parks and camping areas, as well as temporal and environmental factors, played a significant role in improving the model’s accuracy.

### Key Insights
- **Human-Related Causes**: Fires caused by arson or campfires showed strong correlations with proximity to population centers and camping areas.
- **Natural Causes**: Fires due to lightning were often associated with high precipitation days and areas near natural reserves.
- **Temporal Influence**: Fires caused by fireworks were frequently close to the 4th of July holiday, indicating the effectiveness of incorporating holiday proximity features.

## Future Work

Potential next steps for the project include:
- **Model Improvement**: Fine-tuning the models further and exploring more sophisticated approaches like deep learning.
- **Additional Data Sources**: Integrating more detailed demographic or land-use data to further improve predictions related to human-caused fires.
- **Deployment**: Creating an API for real-time prediction of fire causes based on input data from new wildfire events.


