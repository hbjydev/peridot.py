from .paginator import Paginator
from .package import Package
from typing import List
import requests


class Project:
    baseUrl: str

    id: str
    createdAt: str
    updatedAt: str
    name: str
    majorVersion: str
    archs: List[str]
    distTag: str
    targetGitlabHost: str
    targetPrefix: str
    targetBranchPrefix: str
    sourceGitHost: str
    sourcePrefix: str
    sourceBranchPrefix: str
    cdnUrl: str
    streamMode: bool
    targetVendor: str
    additionalVendor: str
    followImportDist: bool
    branchSuffix: str
    gitMakePublic: bool
    vendorMacro: str
    packagerMacro: str

    def from_json(self, json: dict[str, str]):
        """
        Parses the JSON from the API into the class instance.

        Generally not something you would call yourself, only used by internal
        client functions.
        """
        self.id = json['id']
        self.createdAt = json['createdAt']
        self.updatedAt = json['updatedAt']
        self.name = json['name']
        self.majorVersion = json['majorVersion']
        self.archs = json['archs']
        self.distTag = json['distTag']
        self.targetGitlabHost = json['targetGitlabHost']
        self.targetPrefix = json['targetPrefix']
        self.targetBranchPrefix = json['targetBranchPrefix']
        self.sourceGitHost = json['sourceGitHost']
        self.sourcePrefix = json['sourcePrefix']
        self.sourceBranchPrefix = json['sourceBranchPrefix']
        self.cdnUrl = json['cdnUrl']
        self.streamMode = json['streamMode']
        self.targetVendor = json['targetVendor']
        self.additionalVendor = json['additionalVendor']
        self.followImportDist = json['followImportDist']
        self.branchSuffix = json['branchSuffix']
        self.gitMakePublic = json['gitMakePublic']
        self.vendorMacro = json['vendorMacro']
        self.packagerMacro = json['packagerMacro']

        apiUrl = 'https://peridot.build.resf.org/api/v1'
        self.baseUrl = f'{apiUrl}/projects/{self.id}'

    def packages(self) -> Paginator[Package]:
        req = requests.get(f'{self.baseUrl}/packages')
        paginator = Paginator[Package](req.json(), 'packages')
        return paginator
