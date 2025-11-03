# libraies importation
import gradio as gr
import pickle
import pandas as pd

# Load the trained pipeline
pipeline = pickle.load(open("fraud_detection_model.pkl", "rb"))

def predict_fraud(type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest):
    # Prepare input as a DataFrame
    input_df = pd.DataFrame([{
        "type": type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])
    # Predict
    pred = pipeline.predict(input_df)[0]
    return "Fraudulent" if pred == 1 else "Legitimate"

types = ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]

demo = gr.Interface(
    fn=predict_fraud,
    inputs=[
        gr.Dropdown(types, label="Transaction Type"),
        gr.Number(label="Amount ($)"),
        gr.Number(label="Old Balance Origin Bank"),
        gr.Number(label="New Balance Origin Bank"),
        gr.Number(label="Old Balance Destination Bank"),
        gr.Number(label="New Balance Destination Bank"),
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Online Fraud Transaction Detection",
    description="Enter transaction details to predict if it's fraudulent or legitimate."
)
# run the app
if __name__ == "__main__":
    demo.launch()
