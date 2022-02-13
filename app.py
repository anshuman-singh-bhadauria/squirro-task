from flask import Flask
from flask_restful import Api, Resource
import os
import pathlib
from db import DB
from summarizer import text_summarizer

app = Flask(__name__)
api=Api(app)

database = DB("database.db")

class SubmitDocument(Resource):

    def post(self, document_text):
        if len(document_text)>0:
            document_id=database.insert(document_text)
            print(document_id)

class GetDocument(Resource):

    def get(self, document_id):
        document=database.fetch(document_id)
        text_summary = text_summarizer(document)
        return {
            "document_id":document_id,
            "summary": text_summary
        }

api.add_resource(SubmitDocument, "/<string:document_text>")
api.add_resource(GetDocument, "/<int:document_id>")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 30003))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
