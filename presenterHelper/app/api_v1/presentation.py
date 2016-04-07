__author__ = 'farzin'

from . import api
from . import app
from flask import jsonify, request,g
import json as js
import os
from ..decorators import json

@api.route('/get_presentation/<int:id>', methods=['GET'])
@json
def get_presentation(id):
    try:
        if(g.user):
            dir = os.path.join(app.config['DATA_DIR'], "user_"+str(g.user))
            file = open(dir+"/presentation_"+str(id))
            presentation = js.load(file)
            return presentation
        else:
            return jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'please send your authentication token'})
    except IOError:
        return {"error":"the presentation not found"},404