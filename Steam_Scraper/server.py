from flask import Flask, render_template, request
import os
import subprocess


template_dir = os.path.abspath(os.getcwd() + '/')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
 projectpath = request.form['projectFilepath']
 with open("filename", "w") as file:
    file.write(projectpath)
 subprocess.call(['python3', os.getcwd() +'/game_scrapper.py'])
 return (projectpath + '\n Web Scrapping Done')

@app.route('/run.py')
def my_link():
  print ('I got clicked!')
  subprocess.call(['python3', os.getcwd() +'/run.py'])
  import codecs
  f=codecs.open("sentiment.html", 'r')
  return f
if __name__ == '__main__':
  app.run()
