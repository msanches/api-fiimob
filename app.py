#https://medium.com/analytics-vidhya/flask-hello-world-47ca1ccd0d30
#https://stackoverflow.com/questions/41804507/h14-error-in-heroku-no-web-processes-running
#https://medium.com/@speedforcerun/heroku-deploy-no-web-process-running-6f6b4059765d
#Para impedir que o app entre em modo sleep no heroku: http://kaffeine.herokuapp.com/

from flask import Flask, jsonify, render_template
import fii

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')
  
@app.route('/api/<fundo>')
def fundo(fundo):
  dados = fii.fundo(fundo)
  
  response = jsonify(dados)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/api/')
def api():
    dados = fii.scraping()
    response = jsonify(dados)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    #app.run(debug=False)
    app.run(host='0.0.0.0', port=80, debug=False, threaded=True)