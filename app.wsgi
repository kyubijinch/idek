import os
from flask import Flask
from flask_script import Manager
import app

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
