# Features

## Introduction
The art of machine learning is to extract useful features from raw data (or training data). 

We use big X to denote the feature matrix, and the small y to denote the label vector. It is also known as the predictive variable. 

Types of features: Numeric features, Categorical features, Text features (and plenty more of unstructured data). 

When working with structured data, more columns of data isn't always better. It doesn't mean all columns are useful features. There is the issue of Curse of Dimensionality (definition): expoentially exponentially more data is needed to train machine learning models as the number of data attributes increase. On the other hand, more rows of data is a good thing. It means more of real world data is observed and collected. And that's a good thing. More rows of data is always better. More columns of data isn’t necessarily better, especially if irrelevant features are included. We also need to be concerned with correlated columns and data leaks. 

## Feature transformation
Data can be put through a pipeline of transformations, processing to better feed into models, making compute more efficient, and the model performance better etc. These steps could include: converting to tensors, scaling, imputation, and more. 

## Feature engineering
[What is feature engineering (definition)? \[public, flash card, easter egg\]](https://ml.learn-to-code.co/skillView.html?skill=t5LaiwBlRRS9zok5gmdx)

## Feature selection
A series of analysis, even deep learning, canb e performed to decide whether to retain a feature for training. We can look at the contribution of the feature to model performance, check for correlation, redundancy etc. We can find a variety of reasons to keep or remove a feature column. Just because some features are statistically significant doesn’t mean they should be chosen : age, phone # 2, bankruptcy. It may be immoral (or privacy issue, fallacies). source kaggle day. 

On the importance of feature selection : some models are sensitive to noises and outliers such as K Nearest Neighbor (KNN) and linear regression, including invalid or less relevant noisy data points can significantly change the shape, frontier of predicitive modes and even change the final prediction label/value significantly. 

Feature selection can be a boolean True/False, meaning choosing to include a feature or not. Or it can be weighted, account for a fraction of a value of feature contribution. 

### Feature importance
Some models can give us measurements of feature importance, which can be used as a tool to select features in the feature selection process. 
