from src.api.app import app
from src.api.utils.helpers import  token_required


@app.route('/test', methods=['GET'])
@token_required
def test():
    return "Authorized"


@app.route('/notest', methods=['GET'])
def notest():
    return "No need off Authorization"