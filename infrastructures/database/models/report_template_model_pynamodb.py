from __future__ import annotations

from database import db_pynamodb as db
from domains.models.entities.report_templates import ReportTemplate
from domains.repositories.report_template_repository import IReportTemplateRepository
from pynamodb.attributes import UnicodeAttribute, ListAttribute, MapAttribute, NumberAttribute
import pynamodb.exceptions as errors

from tasks.uuid_generator import generate_uuid


class SubSection(MapAttribute):
    index = NumberAttribute(null=True)
    type = UnicodeAttribute()
    data_type = UnicodeAttribute(null=True)
    name = UnicodeAttribute()


class ReportTemplateModel(db.Model, IReportTemplateRepository):
    class Meta:
        table_name = 'report_template'
    id = UnicodeAttribute(hash_key=True, default=generate_uuid)
    type = UnicodeAttribute()
    name = UnicodeAttribute()
    sub_sections = ListAttribute(of=SubSection)

    @classmethod
    def _to_report_template_model(cls, report: ReportTemplate) -> ReportTemplateModel:
        return ReportTemplateModel(
            type=report.type,
            name=report.name,
            sub_sections=report.sub_sections
        )

    @classmethod
    def _to_report_template_object(cls, report: ReportTemplateModel) -> ReportTemplate:
        return ReportTemplate(
            id=report.id,
            type=report.type,
            name=report.name,
            sub_sections=report.sub_sections
        )

    @classmethod
    def _update(cls, report: ReportTemplate,
                db_report: ReportTemplateModel) -> None:
        db_report.type = report.type
        db_report.name = report.name
        db_report.sub_sections = report.sub_sections

        try:
            db_report.update()
        except errors.UpdateError:
            raise ValueError("Already exists")

    @classmethod
    def _delete(cls, report: ReportTemplateModel) -> None:
        report.delete()

    @classmethod
    def add_report_template(cls, report: ReportTemplate) -> str:
        new_report = cls._to_report_template_model(report)
        try:
            new_report.save()
        except errors.PutError:
            raise ValueError("Already exists")
        return str(new_report.name)

    @classmethod
    def get_by_id(cls, id: str) -> ReportTemplate:
        db_report = cls.get(id)
        if db_report is None:
            raise errors.DoesNotExist
        return cls._to_report_template_object(db_report)

    @classmethod
    def update_by_id(cls, id: str, report: ReportTemplate) -> None:
        db_report = cls.objects.get(id=id)
        if db_report is None:
            raise errors.DoesNotExist
        cls._update(report, db_report)

    @classmethod
    def delete_by_id(cls, id: str) -> None:
        db_report = cls.objects.get(id=id)
        cls._delete(db_report)