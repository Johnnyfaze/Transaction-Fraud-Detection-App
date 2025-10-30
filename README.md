# Online Fraud Transaction Detection

This project uses a machine learning model to detect fraudulent online transactions. It provides an interactive web interface built with Gradio for easy testing.

## Features

- Predicts if a transaction is **Fraudulent** or **Legitimate**
- User-friendly web UI
- Powered by scikit-learn and pandas

## Getting Started

### 1. Clone the repository or download the files

### 2. Install dependencies

```bash
pip install gradio pandas scikit-learn joblib
```

### 3. Run the app

Make sure `fraud_detection_model.pkl` is in the same directory as `app.py`.

```bash
python app.py
```

Open the link shown in your terminal to access the web interface.

## Usage

Enter transaction details:
- Transaction Type (CASH_IN, CASH_OUT, DEBIT, PAYMENT, TRANSFER)
- Amount
- Old/New Balance (Origin and Destination)

Click **Submit** to see the prediction.

## Deployment

You can deploy this app using:
- [Hugging Face Spaces](https://huggingface.co/spaces)
- Render.com
- PythonAnywhere
- Cloud VM (AWS, Azure, GCP)

## Files

- `app.py`: Gradio web app
- `fraud_detection_model.pkl`: Trained ML model
- `requirements.txt`: List of dependencies

## License

MIT
