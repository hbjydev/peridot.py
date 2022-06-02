from datetime import datetime


class Package:
    baseUrl: str

    project_id: str

    id: str
    name: str
    type: str
    last_import_at: datetime
    last_build_at: datetime

    def from_json(self, project_id: str, json: dict[str, str]):
        self.id = json['id']
        self.name = json['name']
        self.type = json['type']

        if json['lastImportAt']:
            self.last_import_at = datetime.strptime(str(json['lastImportAt']), '%Y-%m-%dT%H:%M:%S.%fZ')
        else:
            self.last_import_at = None

        if json['lastBuildAt']:
            self.last_build_at = datetime.strptime(str(json['lastBuildAt']), '%Y-%m-%dT%H:%M:%S.%fZ')
        else:
            self.last_build_at = None

        self.project_id = project_id

        apiUrl = 'https://peridot.build.resf.org/api/v1'
        self.baseUrl = f'{apiUrl}/projects/{self.project_id}/packages/id/{self.id}'
