from flask import Flask, render_template
import sys
application = Flask(__name__)

@application.route('/') # 기본 페이지
def hello():
    # var = request.args.get("폼태그_name 값")
    return render_template("index.html")

if __name__ == "__main__":
    application.run(host='localhost', port=int(sys.argv[1]))

############################################### FAQ ###############################################
# Q1. CSS를 변경하고 새로고침 했더니 변경이 안돼요.
# A1. 캐시가 쌓여서 새로운 내용만 로드하다보니 적용이 안됨. 따라서, 크롬에서 Ctrl + F5(캐시 및 메모리까지 새로고침)을 사용하자.
#
#
###################################################################################################

