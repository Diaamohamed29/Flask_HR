from flask import Flask, render_template, request , redirect , url_for
from pdf2image import convert_from_path
from time import sleep
app = Flask(__name__)






@app.route('/')
def test():
    return render_template('test.html')




@app.route('/loading')
def loading():

    return render_template('loading.html')


@app.route('/login')
def login():
    return render_template('login.html')




@app.route('/dashboard')
def dashboard():
    active_page = 'dashboard'
    return render_template('index.html',active_page=active_page)




@app.route('/employes')
def employes():
    active_page = 'employes'
    return render_template('employes.html',active_page=active_page)



@app.route('/missions')
def missions():
    active_page = 'missions'
    return render_template('missions.html',active_page=active_page)



@app.route('/attendance')
def attendance():
    active_page = 'attendance'
    return render_template('attendance.html',active_page=active_page)



@app.route('/vacations')
def vacations():
    active_page = 'vacations'
    return render_template('vacations.html',active_page=active_page)



@app.route('/upload-report')
def upload_report():
    return render_template('upload-report.html')


@app.route('/reports')
def reports():
    active_page = 'reports'
    return render_template('reports.html',active_page=active_page)


@app.route('/gaz')
def gaz():
    active_page = 'gaz'
    return render_template('gaz.html',active_page=active_page)


@app.route('/invoice')
def invoice():
    active_page = 'invoice'
    return render_template('invoice.html',active_page=active_page)



if __name__ == '__main__':
    app.run(debug=True)
