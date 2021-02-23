from typing import Optional, List

class ReportTemplate:
    def __init__(self,
                 type: str,
                 name: str,
                 sub_sections: List[dict],
                 id: Optional[str] = None,
                 ):
        self._id = id
        self._type = type
        self._name = name
        self._sub_sections = sub_sections

    @property
    def id(self) -> Optional[str]:
        return self._id

    @property
    def type(self) -> str:
        return self._type

    @property
    def name(self) -> str:
        return self._name

    @property
    def sub_sections(self) -> List[dict]:
        return self._sub_sections
