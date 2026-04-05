"""Tests for Day 2 artifacts: trait tables, species configs, source/feature registries."""

import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

FOCAL_TARGETS = ["blue_crab", "eastern_oyster", "estuarine_finfish", "seagrass_sav"]


def test_trait_tables_exist():
    """Each focal target must have a trait table."""
    for target in FOCAL_TARGETS:
        path = PROJECT_ROOT / "01_literature_map" / "trait_tables" / f"{target}.md"
        assert path.is_file(), f"Missing trait table: {target}.md"


def test_trait_tables_have_required_sections():
    """Each trait table must contain key section headers."""
    required_headers = [
        "Healthy-Range Concept",
        "Temperature Relevance",
        "Salinity Relevance",
        "Dissolved Oxygen Relevance",
        "Habitat Dependency",
        "Degree-Day Relevance",
        "Literature Status",
        "Unresolved Threshold Questions",
    ]
    for target in FOCAL_TARGETS:
        path = PROJECT_ROOT / "01_literature_map" / "trait_tables" / f"{target}.md"
        content = path.read_text()
        for header in required_headers:
            assert header in content, f"Trait table {target}.md missing section: {header}"


def test_species_configs_exist():
    """Each focal target must have a species config YAML."""
    for target in FOCAL_TARGETS:
        path = PROJECT_ROOT / "configs" / "species" / f"{target}.yaml"
        assert path.is_file(), f"Missing species config: {target}.yaml"


def test_species_configs_are_valid_yaml():
    """All species configs must parse as valid YAML."""
    for target in FOCAL_TARGETS:
        path = PROJECT_ROOT / "configs" / "species" / f"{target}.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict), f"Species config {target}.yaml did not parse as dict"


def test_species_configs_have_required_keys():
    """Species configs must have essential keys."""
    required_keys = [
        "species_id",
        "common_name",
        "target_type",
        "hypothesis_roles",
        "response_variable",
        "depth_policy",
        "healthy_ranges",
        "variable_relevance",
    ]
    for target in FOCAL_TARGETS:
        path = PROJECT_ROOT / "configs" / "species" / f"{target}.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)
        for key in required_keys:
            assert key in data, f"Species config {target}.yaml missing key: {key}"


def test_source_registry_valid():
    """Source registry must parse and contain sources."""
    path = PROJECT_ROOT / "configs" / "sources" / "source_registry.yaml"
    with open(path) as f:
        data = yaml.safe_load(f)
    assert "sources" in data
    assert len(data["sources"]) >= 5, "Expected at least 5 data sources"


def test_feature_registry_valid():
    """Feature registry must parse and contain engineered and benchmark features."""
    path = PROJECT_ROOT / "configs" / "features" / "feature_registry.yaml"
    with open(path) as f:
        data = yaml.safe_load(f)
    assert "engineered_features" in data
    assert "benchmark_features" in data
    assert len(data["engineered_features"]) >= 5, "Expected at least 5 engineered features"
    assert len(data["benchmark_features"]) >= 3, "Expected at least 3 benchmark features"


def test_feature_registry_has_variable_aliases():
    """Feature registry must include a variable alias map."""
    path = PROJECT_ROOT / "configs" / "features" / "feature_registry.yaml"
    with open(path) as f:
        data = yaml.safe_load(f)
    assert "variable_aliases" in data
    assert len(data["variable_aliases"]) >= 3


def test_project_config_has_variable_families():
    """Working project config must classify variables into families."""
    path = PROJECT_ROOT / "configs" / "project_config.yaml"
    with open(path) as f:
        config = yaml.safe_load(f)
    assert "variable_families" in config
    required_families = ["forcing", "local_estuarine_state", "habitat_condition",
                         "engineered_features", "benchmark"]
    for family in required_families:
        assert family in config["variable_families"], f"Missing variable family: {family}"


def test_project_config_has_deferred_and_rejected():
    """Working project config must track deferred and rejected variables."""
    path = PROJECT_ROOT / "configs" / "project_config.yaml"
    with open(path) as f:
        config = yaml.safe_load(f)
    assert "deferred_variables" in config
    assert "rejected_variables" in config
    assert len(config["deferred_variables"]) >= 3
    assert len(config["rejected_variables"]) >= 3


def test_reference_stubs_exist():
    """Reference stubs file must exist and contain stubs."""
    path = PROJECT_ROOT / "refs" / "reference_stubs.md"
    assert path.is_file()
    content = path.read_text()
    assert "REF-BC-01" in content, "Missing blue crab reference stub"
    assert "REF-OY-01" in content, "Missing oyster reference stub"
    assert "REF-FF-01" in content, "Missing finfish reference stub"
    assert "REF-SAV-01" in content, "Missing SAV reference stub"
    assert "REF-GEN-01" in content, "Missing general reference stub"


def test_lit_matrix_has_mechanism_rows():
    """Literature matrix must contain mechanism entries."""
    path = PROJECT_ROOT / "01_literature_map" / "lit_matrix.csv"
    content = path.read_text()
    lines = [l for l in content.strip().split("\n") if l and not l.startswith("#")]
    # Header + at least 5 mechanism rows
    assert len(lines) >= 6, f"Expected at least 6 lines (header + 5 mechanisms), got {len(lines)}"


def test_no_fabricated_thresholds_in_species_configs():
    """Species configs must not contain hardcoded numeric thresholds (DEC-005)."""
    for target in FOCAL_TARGETS:
        path = PROJECT_ROOT / "configs" / "species" / f"{target}.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)
        ranges = data.get("healthy_ranges", {})
        for var_name, var_range in ranges.items():
            if isinstance(var_range, dict):
                lower = var_range.get("lower")
                upper = var_range.get("upper")
                assert lower is None, (
                    f"Species {target} has a hardcoded lower threshold for {var_name}: {lower}. "
                    "Thresholds require literature sign-off (DEC-005)."
                )
                assert upper is None, (
                    f"Species {target} has a hardcoded upper threshold for {var_name}: {upper}. "
                    "Thresholds require literature sign-off (DEC-005)."
                )
