# 💎 Onyx Forecaster: Intelligent Sales Prediction for UMKM

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)

Onyx Forecaster is a lightweight yet powerful time-series forecasting engine designed to help small and medium enterprises (UMKM) optimize their inventory and sales strategy. Built with transparency and ease-of-use in mind, it bridges the gap between complex data science and practical business application.

## 🌟 Key Features
- **Accurate Time-Series Forecasting:** Utilizes ARIMA and Scikit-learn models for robust sales predictions.
- **Business-First API:** Simple REST endpoints to integrate with existing POS or inventory systems.
- **Automated Insights:** Automatically detects seasonality and trends in historical sales data.
- **Lightweight & Fast:** Optimized for performance without requiring heavy GPU infrastructure.

## 🛠️ Technology Stack
- **Core:** Python
- **AI/ML:** Scikit-learn, Pandas, NumPy
- **API:** FastAPI, Uvicorn
- **Utilities:** Pydantic for data validation

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Pip (Python Package Index)

### Installation
1. Clone the repository:
   `ash
   git clone https://github.com/hilmanfauzi21/onyx-forecaster.git
   cd onyx-forecaster
   `
2. Install dependencies:
   `ash
   pip install -r requirements.txt
   `
3. Run the application:
   `ash
   python app.py
   `

## 📊 How It Works
Onyx processes CSV or JSON-based historical sales data. It performs automated feature engineering (extracting day-of-week, month, and seasonality) before training a gradient-boosted regression model to forecast the next 7-30 days of sales.

## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

---
Developed with ❤️ by **Hilman Fauji Abdilah**