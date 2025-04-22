<<<<<<< HEAD
#For API handler (react)

=======
>>>>>>> 2b5e4addcda79bbdadea8aefbf5347084906e99c
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
<<<<<<< HEAD
CORS(app)  # Allows communication between React and Flask

# Load the saved machine learning model and vectorizer
=======
CORS(app) 
>>>>>>> 2b5e4addcda79bbdadea8aefbf5347084906e99c
model = pickle.load(open('logistic_regression.pkl', 'rb'))
feature_extraction = pickle.load(open('feature_extraction.pkl', 'rb'))

@app.route('/')
def home():
    return "Spam Detection API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_text = data.get('mail', '')
        
        if not input_text:
            return jsonify({'error': 'No input provided'}), 400

        input_features = feature_extraction.transform([input_text])
        prediction = model.predict(input_features)[0]
        print('1111',prediction)
        result = 'Not Spam' if prediction == 1 else 'Spam'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
<<<<<<< HEAD
    app.run()





















# for HTML template rendering

# from flask import Flask, render_template, request
# import pickle

# app = Flask(__name__)

# # ======================== Load the saved files ========================
# model = pickle.load(open('logistic_regression.pkl', 'rb'))
# feature_extraction = pickle.load(open('feature_extraction.pkl', 'rb'))

# def predict_mail(input_text):
#     try:
#         input_user_mail = [input_text]
#         input_data_features = feature_extraction.transform(input_user_mail)
#         prediction = model.predict(input_data_features)[0]

#         return "Spam" if prediction == 1 else "Not Spam"
#     except Exception as e:
#         return f"Error: {str(e)}"

# @app.route('/', methods=['GET', 'POST'])
# def analyze_mail():
#     if request.method == 'POST':
#         mail = request.form.get('mail')
#         predicted_mail = predict_mail(input_text=mail)
#         print(predicted_mail)
#         return render_template('index.html', classify=predicted_mail)

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
=======
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(host='0.0.0.0', debug=True)
>>>>>>> 2b5e4addcda79bbdadea8aefbf5347084906e99c
