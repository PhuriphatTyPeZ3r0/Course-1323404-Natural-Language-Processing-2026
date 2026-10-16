"""
Titanic: Machine Learning from Disaster
Baseline Random Forest Model & Submission Generator
"""

import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

def load_data(data_dir):
    train_path = os.path.join(data_dir, "train.csv")
    test_path = os.path.join(data_dir, "test.csv")
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df

def extract_features(df, is_train=True):
    df = df.copy()
    
    # 1. Extract Title
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace('Mlle', 'Miss')
    df['Title'] = df['Title'].replace('Ms', 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    
    # 2. Family Features
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    # 3. Missing Value Handling
    # Embarked: fill mode
    df['Embarked'] = df['Embarked'].fillna('S')
    
    return df

def preprocess_and_encode(train_df, test_df):
    train_feat = extract_features(train_df, is_train=True)
    test_feat = extract_features(test_df, is_train=False)
    
    # Impute Age based on median within (Pclass, Title)
    age_medians = train_feat.groupby(['Pclass', 'Title'])['Age'].median()
    overall_age_median = train_feat['Age'].median()
    
    def fill_age(row):
        if pd.isna(row['Age']):
            val = age_medians.get((row['Pclass'], row['Title']), overall_age_median)
            return overall_age_median if pd.isna(val) else val
        return row['Age']
    
    train_feat['Age'] = train_feat.apply(fill_age, axis=1)
    test_feat['Age'] = test_feat.apply(fill_age, axis=1)
    
    # Impute Fare in test set with median of Pclass
    fare_medians = train_feat.groupby('Pclass')['Fare'].median()
    overall_fare_median = train_feat['Fare'].median()
    test_feat['Fare'] = test_feat.apply(
        lambda r: fare_medians.get(r['Pclass'], overall_fare_median) if pd.isna(r['Fare']) else r['Fare'],
        axis=1
    )
    
    # Features to select
    categorical_cols = ['Sex', 'Embarked', 'Title']
    numerical_cols = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize', 'IsAlone']
    
    # Combine for consistent one-hot encoding
    combined = pd.concat([train_feat[categorical_cols + numerical_cols], test_feat[categorical_cols + numerical_cols]], axis=0)
    combined_encoded = pd.get_dummies(combined, columns=categorical_cols, drop_first=True, dtype=int)
    
    X_train = combined_encoded.iloc[:len(train_feat)].copy()
    y_train = train_feat['Survived'].astype(int)
    X_test = combined_encoded.iloc[len(train_feat):].copy()
    test_passenger_ids = test_df['PassengerId']
    
    return X_train, y_train, X_test, test_passenger_ids

def train_and_evaluate(X_train, y_train):
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        min_samples_split=4,
        min_samples_leaf=2,
        random_state=42
    )
    
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy')
    
    print(f"5-Fold CV Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
    for i, s in enumerate(scores, 1):
        print(f"  Fold {i}: {s:.4f}")
        
    model.fit(X_train, y_train)
    return model

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    output_path = os.path.join(base_dir, "submission.csv")
    
    print("Loading datasets...")
    train_df, test_df = load_data(data_dir)
    print(f"Train data: {train_df.shape}, Test data: {test_df.shape}")
    
    print("Preprocessing and engineering features...")
    X_train, y_train, X_test, test_ids = preprocess_and_encode(train_df, test_df)
    print(f"Feature matrix shape: {X_train.shape}")
    print("Features:", list(X_train.columns))
    
    print("\nTraining and evaluating Random Forest model...")
    model = train_and_evaluate(X_train, y_train)
    
    print("\nGenerating predictions on test set...")
    predictions = model.predict(X_test)
    
    submission_df = pd.DataFrame({
        "PassengerId": test_ids,
        "Survived": predictions
    })
    
    submission_df.to_csv(output_path, index=False)
    print(f"Submission saved to: {output_path}")
    print(f"Total rows: {len(submission_df)}")
    print(f"Survival distribution in test predictions:\n{submission_df['Survived'].value_counts(normalize=True)}")
    print("\nSample preview:")
    print(submission_df.head(10))

if __name__ == "__main__":
    main()
