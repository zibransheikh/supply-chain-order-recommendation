# 📦 AI-Based Supply Chain Order Recommendation System

This project is an AI-driven supply chain optimization tool that recommends optimal product order quantities using a trained **XGBoost machine learning model**.  
It helps businesses make informed inventory decisions by considering demand, stock levels, lead time, shelf life, supplier constraints, and cost.

---

## 🎯 Problem Statement

In supply chain management, improper inventory planning can lead to:
- Stockouts and lost sales
- Excess inventory and increased holding costs
- Inefficient procurement decisions

This system addresses these issues by predicting the **recommended order quantity** for a product and suggesting the **additional quantity to order** based on real-world constraints.

---

## 🚀 Key Features

- Predicts optimal order quantity using machine learning
- Accepts SKU or product name as input
- Considers:
  - Daily demand
  - Current inventory level
  - Shelf life
  - Supplier lead time
  - Minimum Order Quantity (MOQ)
  - Unit cost
- Automatically fills missing model features using dataset medians
- Calculates total procurement cost
- Command-line based and easy to use

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **XGBoost**
- **Joblib**
- **Regular Expressions (re)**

---

## 📁 Project Structure

supply-chain-order-recommendation/
│
├── predict_order.py # Main script (user input + prediction logic)
├── xgb_model.joblib # Trained XGBoost model
├── supply_chain_dataset.csv # Dataset used for reference and medians
├── README.md # Project documentation
└── .gitignore


---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/zibransheikh/supply-chain-order-recommendation.git
cd supply-chain-order-recommendation

2️⃣ Install required libraries
pip install pandas joblib xgboost

3️⃣ Execute the script
python predict_order.py

🧾 Sample Input
SKU / product_name / sku_label: SKU-1023
Daily demand: 50
Current stock: 200
Shelf life (days): 30
Lead time (days): 7
Supplier minimum order qty (MOQ): 100
Cost per unit: 12

📤 Sample Output
--------------------------
PRODUCT SUMMARY
--------------------------
Product name: Organic Rice 5kg
Recommended order qty: 420.56
Suggested additional order: 221
Total cost for additional order: $2652.00
--------------------------

🧠 System Workflow

1Loads the trained XGBoost model

Reads median values from the dataset for missing features

Maps user inputs to model-required feature names

Predicts recommended inventory level

Applies supplier MOQ constraints

Outputs final order quantity and total cost

📌 Use Cases

Inventory planning and replenishment

Demand-driven procurement

Supply chain optimization

Academic and ML learning projects

🔮 Future Enhancements

Web interface using Streamlit or Flask

REST API integration

Automated model retraining

Visualization dashboard

Cloud deployment

👤 Author

Zibran_Sheikh
B.Tech Computer Science Engineering

⭐ Acknowledgements

This project was developed for academic and learning purposes, focusing on the practical application of machine learning in supply chain management.


