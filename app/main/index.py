from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/main', methods=['GET'])
def index():
    testData = 'testData Array'
    # /main/index.html은 사실 /${project_name}/app/template/main/index.html
    return render_template('/main/index.html', testDataHtml=testData)

@main.route('/test', methods=['GET'])
def test():
    return render_template('/main/test.html')