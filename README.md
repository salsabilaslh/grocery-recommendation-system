# Grocery Recommendation System

## Live Demo

[![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?logo=streamlit&logoColor=white)](https://grocery-recommendation-system.streamlit.app/)

---

## Project Overview

This project implements a Grocery Recommendation System using Association Rule Mining and Frequent Itemset Mining techniques.

The objective is to analyze customer grocery purchase transactions and identify products that are frequently purchased together. The discovered association rules are then used to generate personalized product recommendations through an interactive web application.

The data mining workflow was developed using Orange Data Mining, while the user interface was built using Streamlit.

---

## Project Objectives

- Discover hidden purchasing patterns from grocery transaction data
- Generate product recommendations based on association rules
- Measure relationship strength using Lift values
- Provide an interactive recommendation dashboard
- Visualize purchasing patterns and recommendation results

---

## Dataset

The project uses a grocery transaction dataset containing customer purchase records.

Files used:

- `groceries_transaction.csv`
- `association rules.csv`

The transaction data was transformed into a format suitable for association rule mining before being processed in Orange.

---

## Methodology

### 1. Data Preprocessing

The grocery transaction dataset was cleaned and transformed into transaction-based data suitable for market basket analysis.

### 2. Frequent Itemset Mining

Frequent itemsets were extracted to identify combinations of products that appear together frequently.

### 3. Association Rule Mining

Association rules were generated from the frequent itemsets.

Example:

```
Milk → Bread
```

This indicates customers who purchase milk are also likely to purchase bread.

### 4. Lift-Based Ranking

The recommendation strength is evaluated using Lift.

Higher Lift values indicate stronger relationships between products.

---

## Orange Workflow

The Orange Data Mining workflow includes:

- File
- Select Columns
- Rank
- Column Statistics
- Data Table
- Frequent Itemsets
- Association Rules
- Save Data

The generated association rules were exported and used in the Streamlit application.

---

## Streamlit Web Application

Features:

### Product Recommendation

Users can:

- Select one or multiple products
- Generate recommendations
- View recommended products
- Analyze Lift values

### Interactive Dashboard

The application provides:

- Number of products
- Number of association rules
- Average Lift value
- Recommendation visualization

### Data Export

Users can download recommendation results as CSV files.

---

## Visualization

The application includes:

### Recommendation Lift Chart

Displays recommendation strength based on Lift values.

### Purchase Pattern Analysis

Shows the most frequently purchased grocery products.

### Top Association Rules

Displays the strongest association rules discovered from the dataset.

---

## Technologies Used

- Python
- Pandas
- Streamlit
- Matplotlib
- Orange Data Mining

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Project Structure

```text
grocery-recommendation-system/
│
├── app.py
├── association rules.csv
├── groceries_transaction.csv
├── Grocery_Recommendation_System.ows
├── requirements.txt
└── README.md
```
