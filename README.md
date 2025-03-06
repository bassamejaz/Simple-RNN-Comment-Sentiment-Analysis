### **Simple RNN IMDB Movie Review Sentiment Analysis**  

This project is a **sentiment analysis** application that classifies IMDB movie reviews as **positive** or **negative** using a **Recurrent Neural Network (RNN)**. The model is built with **TensorFlow/Keras** and deployed using **Streamlit** for an interactive web application.

---

## 🚀 **Features**  

- Loads a **pre-trained RNN model** for sentiment classification.  
- Uses the **IMDB dataset** for word encoding and preprocessing.  
- Provides a **simple and interactive UI** using Streamlit.  
- Accepts user-input movie reviews and predicts the **sentiment (Positive/Negative)** with a probability score.  

---

## 🛠 **Installation & Setup**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/bassamejaz/Simple-RNN-Comment-Sentiment-Analysis.git
cd Simple-RNN-Comment-Sentiment-Analysis
```

### **2. Install Dependencies**  
Make sure you have **Python 3.7+** installed. Then, install the required libraries:  

```bash
pip install tensorflow streamlit
```

---

## 📌 **How to Run the App**  

```bash
streamlit run app.py
```

This will open the application in your browser.

---

## 🏗 **Project Structure**  

```
📂 Simple-RNN-Comment-Sentiment-Analysis
│── simple_rnn_imdb.h5   # Pre-trained sentiment analysis model
│── app.py               # Main Streamlit app
│── embedding.ipynb      # To create embeddings
│── simplernn.ipynb      # Model training
│── README.md            # Project documentation
└── requirements.txt      # List of dependencies (optional)
```

---

## 🔍 **How It Works**  

1. **Preprocessing:**
   - Tokenizes and encodes words using the IMDB dataset word index.
   - Pads sequences to ensure uniform input size for the model.

2. **Prediction:**
   - The RNN model predicts a probability score.
   - If the probability is **> 0.5**, the sentiment is classified as **Positive**; otherwise, it's **Negative**.

3. **Streamlit UI:**
   - Users can enter a movie review in the text box.
   - The app displays the predicted **sentiment** and its probability.

---

## 🖥 **Example Usage**  

### **Input:**  
> "The movie was fantastic! The storyline and acting were amazing."

### **Output:**  
✅ **Sentiment: Positive**  
📊 **Probability: 0.92**  

---

## 📌 **Future Improvements**  

- Add a **bar chart** to visualize probability distribution.  
- Support for **multiple languages** using translation APIs.  
- Deploy the model on **Hugging Face Spaces** or **Heroku**.  

---

## 🤝 **Contributing**  

Feel free to contribute by **reporting issues**, **suggesting improvements**, or **submitting pull requests**!  

---

## 📜 **License**  

This project is **MIT Licensed** – you can use, modify, and distribute it freely.  

---

### **📢 Connect With Me**  

🔗 GitHub: [github.com/bassamejaz](https://github.com/bassamejaz)  
📧 Email: [bassamejaz@gmail.com](bassamejaz@gmail.com) 
