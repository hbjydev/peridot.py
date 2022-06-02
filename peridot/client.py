import requests
from typing import List
from .project import Project


class PeridotClient:
    url: str = "https://peridot.build.resf.org/api/v1"

    def __init__(
        self,
        url: str = "https://peridot.build.resf.org/api/v1"
    ):
        self.url = url

    def projects(self) -> List[Project]:
        p: List[Project] = []

        list = requests.get(f'{self.url}/projects')
        json = list.json()
        for pdata in json['projects']:
            proj = Project()
            proj.from_json(pdata)
            p.append(proj)

        return p
