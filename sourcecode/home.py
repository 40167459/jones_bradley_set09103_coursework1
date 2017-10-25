from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home') #Redirects to homepage
def home():
  return render_template('home.html') #Renders the appropriate template

@app.route('/home/ar') #Redirect to armsrace page
def armsrace():
  return render_template('armsrace.html') #renders the appropriate template

@app.route('/home/de') #Redirect to demolition page
def demolition():
  return render_template('de.html') #Renders the appropriate template

@app.route('/home/hostage') #Recirect to hostage rescue page
def hostage():
  return render_template('hostage.html') #Renders the appropriate template

@app.route('/home/bomb') # redirect to Bomb Scenario page
def bomb():
  return render_template('bomb.html') #Renders the appropriate template

@app.errorhandler(404) #Redirect to error screen
def page_not_found(error):
  return "Couldn't find the page you request.", 404

@app.route('/home/deathmatch') #redirects to deathmatch page
def deathmatch():
  return render_template('deathmatch.html') #renders the appropriate template

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
