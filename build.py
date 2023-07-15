from flask_frozen import Freezer
from server import app
import os

freezer = Freezer(app)

app.config['FREEZER_DESTINATION'] = "./build"

if __name__ == '__main__':
    freezer.freeze()
