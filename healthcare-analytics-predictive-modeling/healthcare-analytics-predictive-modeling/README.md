# 🏥 Healthcare Analytics & Predictive Modeling (Offline)

End-to-end data analyst + data scientist project using a synthetic heart-disease style dataset.

## Highlights
- **EDA & Insights**: demographics, risk factor trends, correlations
- **Models**: Logistic Regression, Random Forest, Gradient Boosting (auto-selects best by ROC-AUC)
- **Explainability**: permutation feature importance
- **App**: Streamlit risk predictor using the saved best model
- **Artifacts**: model `.joblib`, ROC curve, feature-importance CSV/PNG

## Run locally
```bash
pip install -r requirements.txt
jupyter notebook notebooks/healthcare_modeling.ipynb
streamlit run app/streamlit_app.py
```
