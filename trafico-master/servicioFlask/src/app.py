from flask import Flask
from config import config

#Rutas
from routes import Bus

app = Flask(__name__)

#@app.route("/")
#def hello():
#  return "<h1 style = 'color:blue'>Hello There!</hi>"

def page_not_found(error):
  return "<h1>Not found page</h1>"

if __name__ == "__main__":
  app.config.from_object(config['develoment'])

  #Blueprints(asignar rutas)
  app.register_blueprint(Bus.main,url_prefix='/api/bus')
  
  #app.run(host = '0.0.0.0')

  #Manejador de errores
  app.register_error_handler(404, page_not_found)

  app.run()