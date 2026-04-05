"""Tests for configuration loading and validation."""

import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_TEMPLATE = PROJECT_ROOT / "configs" / "project_config_template.yaml"


def test_config_template_exists():
    """Config template file must exist."""
    assert CONFIG_TEMPLATE.exists(), "configs/project_config_template.yaml not found"


def test_config_template_is_valid_yaml():
    """Config template must parse as valid YAML."""
    with open(CONFIG_TEMPLATE) as f:
        config = yaml.safe_load(f)
    assert isinstance(config, dict)


def test_config_template_has_required_sections():
    """Config template must contain all required top-level sections."""
    with open(CONFIG_TEMPLATE) as f:
        config = yaml.safe_load(f)

    required_sections = [
        "geography",
        "focal_species",
        "date_ranges",
        "source_paths",
        "analysis_unit",
        "validation",
        "benchmarks",
        "habitat_compression",
        "ablations",
    ]
    for section in required_sections:
        assert section in config, f"Missing required config section: {section}"


def test_config_focal_species_count():
    """Config must define exactly 4 focal targets."""
    with open(CONFIG_TEMPLATE) as f:
        config = yaml.safe_load(f)

    species = config["focal_species"]
    assert len(species) == 4, f"Expected 4 focal species, got {len(species)}"


def test_config_validation_strategy():
    """Validation must use time_blocked as primary strategy."""
    with open(CONFIG_TEMPLATE) as f:
        config = yaml.safe_load(f)

    assert config["validation"]["strategy"] == "time_blocked"
