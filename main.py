import tkinter as tk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data (list)
texts = [
    "Win money now",
    "Limited offer just for you",
    "Hello how are you",
    "Let's meet tomorrow",
    "Congratulations you won a prize",
    "Are you coming to class"
]

labels = [1, 1, 0, 0, 1, 0]

# Model training
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# Function to check spam
def check_spam():
    msg = entry.get()
    msg_vec = vectorizer.transform([msg])
    prediction = model.predict(msg_vec)

    if prediction[0] == 1:
        result_label.config(text="🚨 Spam", fg="red")
    else:
        result_label.config(text="✅ Not Spam", fg="green")

# GUI window
root = tk.Tk()
root.title("Spam Email Classifier")
root.geometry("400x250")

# Title
title = tk.Label(root, text="Spam Email Classifier", font=("Arial", 16))
title.pack(pady=10)

# Input box
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Button
check_button = tk.Button(root, text="Check", command=check_spam)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run app
root.mainloop()
