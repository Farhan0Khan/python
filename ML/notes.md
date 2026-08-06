# 📘 Machine Learning Revision Notes (Complete Beginner → Interview Ready)

> 🎯 **Goal:** Understand the complete Machine Learning workflow from data to prediction.

---

# 🧠 What is Machine Learning?

> **Machine Learning (ML)** is a branch of Artificial Intelligence (AI) where computers learn patterns from data instead of being explicitly programmed.

### Traditional Programming

```text
Rules + Data
      │
      ▼
Program
      │
      ▼
 Output
```

Example

```
Rules:
if marks > 40 → Pass
else → Fail

Input: 75

Output: Pass
```

---

### Machine Learning

```text
Data + Correct Answers
         │
         ▼
Machine Learning Algorithm
         │
         ▼
Trained Model
         │
         ▼
Predictions on New Data
```

Example

```
Thousands of House Prices
        │
        ▼
ML Algorithm learns pattern
        │
        ▼
Predict price of new house
```

---

# 🤖 Types of Machine Learning Systems

Machine Learning is mainly divided into four categories.

```text
                    Machine Learning
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
     ▼                     ▼                     ▼
Supervised          Unsupervised       Reinforcement
Learning             Learning            Learning
                           │
                           ▼
                    Generative AI
```

---

# 1️⃣ Supervised Learning

## Definition

The model learns using **input data** and **correct output labels**.

Teacher already knows the answers.

```text
Input (X) -------------> Output (Y)

House Features -------> House Price

Student Hours --------> Marks

Weather Data ---------> Rain?
```

---

## Supervised Learning Workflow

```text
Collect Data
      │
      ▼
Label Data
      │
      ▼
Train Model
      │
      ▼
Evaluate Model
      │
      ▼
Deploy
      │
      ▼
Predict New Data
```

---

## Two Types of Supervised Learning

```text
Supervised Learning
       │
 ┌─────┴─────┐
 │           │
 ▼           ▼
Regression  Classification
```

---

# 📈 Regression

Regression predicts **continuous numerical values**.

Examples

✅ House Price

```
₹12,50,000
₹28,30,000
₹45,10,000
```

✅ Weather Temperature

```
31.5°C
28°C
17°C
```

✅ Salary Prediction

```
₹5,20,000/year
```

---

### Regression Examples

| Input | Output |
|--------|---------|
| House Size | House Price |
| Years of Experience | Salary |
| Weather Data | Temperature |
| Age | Weight |
| Advertising Cost | Sales |

---

### Regression Visualization

```text
Price
 ^
 |
 |                         ●
 |                     ●
 |                 ●
 |             ●
 |         ●
 |     ●
 | ●
 +------------------------------>
        House Size
```

Regression predicts a continuous line.

---

# 🏷 Classification

Classification predicts **categories**.

Instead of numbers,
it predicts labels.

Example

```
Spam
Not Spam
```

---

## Types of Classification

```text
Classification
       │
 ┌─────┴────────┐
 │              │
 ▼              ▼
Binary      Multi-Class
```

---

# Binary Classification

Only **2 classes**.

Examples

```
Yes / No

True / False

Spam / Not Spam

Cancer / No Cancer

Fraud / Genuine
```

Diagram

```text
Input
  │
  ▼
Classifier
  │
  ▼
Yes OR No
```

---

# Multi-Class Classification

More than two classes.

Examples

```
Cat

Dog

Horse

Cow

Elephant
```

Another Example

```
Digit Recognition

0
1
2
3
...
9
```

Diagram

```text
           Image
             │
             ▼
       ML Classifier
             │
      ┌──────┼──────┐
      ▼      ▼      ▼
     Cat    Dog    Horse
```

---

# 🎯 Supervised Learning Summary

| Problem | Output |
|----------|---------|
| Regression | Continuous Number |
| Classification | Category |

---

# 2️⃣ Unsupervised Learning

## Definition

The data has **NO labels**.

The computer must discover patterns itself.

```text
Input Data
     │
     ▼
ML Algorithm
     │
     ▼
Hidden Patterns
```

---

Example

Customer shopping history

```
Milk
Bread
Eggs

Milk
Bread

Phone
Laptop

Laptop
Mouse
```

Model automatically groups similar customers.

---

## Common Tasks

### Clustering

Grouping similar objects.

```text
Customers

😀😀😀

🙂🙂🙂

😎😎😎
```

---

### Dimensionality Reduction

Compresses data while keeping important information.

Example

```
100 Features

↓

20 Important Features
```

---

### Association Rule Learning

Finding relationships.

Example

```
People buying

Bread

↓

also buy

Butter
```

---

# Examples

Netflix Movie Recommendation

Customer Segmentation

Market Basket Analysis

Anomaly Detection

Image Compression

---

# 3️⃣ Reinforcement Learning (RL)

Definition

The model learns by interacting with an environment.

It receives

✅ Reward

or

❌ Penalty

---

Diagram

```text
          Reward
             ▲
             │
Environment ◄──────── Agent
      ▲                 │
      │                 ▼
      └──── Action ─────┘
```

---

Example

Robot Walking

```
Step Correct

Reward +10

Falls

Penalty -10
```

---

Game Example

```text
Move

↓

Win

Reward +100

Lose

Penalty -100
```

---

Applications

🎮 Games

🤖 Robotics

🚗 Self Driving Cars

📈 Trading Bots

---

# 4️⃣ Generative AI (GenAI)

Definition

Generative AI creates **new content**.

Instead of only predicting,

it generates.

---

Examples

Input

```
Write a poem
```

Output

```
AI writes poem
```

---

Input

```
Generate image of a tiger
```

Output

🖼 AI Image

---

Input

```
Write Python Code
```

Output

```python
print("Hello World")
```

---

Applications

✍️ Text Generation

🖼 Image Generation

🎵 Music Generation

🎬 Video Generation

💻 Code Generation

---

Examples

ChatGPT

Gemini

Claude

GitHub Copilot

Midjourney

DALL·E

Stable Diffusion

---

# Comparison of ML Types

| Feature | Supervised | Unsupervised | Reinforcement | GenAI |
|----------|------------|--------------|---------------|--------|
| Labels | ✅ Yes | ❌ No | Reward | Large Datasets |
| Goal | Predict | Find Patterns | Max Reward | Generate Content |
| Output | Numbers/Categories | Clusters | Best Actions | New Content |

---

# Complete Supervised Learning Pipeline

```text
Raw Data
    │
    ▼
Dataset
    │
    ▼
Preprocessing
    │
    ▼
Training
    │
    ▼
Model
    │
    ▼
Evaluation
    │
    ▼
Inference
```

---

# 📂 Data

Data is the raw information used to train ML models.

Examples

```
Images

Text

Audio

Video

CSV Files

Excel Files

Database Records
```

Example

| House Size | Bedrooms | Price |
|-------------|----------|--------|
|1000|2|20L|
|1200|3|28L|
|1500|3|35L|

---

# 📚 Dataset

A dataset is a collection of many data samples.

```text
Dataset

Row 1

Row 2

Row 3

...

Row N
```

---

## Dataset Terminology

### Sample

One row.

```
House Size = 1200

Bedrooms = 3

Price = 28L
```

---

### Feature

Input variable.

```
Age

Height

Weight

Bedrooms

Temperature
```

---

### Target (Label)

Desired output.

```
Price

Pass/Fail

Spam

Temperature
```

---

Visualization

```text
Features -----------> Target

X ------------------> Y
```

---

# Dataset Characteristics

## Number of Samples

```
100 rows

1000 rows

1 Million rows
```

More samples usually improve learning.

---

## Number of Features

```
Age

Height

Salary

Gender

City

Experience
```

Each column is a feature.

---

## Data Quality

Good Data

✅ Complete

✅ Accurate

✅ Consistent

Bad Data

❌ Missing Values

❌ Wrong Values

❌ Duplicate Rows

---

## Balanced Dataset

```text
Cats

██████████

Dogs

█████████
```

Good Balance

---

Unbalanced Dataset

```text
Cats

██████████████████

Dogs

██
```

Can produce biased models.

---

## Train-Test Split

```text
Dataset

100%

│

├───────────────┐

▼               ▼

Training      Testing

80%             20%
```

Training learns.

Testing checks performance.

---

# 🤖 Model

A model is the learned mathematical representation of patterns in data.

```text
Training Data

↓

Learning

↓

Model

↓

Predictions
```

Example

House Price Model

```
Input

1500 sqft

↓

Model

↓

₹35 Lakhs
```

---

# 🎯 Training

Training means teaching the model.

```text
Data

↓

Algorithm

↓

Model learns patterns

↓

Weights Updated
```

Training repeats many times.

```
Epoch 1

Epoch 2

Epoch 3

...

Epoch N
```

---

# 📊 Evaluating the Model

Evaluation checks how good the model is.

```text
Testing Data

↓

Model

↓

Predictions

↓

Compare with Actual Answer
```

---

Common Metrics

Regression

📌 MAE

📌 MSE

📌 RMSE

📌 R² Score

Classification

📌 Accuracy

📌 Precision

📌 Recall

📌 F1 Score

📌 ROC-AUC

---

Example

Actual

```
₹25L
```

Predicted

```
₹24.5L
```

Small error

✅ Good model

---

Classification Example

Actual

```
Spam
```

Predicted

```
Spam
```

Correct Prediction

---

# 🚀 Inference

Inference means using a trained model on **new unseen data**.

```text
New Data

↓

Trained Model

↓

Prediction
```

Example

Training

```
1000 Houses
```

Inference

```
New House

↓

Predict Price
```

---

# Complete ML Lifecycle

```text
             DATA
              │
              ▼
      Data Collection
              │
              ▼
     Data Cleaning
              │
              ▼
      Dataset Creation
              │
              ▼
      Train-Test Split
              │
              ▼
      Model Selection
              │
              ▼
         Training
              │
              ▼
        Evaluation
              │
      Good? ─────── No
        │             │
       Yes            │
        ▼             │
     Deployment ◄─────┘
        │
        ▼
      Inference
        │
        ▼
   Predictions
```

---

# 📝 Quick Revision Mind Map

```text
                      Machine Learning
                             │
     ┌───────────────────────┼─────────────────────────┐
     │                       │                         │
     ▼                       ▼                         ▼
 Supervised            Unsupervised          Reinforcement
     │                       │                         │
     │                       │                         ▼
     │                  Find Patterns          Reward/Penalty
     │
     ▼
Regression
Continuous Numbers

Classification
│
├── Binary
└── Multi-Class

                ↓

Data
│
Dataset
│
Features + Labels
│
Train/Test Split
│
Training
│
Model
│
Evaluation
│
Inference
│
Prediction
```

---

# 🎯 Interview One-Liners

- ✅ Machine Learning enables computers to learn patterns from data without explicit programming.
- ✅ Supervised learning uses labeled data.
- ✅ Regression predicts continuous numerical values.
- ✅ Classification predicts categorical labels.
- ✅ Binary classification has two classes; multi-class classification has more than two.
- ✅ Unsupervised learning discovers hidden patterns in unlabeled data.
- ✅ Reinforcement learning learns through rewards and penalties.
- ✅ Generative AI creates new content such as text, images, code, audio, and video.
- ✅ A feature is an input variable; a label (target) is the desired output.
- ✅ Training teaches the model using training data.
- ✅ Evaluation measures model performance on unseen test data.
- ✅ Inference is the process of making predictions using a trained model.
- ✅ High-quality, balanced datasets generally produce more reliable models.