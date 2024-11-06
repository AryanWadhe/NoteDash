from flask import Flask, render_template, request
import json

app = Flask(__name__)

notes = []


if __name__ == '__main__':
    app.run(debug=True)