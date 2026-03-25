# 🚗 Car Price Predictor (Streamlit App)

A simple machine learning web app that predicts the price of a used car based on user inputs like year, distance driven, fuel type, company, and model.

---

## 📌 Features

* Interactive UI built with Streamlit
* Dynamic dropdowns (company → model)
* Machine learning prediction using a trained pipeline
* Clean and simple user experience

---

## 🧠 Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn (Pipeline + ColumnTransformer)
* Pickle (model serialization)

---

## 📂 Project Structure

```
├── app.py               # Streamlit application
├── data.csv             # Dataset
├── linear_model.pkl     # Trained ML pipeline
├── README.md            # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <your-repo-link>
cd <your-folder>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧾 How It Works

1. User selects:

   * Year
   * Distance driven
   * Fuel type
   * Company
   * Model

2. Input is converted into a DataFrame

3. The saved **Pipeline**:

   * Handles preprocessing (encoding + scaling)
   * Predicts price using trained model

4. Result is displayed instantly

---

## ⚠️ Important Notes

* Model expects **same column names as training data**
* Uses `OneHotEncoder(handle_unknown='ignore')` to handle unseen categories
* Pipeline ensures **no data leakage**

---

## 🚀 Future Improvements

* Better UI (cards, styling)
* Add more features (owner type, transmission)
* Deploy on Streamlit Cloud
* Improve model performance

---

## 🙌 Acknowledgment

This project is built as a hands-on implementation of:

* Machine Learning pipelines
* Streamlit app deployment

---

## 📬 Contact

Feel free to reach out if you want to collaborate or improve this project!
