from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/home/ar')
def armsrace():
  return render_template('armsrace.html')

@app.route('/home/de')
def demolition():
  return render_template('de.html')

@app.route('/home/hostage')
def hostage():
  return render_template('hostage.html')

@app.route('/home/bomb')
def bomb():
  return render_template('bomb.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
