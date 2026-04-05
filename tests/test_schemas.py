"""Tests for schema placeholder files."""

import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
SCHEMAS_DIR = PROJECT_ROOT / "configs" / "schemas"

REQUIRED_SCHEMAS = [
    "species.yaml",
    "environmental_variables.yaml",
    "station_metadata.yaml",
    "survey_metadata.yaml",
]


def test_schema_files_exist():
    """All required schema files must be present."""
    for schema_file in REQUIRED_SCHEMAS:
        path = SCHEMAS_DIR / schema_file
        assert path.is_file(), f"Missing schema file: configs/schemas/{schema_file}"


def test_schemas_are_valid_yaml():
    """All schema files must parse as valid YAML."""
    for schema_file in REQUIRED_SCHEMAS:
        path = SCHEMAS_DIR / schema_file
        with open(path) as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict), f"Schema {schema_file} did not parse as dict"


def test_schemas_have_fields():
    """All schemas must define a fields list."""
    for schema_file in REQUIRED_SCHEMAS:
        path = SCHEMAS_DIR / schema_file
        with open(path) as f:
            data = yaml.safe_load(f)
        assert "schema" in data, f"Schema {schema_file} missing 'schema' key"
        assert "fields" in data["schema"], f"Schema {schema_file} missing 'schema.fields'"
        assert len(data["schema"]["fields"]) > 0, f"Schema {schema_file} has no fields"
