import inject as inject

from domains.models.entities.report_templates import ReportTemplate
from domains.repositories.report_template_repository import IReportTemplateRepository


class ReportTemplateService:
    @inject.param('report_repository', IReportTemplateRepository)
    def __init__(self, report_repository: IReportTemplateRepository) -> None:
        self._report_repository = report_repository

    def get_report_template_by_id(self, id: str) -> ReportTemplate:
        return self._report_repository.get_by_id(id)
