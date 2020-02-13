from flask_api import FlaskAPI
from flask import request

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = FlaskAPI(__name__)

@app.route('/setupForwardEmail', methods=['POST'])
def setupForwardEmail():
    """
    API for setting up forwarding gmail and verify it.
    """
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        return 'success'
    except Exception as ex:
        exceptStr = "Exception {0}".format(ex)
        print(exceptStr)
        return exceptStr

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)