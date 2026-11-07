# Obesity Risk Prediction Using Machine Learning

A machine learning project that analyzes demographic, physical, and lifestyle-related information to predict an individual's obesity category.

> **Note:** This project predicts existing obesity categories using the dataset's labels. It does not predict future obesity risk or provide medical diagnoses.

## Project Overview

Obesity is a major public health concern influenced by several factors, including age, physical characteristics, eating habits, physical activity, and lifestyle choices.

The objective of this project is to apply machine learning techniques to identify patterns in these factors and predict the corresponding obesity category.

The project includes data preprocessing, model training, performance evaluation, model comparison, and an interactive Streamlit dashboard.

## Objectives

- Analyze demographic and lifestyle-related factors associated with obesity categories.
- Clean and preprocess the dataset.
- Train and compare multiple classification algorithms.
- Evaluate models using accuracy, precision, recall, and F1-score.
- Select the best-performing model.
- Develop an interactive web dashboard using Streamlit.

## Dataset Description

The project uses a Kaggle obesity dataset.

| Property | Description |
|---|---|
| Initial records | 2,111 |
| Records after cleaning | 2,087 |
| Input features | 16 |
| Target variable | `NObeyesdad` |
| Number of target classes | 7 |
| Problem type | Multiclass classification |

### Input Features

Gender, Age, Height, Weight, family_history_with_overweight, FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, FAF, TUE, CALC, and MTRANS.

### Target Classes

1. Insufficient Weight
2. Normal Weight
3. Obesity Type I
4. Obesity Type II
5. Obesity Type III
6. Overweight Level I
7. Overweight Level II

## Data Preprocessing

The following steps were performed:

1. Checked dataset structure and data types.
2. Removed duplicate records.
3. Removed records with missing target values.
4. Separated input features and target variable.
5. Split the dataset into training and testing sets using an 80:20 ratio.
6. Used stratified splitting to maintain class distribution.
7. Handled missing numerical values using median imputation.
8. Handled missing categorical values using most-frequent imputation.
9. Applied one-hot encoding to categorical features.

## Machine Learning Algorithms

Four classification algorithms were trained and evaluated:

- Decision Tree Classifier
- Random Forest Classifier
- Logistic Regression
- K-Nearest Neighbors (KNN)

### Evaluation Metrics

- **Accuracy:** Proportion of correct predictions.
- **Precision:** Correctness of positive class predictions.
- **Recall:** Ability to identify actual class instances.
- **F1-score:** Balance between precision and recall.

## Model Performance Comparison

| Algorithm | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Decision Tree | **94.74%** | **94.76%** | **94.74%** | **94.73%** |
| Random Forest | 94.02% | 94.28% | 94.02% | 94.08% |
| Logistic Regression | 89.71% | 89.48% | 89.71% | 89.52% |
| KNN | 83.73% | 83.06% | 83.73% | 82.29% |

### Best Model: Decision Tree Classifier

The Decision Tree Classifier achieved the highest accuracy and F1-score among the four evaluated models.

It was therefore selected as the final model for the Streamlit application.

**Final accuracy: 94.74%**

The test dataset contained 418 records, of which 396 were correctly classified.

## Confusion Matrix

The confusion matrix evaluates the classification performance of the selected Decision Tree model across all seven target categories.

| Actual / Predicted | Insufficient | Normal | Obesity I | Obesity II | Obesity III | Overweight I | Overweight II |
|---|---:|---:|---:|---:|---:|---:|---:|
| Insufficient | 52 | 1 | 0 | 0 | 0 | 0 | 0 |
| Normal | 1 | 54 | 0 | 0 | 0 | 2 | 0 |
| Obesity I | 0 | 0 | 63 | 2 | 0 | 2 | 3 |
| Obesity II | 0 | 0 | 2 | 58 | 0 | 0 | 0 |
| Obesity III | 0 | 0 | 0 | 1 | 64 | 0 | 0 |
| Overweight I | 0 | 3 | 1 | 0 | 0 | 49 | 2 |
| Overweight II | 0 | 0 | 1 | 0 | 0 | 1 | 56 |

## Web Application

An interactive web application was developed using Streamlit.

The dashboard allows users to:

1. Enter demographic information.
2. Provide physical measurements such as height and weight.
3. Enter lifestyle-related information.
4. Submit the information to the trained machine learning model.
5. View the predicted obesity category.

The application uses the saved trained model (`obesity_model.joblib`) to generate predictions.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and preprocessing |
| Jupyter Notebook | Model development |
| Joblib | Saving and loading the trained model |
| Streamlit | Interactive web application |

## Project Structure

```text
obesity-risk-prediction/
│
├── app.py
├── train_model.ipynb
├── obesity_model.joblib
├── requirements.txt
└── README.md
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/Shreya156-bit/obesity-risk-prediction.git
```

### 2. Navigate to the project directory

```bash
cd obesity-risk-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

## Limitations

- The dataset contains existing obesity-category labels rather than future health outcomes.
- Model performance depends on the quality and representativeness of the dataset.
- Predictions should not be considered medical diagnoses.
- Performance on other populations may differ.

## Future Scope

- Explore larger and more diverse datasets.
- Include additional relevant health and lifestyle features.
- Evaluate model performance on independent datasets.
- Improve dashboard design and usability.
- Explore longitudinal datasets for actual future obesity-risk prediction.

## Conclusion

This project demonstrates the application of machine learning classification techniques to obesity-related data.

Four classification algorithms were trained and compared. The Decision Tree Classifier achieved the best test accuracy of **94.74%**.

The selected model was integrated into an interactive Streamlit dashboard, providing a simple interface for entering information and viewing predicted obesity categories.

---

**Project Title:** Obesity Risk Prediction Using Machine Learning  
**Project Type:** Academic Group Project  
**GitHub Repository:** https://github.com/Shreya156-bit/obesity-risk-prediction
