

Disable MD

Edit File

Split Edit

Preview Edit








Change to GitHub Flavored Markdown
Outline
x
Heart Disease Cleveland
Data Card 설명
About Dataset
Context
Variable to be predicted
Acknowledgements
Dataset Notebooks
Related Nootbooks
Heart Disease Cleveland#
url: https://www.kaggle.com/datasets/ritwikb3/heart-disease-cleveland/data

Data Card 설명#
1777859114047

About Dataset#
Context#
The dataset is the Cleveland Heart Disease dataset taken from the UCI repository. The dataset consists of 303 individuals’ data. There are 14 columns in the dataset(which have been extracted from a larger set of 75). No missing values. The classification task is to predict whether an individual is suffering from heart disease or not. (0: absence, 1: presence)

original data: https://archive.ics.uci.edu/ml/datasets/Heart+Disease

Content
This database contains 13 attributes and a target variable. It has 8 nominal values and 5 numeric values. The detailed description of all these features are as follows:

1.  Age: Patients Age in years (Numeric)
2.  Sex: Gender (Male : 1; Female : 0) (Nominal)
3.  cp: Type of chest pain experienced by patient. This term categorized into 4 category.
0 typical angina, 1 atypical angina, 2 non- anginal pain, 3 asymptomatic (Nominal)
4.  trestbps: patient's level of blood pressure at resting mode in mm/HG (Numerical)
5.  chol: Serum cholesterol in mg/dl (Numeric)
6.  fbs: Blood sugar levels on fasting > 120 mg/dl represents as 1 in case of true and 0 as false (Nominal)
7.  restecg: Result of electrocardiogram while at rest are represented in 3 distinct values
0 : Normal 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of >
0.05 mV) 2: showing probable or definite left ventricular hypertrophyby Estes' criteria (Nominal)
8.  thalach: Maximum heart rate achieved (Numeric)
9.  exang: Angina induced by exercise 0 depicting NO 1 depicting Yes (Nominal)
10. oldpeak: Exercise induced ST-depression in relative with the state of rest (Numeric)
11. slope: ST segment measured in terms of slope during peak exercise
0: up sloping; 1: flat; 2: down sloping(Nominal)
12. ca: The number of major vessels (0–3)(nominal)
13. thal: A blood disorder called thalassemia
0: NULL 1: normal blood flow 2: fixed defect (no blood flow in some part of the heart) 3: reversible defect (a blood flow is observed but it is not normal(nominal)
14. target: It is the target variable which we have to predict 1 means patient is suffering from heart disease and 0 means patient is normal.
Variable to be predicted#
Absence (1) or presence (2) of heart disease

Cost Matrix

abse pres
absence 0 1
presence 50

where the rows represent the true values and the columns the predicted.

No missing values.

303 observations

Acknowledgements#
Creators:

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
Donor:
David W. Aha (aha ‘@’ ics.uci.edu) (714) 856-8779

similar dataset : https://www.kaggle.com/datasets/ritwikb3/heart-disease-statlog

Dataset Notebooks#
You can download and use any jypyter notebook from Dataset Notebooks Library

Related Nootbooks#
1777858839868

75 lines · 473 words · 3369 chars · ~3 min read
