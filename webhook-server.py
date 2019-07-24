#!flask/bin/python
#!/usr/bin/env python3
import six
from flask import Flask, request
from flask_json import json_response
from model import Dao
import logging

app = Flask(__name__, static_url_path="")


log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

app = Flask(__name__)
app.config['JSON_ADD_STATUS'] = True
app.config['JSON_STATUS_FIELD_NAME'] = 'http_status'


@app.route('/snp/webhooks/<sku>', methods=['GET'])
@app.route('/snp/webhooks', methods=['GET'])
def get_documents(sku=None):
    if sku is None:
        dao = Dao()
        result = dao.find_document()
        elemcount = len(result)
        #result.append({'count':elemcount})
        if result is not None:
            return json_response(documents=result,count=elemcount)
        else:
            return json_response(http_status=500, message='Some errors occurred in the process')
    else:
        dao = Dao()
        try:
            #sku = int(sku)
            result = dao.find_document(sku)
            elemcount = len(result)
            if result is not None:
                return json_response(document=result,count=elemcount)
            else:
                return json_response(http_status=500, message='Some errors occurred in the process')
        except Exception:
            return json_response(http_status=422, message="Invalid parameter")


@app.route('/snp/webhooks', methods=['POST'])
def post_document():
    if request.method == 'POST':
        json = request.get_json()
        dao = Dao()
        try:
            if dao.insert_document(json):
                return json_response(http_status=201, message='Record inserted successfully')
            else:
                return json_response(http_status=500, message='Some errors occurred in the process')
        except Exception:
            return json_response(http_status=422, message='Some errors occurred in the process')


@app.route('/snp/webhooks/<sku>', methods=['DELETE'])
def delete_document_by_sku(sku):
    if request.method == 'DELETE':
        dao = Dao()
        try:
            if dao.delete_document(sku):
                return json_response(http_status=202, message='Record deleted successfully.')
            else:
                return json_response(http_status=500, message='Some errors occurred in the process.')
        except Exception:
            return json_response(http_status=422, message='Invalid parameter to delete.')

@app.route('/snp/webhooks', methods=['DELETE'])
def delete_document_by_cuid():
    cuid=request.args.get('cuid')
    if request.method == 'DELETE':
        dao = Dao()
        try:
            if dao.delete_document_cuid(cuid):
                return json_response(http_status=202, message='Record deleted successfully.')
            else:
                return json_response(http_status=500, message='Some errors occurred in the process.')
        except Exception:
            return json_response(http_status=422, message='Invalid parameter to delete.')



@app.errorhandler(404)
def error_404(e):
    return json_response(http_status=404, message='Unknown URL')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
