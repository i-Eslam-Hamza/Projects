# 🏡 Boston Housing Price Analysis Project

## 📄 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset Description](#-dataset-description)
- [Project Objectives](#-project-objectives)
- [Key Insights](#-key-insights)
- [Data Analysis & Methodology](#-data-analysis--methodology)
- [Technologies Used](#-technologies-used)
- [Results & Findings](#-results--findings)
- [Conclusions & Recommendations](#-conclusions--recommendations)
- [Acknowledgments](#-acknowledgments)
- [License](#-license)

## 📊 Project Overview
This project analyzes housing prices in Boston using a dataset from the U.S. Census Service. The goal is to provide insights to upper management on factors affecting housing prices, such as proximity to the Charles River, building age, and distance to employment centers.

## 📁 Dataset Description
The dataset has **506 observations** with **13 numerical attributes**:

| Feature Name | Description |
|--------------|-------------|
| CRIM         | Per capita crime rate by town |
| ZN           | Residential land zoned for lots over 25,000 sq.ft. |
| INDUS        | Non-retail business acres per town |
| CHAS         | Charles River (1 if tract bounds river; 0 otherwise) |
| NOX          | Nitric oxides concentration (parts per 10 million) |
| RM           | Average number of rooms per dwelling |
| AGE          | Owner-occupied units built before 1940 |
| DIS          | Weighted distances to five Boston employment centers |
| RAD          | Accessibility to radial highways |
| TAX          | Property-tax rate per $10,000 |
| PTRATIO      | Pupil-teacher ratio by town |
| LSTAT        | % lower status of the population |
| MEDV         | Median value of owner-occupied homes in $1000's |

## 🎯 Project Objectives
1. Is there a significant difference in house prices near the Charles River?
2. Does the age of buildings affect house prices?
3. Is there a relationship between Nitric Oxide levels and industrial areas?
4. Impact of distance to employment centers on home values.

## 🔍 Key Insights
- **Charles River Proximity**: Higher median values for homes near the river.
- **Building Age**: Newer homes generally have higher median values.
- **Industrial Influence**: Strong positive correlation between NOX levels and business acreage.
- **Employment Centers**: Weak positive impact on home values.

## 🛠 Data Analysis & Methodology
- **EDA**: Box plots, scatter plots, and histograms.
- **Statistical Tests**:
  - T-Test, ANOVA, Pearson Correlation, Linear Regression.

## 🛠 Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, SciPy, Plotly)

## 📈 Results & Findings
- **Significant Difference** in house prices based on proximity to the Charles River.
- **Strong Correlation** between NOX levels and industrial acreage.
- **Weak Positive Impact** of employment center proximity on house prices.

## 📌 Conclusions & Recommendations
- **Invest in Charles River Properties**: Higher median values.
- **Prioritize Newer Buildings**: Higher demand for newer constructions.
- **Monitor Industrial Influence**: Impact on desirability due to pollution.

## Code
[ReviewNB for this project](https://app.reviewnb.com/i-Eslam-Hamza/Projects/blob/main/Analyzing%20a%20dataset%20on%20housing%20prices%20derived%20from%20the%20U.S.%20Census%20Service/Analyzing%20a%20dataset%20on%20housing%20prices%20derived%20from%20the%20U.S.%20Census%20Service.ipynb/file/)

## 🙏 Acknowledgments
Thanks to the authors of the **IBM Statistics for Data Science with Python** course for their guidance and the U.S. Census Service for the dataset.

## 📜 License
Licensed under the MIT License. See the [LICENSE](https://github.com/i-Eslam-Hamza/Projects/blob/70dbe20116e73e4b36014a6d9c9e0071af53a291/LICENSE) file for details.


