import logging
import os

import inject
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_script import Manager, Server

# from database import db_mongoengine as db
# from database import db_pymongo as db
from database import db_pynamodb as db

from domains.repositories.report_template_repository import IReportTemplateRepository

# from infrastructures.database.models.report_template_model_mongoengine import ReportTemplateModel
# from infrastructures.database.models.report_template_model_pymongo import ReportTemplateModel
from infrastructures.database.models.report_template_model_pynamodb import ReportTemplateModel

from presentation.views.health import health
from presentation.views.report_template import ReportTemplate


class Config:
    DYNAMODB_HOST = "http://localhost:8000"
    DYNAMODB_AWS_ACCESS_KEY_ID = "test"
    DYNAMODB_AWS_SECRET_ACCESS_KEY = "test"
    DYNAMODB_READ_CAPACITY_UNITS = 10
    DYNAMODB_WRITE_CAPACITY_UNITS = 10


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, '.env'))


def di_config(binder: inject.Binder) -> None:
    binder.bind(IReportTemplateRepository, ReportTemplateModel)


app = Flask(__name__)

# TODO: configure CORS
CORS(app)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(health, url_prefix='/health')

app.add_url_rule('/v1/reports/<report_id>', view_func=ReportTemplate.as_view('report'), methods=['GET'])

# mongodb config
# app.config['MONGO_URI'] = "mongodb://localhost:27017/test_db"

# dynamodb config
app.config.from_object(Config)

db.init_app(app)

manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0', port=5000))

# dependency injection
inject.configure(di_config)

if __name__ == "__main__":
    logging.basicConfig()
    manager.run()
