from flask import Blueprint


api = Blueprint("api_1_0", __name__)


from . import users
from . import department
from . import customes

