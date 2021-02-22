from abc import abstractmethod

from domains.models.entities.report_templates import ReportTemplate


class IReportTemplateRepository:
    @abstractmethod
    def add_report_template(self, template: ReportTemplate) -> str:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> ReportTemplate:
        pass

    @abstractmethod
    def update_by_id(self, id: str, template: ReportTemplate) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, id: ReportTemplate) -> None:
        pass
