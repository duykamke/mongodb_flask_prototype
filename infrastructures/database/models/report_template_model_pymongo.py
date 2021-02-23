from pymongo import errors
from bson.objectid import ObjectId

from database import db_pymongo
from domains.models.entities.report_templates import ReportTemplate
from domains.repositories.report_template_repository import IReportTemplateRepository


class ReportTemplateModel(IReportTemplateRepository):

    @classmethod
    def _to_report_template_dict(cls, report: ReportTemplate) -> dict:
        return {'type': report.type, 'name': report.name, 'sub_sections': report.sub_sections}

    @classmethod
    def _to_report_template_object(cls, report: dict) -> ReportTemplate:
        return ReportTemplate(
            id=report['_id'],
            type=report['type'],
            name=report['name'],
            sub_sections=report['sub_sections']
        )

    @classmethod
    def add_report_template(cls, report: ReportTemplate) -> str:
        new_report = cls._to_report_template_dict(report)
        try:
            new_report_id = db_pymongo.db.report_template_model.insert(new_report)
        except errors.DuplicateKeyError:
            raise ValueError("Already exists")
        return new_report_id

    @classmethod
    def get_by_id(cls, id: str) -> ReportTemplate:
        db_report = db_pymongo.db.report_template_model.find_one({'_id': ObjectId(id)})
        if db_report is None:
            raise ValueError("Not found")
        return cls._to_report_template_object(db_report)

    @classmethod
    def update_by_id(cls, id: str, report: ReportTemplate) -> None:
        return None

    @classmethod
    def delete_by_id(cls, id: str) -> None:
        return None
