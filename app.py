import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.sav','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = []
    final_features = []
    
    for x in request.form.values():
        int_features.append(x)
    
    if(int_features[0] == 'Male' or int_features[0] == 'male'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[1] == 'Yes' or int_features[1] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[2] == 'Yes' or int_features[2] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[3] == 'Yes' or int_features[3] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[4] == 'Yes' or int_features[4] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[5] == 'Yes' or int_features[5] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[6] == 'Yes' or int_features[6] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[7] == 'Yes' or int_features[7] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[8] == 'Yes' or int_features[8] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[9] == 'Yes' or int_features[9] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[10] == 'Yes' or int_features[10] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[11] == 'Yes' or int_features[11] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
    
    final_features.append(int_features[12])
    final_features.append(int_features[13])
        
    if(int_features[14] == 'Yes' or int_features[14] == 'yes'):
        final_features.append(1)
    else:
        final_features.append(0)
        
    if(int_features[15] == 'Tenure Months_1 - 12'):
        final_features.append(1)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
    elif(int_features[15] == 'Tenure Months_13 - 24'):
        final_features.append(0)
        final_features.append(1)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
    elif(int_features[15] == 'Tenure Months_25 - 36'):
        final_features.append(0)
        final_features.append(0)
        final_features.append(1)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
    elif(int_features[15] == 'Tenure Months_37 - 48'):
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(1)
        final_features.append(0)
        final_features.append(0)
    elif(int_features[15] == 'Tenure Months_49 - 60'):
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(1)
        final_features.append(0)
    else:
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(1)
        
    if(int_features[16] == 'Payment Method_Bank transfer (automatic)'):
       final_features.append(1)
       final_features.append(0)
       final_features.append(0)
       final_features.append(0)
    elif(int_features[16] == 'Payment Method_Credit card (automatic)'):
        final_features.append(0)
        final_features.append(1)
        final_features.append(0)
        final_features.append(0)
    elif(int_features[16] == 'Payment Method_Electronic check'):
        final_features.append(0)
        final_features.append(0)
        final_features.append(1)
        final_features.append(0)
    else:
        final_features.append(0)
        final_features.append(0)
        final_features.append(0)
        final_features.append(1)
        
        
    x_predict = [np.array(final_features)]
    prediction = model.predict(x_predict)

    return render_template('index.html', prediction_text='Churn customer or not {}'.format(prediction))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
