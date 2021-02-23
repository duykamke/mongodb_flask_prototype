from __future__ import annotations

from flask import Response, make_response, jsonify
from flask.views import MethodView
from marshmallow import fields, Schema
from mongoengine.errors import DoesNotExist

from applications.services.report_template import ReportTemplateService
from presentation.response_messages import NOT_FOUND_FORMAT, \
    SUCCESS_MESSAGE


class SubSectionSchema(Schema):
    class Meta:
        strict = True
    index = fields.Int()
    type = fields.Str(required=True)
    data_type = fields.Str()
    name = fields.Str(required=True)
    sub_sections = fields.List(fields.Nested('self'))


class ReportTemplateSchema(Schema):
    class Meta:
        strict = True
    id = fields.Str(required=True)
    type = fields.Str(required=True)
    name = fields.Str(required=True)
    sub_sections = fields.List(fields.Nested(SubSectionSchema))


class ReportTemplate(MethodView):

    def get(self, report_id: str) -> Response:
        try:
            report = ReportTemplateService().get_report_template_by_id(report_id)
        except DoesNotExist:
            return make_response(jsonify(
                {"message": NOT_FOUND_FORMAT.format(id=report_id)}
            ), 404)
        response = {
            "message": SUCCESS_MESSAGE,
            "template": ReportTemplateSchema().dump(report)
        }
        return make_response(jsonify(response), 200)
