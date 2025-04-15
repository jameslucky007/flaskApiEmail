from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app) 
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
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(host='0.0.0.0', debug=True)
