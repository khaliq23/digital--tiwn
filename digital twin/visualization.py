from flask import render_template

def create_dashboard(data, predictions):
    return render_template('index.html', data=data, predictions=predictions)
