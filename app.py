#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_rf_v2.pkl', 'rb'))
df_inp_chk =pd.read_csv('pred_output.csv')

@app.route('/')
def home():
    return render_template('fpu.html')

@app.route('/predict',methods=['POST'])
def predict():
    cust_ID = request.form.get('Customer')
    print(cust_ID)
    cust_data = df_inp_chk.query("CustomerID==@cust_ID")["fraud_stats"].iloc[0]
#     int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)

    output = cust_data
    return render_template('fpu.html', prediction_text="The given customer's claim is a {output_pred}".format(output_pred=output))

if __name__ == "__main__":
    app.run(debug=True)



# In[ ]:




