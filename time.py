from flask import Flask, Response, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mainpage():
    name = ''
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hello = ''
    if request.method == 'POST':
       name = request.form['name']
       hello = 'Hello! ' + name + '<BR /> Current time is ' + str(now) 
    header = '<html><head><title>Time now</title></head><body>'
    body = '''<form method="POST">
              Your name: <input type="text" name="name" value="{0}">
              <input type="submit" value="submit">
              </form>
	      <p>{1}</p>
              <p>This is version 1.1</p>
              '''.format(name, hello)
    footer = '</body></html>'
    return header + body + footer


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

