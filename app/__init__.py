from flask import Flask
app = Flask(__name__)

# 파일 이름이 index.py 이므로...
from app.main.index import main as main

# 위에서 추가한 파일을 연동해주는 역할.
app.register_blueprint(main)