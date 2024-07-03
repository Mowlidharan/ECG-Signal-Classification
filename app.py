# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import joblib 
app = Flask(__name__)

# Load the model
model = joblib.load('/home/mowli/Documents/ECG signal Classification/ECG-Signal-Classification/ecg_pred.pkl')

# Define class labels
class_labels = ['Normal Beats', 'Supraventricular Ectopy Beats', 
                'Ventricular Ectopy Beats', 'Fusion Beats', 'Unclassifiable Beats']

# Get the data from the POST request.
@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data.get('features', []))
    try:
        prediction = model.predict(features)
        predicted_class_index = int(prediction[0]) 
        predicted_class = class_labels[predicted_class_index]
        return jsonify({"prediction": predicted_class})
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {e}"}), 500
if __name__ == '__main__':
    app.run(port=5000, debug=True)



    