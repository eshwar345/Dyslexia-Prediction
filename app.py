

from flask import Flask, render_template,request,redirect,url_for
import pandas as pd
import pickle as pkl
import os
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


app = Flask(__name__)

with open('model1.pkl','rb') as file:
    model=pkl.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline =pkl.load(file)





@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        email=request.form['username']
        pswd=request.form['password']
        if email=='admin' and pswd=='admin':
            return render_template('input.html')
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    return redirect(url_for('home'))



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/input_excel')
def input_excel():
    return render_template('input_excel.html')

@app.route('/result', methods=['POST'])
def result():
    
    gender = request.form['gender']
    native = request.form['native']
    other = request.form['other']
    age = request.form['age']
    
    input_values = [gender, native, other, age]  
    for i in range(1, 33):  
        clicks = request.form.get(f'clicks{i}')
        hits = request.form.get(f'hits{i}')
        misses = request.form.get(f'misses{i}')
        score = request.form.get(f'score{i}')
        accuracy = request.form.get(f'accuracy{i}')
        missrate = request.form.get(f'missrate{i}')
        if clicks and hits and misses and score and accuracy and missrate:
            input_values.extend([clicks, hits, misses, score, accuracy, missrate])
    
    print(input_values)
    data=[input_values]
    data=pipeline.transform(data)
    res=model.predict(data)
    print(res[0])
    return render_template('result.html',data=res[0])


@app.route('/result2', methods=['POST'])
def result2():
    file = request.files.get('file')

    if not file:
        return "No file uploaded. Please upload an Excel or CSV file.", 400
    
    file_extension = os.path.splitext(file.filename)[1].lower()
    try:
        if file_extension in ['.xlsx', '.xls']:
            
            df = pd.read_excel(file)
        elif file_extension == '.csv':
            df = pd.read_csv(file, sep=r'[;,]', engine='python')  # Automatically detects separator
        else:
            return "Unsupported file format. Please upload an Excel or CSV file.", 400

        if df.empty:
            return "Uploaded file is empty. Please upload a valid file.", 400
        
        print("DataFrame Content:\n", df)
        
        
        data = df.values 
        d=np.array(data[0][:-1]).reshape(1,-1)
        X_test_processed = pipeline.transform(d)
        res = model.predict(X_test_processed)  
        return render_template("result.html", data=res)
        
    except Exception as e:
        return f"An error occurred while processing the file: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
