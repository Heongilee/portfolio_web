from flask import Flask, render_template
import sys
application = Flask(__name__)

@application.route('/') # 기본 페이지
def hello():
    # var = request.args.get("폼태그_name 값")
    return render_template("index.html")

if __name__ == "__main__":
    application.run(host='localhost', port=int(sys.argv[1]))