from app import app

app.run(host="localhost", port=8080, debug=True)

##########################################################################################
# debug=True 파라미터의 의미
#
# 소스 코드 변경시 즉시 refresh되도록 하기 위해서 debug 파라미터값을 True로 설정해줘야함.
#
# Unix 계열 OS의 경우...
# >export FLASK_DEBUG=1
# Window 계열 OS의 경우...
# >set FLASK_DEBUG=1
#
# 그리고 >flask run 명령 실행.
##########################################################################################
