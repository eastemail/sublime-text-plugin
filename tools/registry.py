from datetime import datetime
import os.path
import json

__doc__ = "Generates Package Control registry file for builded package"


def read_file(file: str):
    dirname = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dirname, file), 'r', encoding='utf8') as f:
        return f.read(None)


version = read_file("../VERSION").strip()
now = datetime.utcnow()

registry = {
    "schema_version": "3.0.0",
    "packages": [{
        "name": "Emmet 2.0",
        "details": "https://github.com/emmetio/sublime-text-plugin",
        "releases": [{
            "version": version,
            "url": "https://github.com/emmetio/sublime-text-plugin/releases/download/v%s/Emmet.zip" % version,
            "date": now.strftime("%Y-%m-%d %H:%M:%S"),
            "sublime_text": ">=3000"
        }]
    }]
}

print(json.dumps(registry, indent=True))
