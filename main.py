### Integrate HTMP With Flask
### HTTP verb GET and POST
### Building Url Dynamically
### Variable Rules and URL Building


##Jinja2 template engine
'''
{%...%} statements,conditions, for loops
{{  }} expressions to print output
{#...#} this is for comments

'''
from flask import Flask,redirect, url_for, render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score, 'res' : res}
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "Person has failed and marks is " + str(score)

##Results checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,score=marks))

##result checker submit HTML Page
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['Science'])
        maths=float(request.form['Maths'])
        C=float(request.form['C'])
        data_science=float(request.form['DataScience'])
        total_score=(science+maths+C+data_science)/4
    res=""
    if total_score>=50:
        res="success"
    else:
        res="fail"
    return redirect(url_for('success',score=total_score))

if __name__=='__main__':
    app.run(debug = True)


