# 📝 Algo8.ai: Data Manipulation Assignment (Using Pandas / SQL / Spark)

This assignment performs **transaction-level sales data analysis** and generates reports using **Pandas / SQL / Spark** inside a containerized environment.  

The dataset contains sales transaction records and is used to analyze **SKUs, customers, and sales representative performance**.  
The project also generates **Excel reports for the top-performing sales representatives**.  

---

## 📂 Project Structure

```
.
├── Dockerfile              # Container setup with Ubuntu, Python, uv
├── output/                 # Stores all generated reports
├── resource/               # Contains dataset and assignment instructions
├── src/                    # Source code and scripts for data analysis
└── README.md               # Project documentation
```

---

## 📊 Dataset Description

The dataset contains **transaction-level sales information**. Each row represents a sales entry recorded by a sales representative during a customer visit.  

### Columns:
- `ENTRY_ID` → Unique entry/transaction identifier  
- `SALES_REP_ID` → Unique ID for each sales representative  
- `SALES_REP` → Name of the sales representative  
- `CUSTOMER_ID` → Unique ID for each customer  
- `CUSTOMER_CODE` → Business/system-specific customer code  
- `CUSTOMER_NAME` → Full name of the customer  
- `SKU_NAME` → Product (Stock Keeping Unit) sold  
- `UNIT_SOLD` → Quantity of SKU sold  
- `TOTAL_VALUE_SOLD` → Total value of SKU sold  
- `CHECKIN_TIME` → Start time of customer visit  
- `CHECKOUT_TIME` → End time of customer visit  

---

## 📝 Assignment Tasks

### 1. Top 10 SKUs Analysis
- Top 10 most-selling SKUs  
  - By **Quantity Sold**  
  - By **Value Sold**  
- Top 10 least-selling SKUs  
  - By **Quantity Sold**  
  - By **Value Sold**  

### 2. Customer Analysis
- Top 10 Customers by **Total Value Purchased**  

### 3. Sales Representative Performance
- Top 10 Sales Representatives  
  - By **Value Sold**  
  - By **Time Spent**  
- For Top 10 Sales Reps (by Value):  
  - **Day-wise Average Value Sold**  
  - **Day-wise Average Time Spent**  

### 4. Reports for Top 3 Sales Representatives
- **Day-wise Transactions Sheets** with:  
  - SKU Sold  
  - Price per SKU  
  - Quantity Sold  
  - Value Sold  
- **Summary Report Sheet** with:  
  - Date  
  - Total Quantity Sold  
  - Total Value Sold  
  - Unique SKUs Sold  
  - Unique Customers Served  
  - Number of Visits  
  - Conversion %  
  - Total Time Spent  

---

## 🐳 Running with Docker

This project is containerized using **Docker** with `ubuntu:latest` and **Python3**.  
Dependencies are managed using **uv**.  

### 🔧 Build the Docker Image
```bash
docker build -t sales-analysis .
```

### 🚀 Run the Container
```bash
docker run -it -v /path/to/workspace/assignment:/workspace sales-analysis
```

Here:  
- `-v` maps your **local workspace** to `/workspace` inside the container.  
- All reports will be available in the `/workspace/output` directory.  

---

## ▶️ Usage

Once inside the container, run the following command to generate all reports:

```bash
uv run src/report.py
ur run src/generate_excle.py
```

This will process the dataset from `resource/`, perform the analysis, and save the results in the `output/` folder.  

---

## 📑 Output

The `output/` directory contains:  

1. **CSV Reports**  
   - **Top 10 SKUs Analysis**  
     - Top 10 most-selling SKUs  
       - By Quantity Sold  
       - By Value Sold  
     - Top 10 least-selling SKUs  
       - By Quantity Sold  
       - By Value Sold  
   - **Customer Analysis**  
     - Top 10 Customers by Total Value Purchased  
   - **Sales Representative Performance**  
     - Top 10 Sales Representatives  
       - By Value Sold  
       - By Time Spent  
     - For Top 10 Sales Reps (by Value):  
       - Day-wise Average Value Sold  
       - Day-wise Average Time Spent  

2. **Excel Reports** (for Top 3 Sales Representatives)  
   - **Day-wise transactions**  
   - **Summary report**  

---

## 👨‍💻 Tech Stack
- **Python 3** (Data Processing)  
- **Pandas / SQL / Spark** (Data Analysis)  
- **OpenPyXL** (Excel Report Generation)  
- **Docker** (Environment Management)  
- **uv** (Python dependency manager)  

---

## 📬 Submitted By
**Devashish Roy - 2024PGCSIS08**  
Master of Technology, Information Systems Security Engineering  
NIT Jamshedpur  
