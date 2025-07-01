from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Optional
import json

try:
    import yaml
except ImportError:  # pragma: no cover - yaml is optional
    yaml = None


@dataclass
class Profile:
    name: str
    bio: str
    skills: List[str]
    projects: List[str]
    contacts: Dict[str, str]


def load_profile(path: Optional[str] = None) -> Profile:
    """Load profile data from JSON or YAML file.

    If no path is provided, load the default profile bundled with the
    package.
    """
    if path is None:
        default_path = Path(__file__).parent / "data" / "default_profile.json"
        path = str(default_path)
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Profile file not found: {path}")
    text = file_path.read_text(encoding="utf-8")
    if file_path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            raise RuntimeError("PyYAML is required to load YAML files")
        data = yaml.safe_load(text)
    elif file_path.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        raise ValueError("Unsupported file type")

    return Profile(
        name=data.get("name", ""),
        bio=data.get("bio", ""),
        skills=data.get("skills", []),
        projects=data.get("projects", []),
        contacts=data.get("contacts", {}),
    )
