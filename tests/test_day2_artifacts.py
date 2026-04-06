"""Tests for Day 2 artifacts: trait tables, species configs, source/feature registries,
cross-file consistency, DEC-005 compliance, and deferred-feature guards."""

import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

FOCAL_TARGETS = ["blue_crab", "eastern_oyster", "southern_flounder", "seagrass_sav"]

LOCKED_SPECIES_NAMES = ["Blue crab", "Eastern oyster", "Southern Flounder", "Seagrass / SAV"]


# --- File existence ---

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


# --- Registry tests ---

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


# --- Variable family and deferred/rejected tests ---

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


# --- Reference stubs and lit matrix ---

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
    assert len(lines) >= 6, f"Expected at least 6 lines (header + 5 mechanisms), got {len(lines)}"


# --- DEC-005: No fabricated thresholds anywhere ---

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


def test_no_fabricated_thresholds_in_config_template():
    """Config template must not contain hardcoded numeric thresholds (DEC-005)."""
    path = PROJECT_ROOT / "configs" / "project_config_template.yaml"
    with open(path) as f:
        config = yaml.safe_load(f)
    for species in config["focal_species"]:
        name = species["name"]
        ranges = species.get("healthy_ranges", {})
        for var_name, bounds in ranges.items():
            if isinstance(bounds, list):
                for val in bounds:
                    assert val is None, (
                        f"Config template has hardcoded threshold for {name}/{var_name}: {val}. "
                        "Thresholds require literature sign-off (DEC-005)."
                    )
        dd = species.get("degree_day_base_c")
        assert dd is None, (
            f"Config template has hardcoded degree_day_base_c for {name}: {dd}. "
            "Requires literature sign-off (DEC-005)."
        )


def test_no_fabricated_thresholds_in_working_config():
    """Working project config must not contain hardcoded numeric thresholds (DEC-005)."""
    path = PROJECT_ROOT / "configs" / "project_config.yaml"
    with open(path) as f:
        config = yaml.safe_load(f)
    for species in config["focal_species"]:
        name = species["name"]
        ranges = species.get("healthy_ranges", {})
        for var_name, bounds in ranges.items():
            if isinstance(bounds, list):
                for val in bounds:
                    assert val is None, (
                        f"Working config has hardcoded threshold for {name}/{var_name}: {val}. "
                        "Thresholds require literature sign-off (DEC-005)."
                    )


# --- Cross-file consistency ---

def test_cross_file_species_names_match():
    """README, brief, hypotheses, and project_config must list the same 4 species names."""
    readme = (PROJECT_ROOT / "README.md").read_text()
    brief = (PROJECT_ROOT / "00_project_brief" / "brief_v1.md").read_text()
    config_path = PROJECT_ROOT / "configs" / "project_config.yaml"
    with open(config_path) as f:
        config = yaml.safe_load(f)
    config_names = [s["name"] for s in config["focal_species"]]
    assert config_names == LOCKED_SPECIES_NAMES, (
        f"project_config.yaml species names {config_names} do not match "
        f"locked set {LOCKED_SPECIES_NAMES}"
    )
    for name in LOCKED_SPECIES_NAMES:
        assert name in readme, f"README.md missing locked species: {name}"
        assert name in brief, f"brief_v1.md missing locked species: {name}"


def test_cross_file_southern_flounder_locked():
    """Southern Flounder must appear by name (not as 'TBD finfish') in binding files."""
    for filepath in [
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "00_project_brief" / "brief_v1.md",
        PROJECT_ROOT / "00_project_brief" / "hypotheses_v1.md",
    ]:
        content = filepath.read_text()
        assert "Southern Flounder" in content, (
            f"{filepath.name} missing 'Southern Flounder' — still using generic name?"
        )
        assert "TBD estuarine finfish" not in content, (
            f"{filepath.name} still contains 'TBD estuarine finfish' — should be locked"
        )


def test_cross_file_pilot_geography():
    """Binding files must reference the locked pilot geography, not generic 'NC'."""
    for filepath in [
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "00_project_brief" / "brief_v1.md",
    ]:
        content = filepath.read_text()
        assert "Pamlico Sound" in content, (
            f"{filepath.name} missing 'Pamlico Sound' — geography not locked?"
        )
        assert "Neuse River Estuary" in content, (
            f"{filepath.name} missing 'Neuse River Estuary' — geography not locked?"
        )


def test_config_geography_locked():
    """Working config must have pilot sub-systems filled in, not empty."""
    path = PROJECT_ROOT / "configs" / "project_config.yaml"
    with open(path) as f:
        config = yaml.safe_load(f)
    subs = config["geography"]["sub_systems"]
    assert len(subs) >= 2, f"Geography sub_systems should be locked, got: {subs}"
    assert "Pamlico Sound" in subs
    assert "Neuse River Estuary" in subs


# --- No deferred features presented as active defaults ---

def test_no_spatial_compression_in_active_features():
    """Spatial compression must not appear as an active v1 feature (DEC-008)."""
    catalog = (PROJECT_ROOT / "04_features" / "feature_catalog.md").read_text()
    assert "habitat_compression_spatial" not in catalog, (
        "Feature catalog still lists habitat_compression_spatial as active. "
        "Spatial compression is DEFERRED per DEC-008."
    )


def test_figure_plan_no_spatial_panel():
    """Figure plan must not promise spatial interpolation panels for v1 (DEC-008)."""
    figure_plan = (PROJECT_ROOT / "08_figures" / "figure_plan.md").read_text()
    assert "Spatial panel showing where compression occurs" not in figure_plan, (
        "Figure plan still promises spatial compression panels. "
        "Spatial compression is DEFERRED per DEC-008."
    )


def test_no_estuarine_finfish_remnants():
    """No files should use the old generic 'estuarine_finfish' ID after rename."""
    for filepath in [
        PROJECT_ROOT / "configs" / "project_config.yaml",
        PROJECT_ROOT / "configs" / "features" / "feature_registry.yaml",
    ]:
        content = filepath.read_text()
        assert "estuarine_finfish" not in content, (
            f"{filepath.name} still references 'estuarine_finfish' — should be 'southern_flounder'"
        )


def test_scaffold_only_gate_sentence():
    """Binding files must contain the scaffold-only gate sentence."""
    gate_fragment = "scaffold and configuration only"
    for filepath in [
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "00_project_brief" / "brief_v1.md",
        PROJECT_ROOT / "00_project_brief" / "hypotheses_v1.md",
    ]:
        content = filepath.read_text()
        assert gate_fragment in content, (
            f"{filepath.name} missing scaffold-only gate sentence"
        )
