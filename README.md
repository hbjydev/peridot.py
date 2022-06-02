# Peridot.py

A Python API client for [Peridot](https://peridot.build.resf.org)

## Development

- Install [Direnv](https://direnv.net)
- Clone the repo
- Open the repo
  - Let Direnv install the Python env

## Example

```py
import peridot.client
from peridot.package import Package

client = peridot.client.PeridotClient()

projects = client.projects()

for project in projects:
    for pkg in project.packages().data:
        p = Package()
        p.from_json(project.id, pkg)
        print(f'"{p.name}" -- I: {p.last_import_at}, B: {p.last_build_at}')
```

## License

This library is distributed under an [Apache 2.0 License](./LICENSE).

