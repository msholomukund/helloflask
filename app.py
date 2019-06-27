from flask import Flask
# from fastai import *
# from fastai.vision import *
# path = Path()
# print(path)
# data = ImageDataBunch.from_folder()
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello, World, this is going to be cool !!"
if __name__ == "__main__" :
    app.run()
#just to test a change

