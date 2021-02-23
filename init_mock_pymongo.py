import secrets
import time
from bson.json_util import dumps

from database import db_pymongo as db
from domains.models.entities.report_templates import ReportTemplate
from infrastructures.database.models.report_template_model_pymongo import ReportTemplateModel
from manage import app


def create_database() -> None:
    app.app_context().push()  # type: ignore
    db.cx.drop_database("test_db")

    populate_report()
    get_filtered_reports()


def timerfunc(func):
    """
    A timer decorator
    """

    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value

    return function_timer


@timerfunc
def populate_report() -> None:
    foo = ['a', 'b', 'c', 'd', 'e']
    for x in range(10000):
        ReportTemplateModel.add_report_template(ReportTemplate(
            type="node",
            name=secrets.choice(foo),
            sub_sections=[
                {
                    "index": 1,
                    "type": "node",
                    "name": "Patient Information",
                    "sub_sections": [
                        {
                            "type": "leaf",
                            "name": "ID",
                            "data_type": "text"
                        }
                    ]
                },
                {
                    "index": 2,
                    "type": "node",
                    "name": "Biometry",
                    "sub_sections": [
                        {
                            "type": "leaf",
                            "name": "ID",
                            "data_type": "text"
                        }
                    ]
                },
            ], )
        )


@timerfunc
def get_filtered_reports() -> None:
    templates = db.db.report_template_model.find({"name": "a"})
    result = dumps(list(templates))


if __name__ == '__main__':
    create_database()
