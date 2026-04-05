"""Tests that the repo structure is complete and consistent."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

REQUIRED_DIRS = [
    "00_project_brief",
    "01_literature_map",
    "02_data_inventory",
    "03_pipeline",
    "04_features",
    "05_benchmarks",
    "06_models",
    "07_ablation_robustness",
    "08_figures",
    "09_manuscript",
    "configs",
    "configs/schemas",
    "tests",
    "data/raw",
    "data/intermediate",
    "data/processed",
    "docs",
    "scripts",
]

REQUIRED_FILES = [
    "README.md",
    "pyproject.toml",
    "environment.yml",
    ".gitignore",
    "Makefile",
    "issue_board.md",
    "decisions_log.md",
    "assumptions_log.md",
    "configs/project_config_template.yaml",
    "00_project_brief/brief_v1.md",
    "00_project_brief/hypotheses_v1.md",
    "01_literature_map/lit_matrix.csv",
    "01_literature_map/variable_ontology.md",
    "02_data_inventory/data_inventory.csv",
    "02_data_inventory/access_tracker.md",
    "03_pipeline/README.md",
    "04_features/feature_catalog.md",
    "05_benchmarks/benchmark_registry.yaml",
    "06_models/model_spec.md",
    "07_ablation_robustness/reviewer_attack.md",
    "08_figures/figure_plan.md",
    "09_manuscript/paper_outline.md",
]


def test_required_directories_exist():
    """All required directories must be present."""
    for d in REQUIRED_DIRS:
        path = PROJECT_ROOT / d
        assert path.is_dir(), f"Missing required directory: {d}"


def test_required_files_exist():
    """All required files must be present."""
    for f in REQUIRED_FILES:
        path = PROJECT_ROOT / f
        assert path.is_file(), f"Missing required file: {f}"


def test_data_dirs_have_gitkeep():
    """Data subdirectories must have .gitkeep so they are tracked."""
    for subdir in ["raw", "intermediate", "processed"]:
        gitkeep = PROJECT_ROOT / "data" / subdir / ".gitkeep"
        assert gitkeep.exists(), f"Missing data/{subdir}/.gitkeep"


def test_no_fabricated_data():
    """Data directories must not contain any data files (only .gitkeep)."""
    for subdir in ["raw", "intermediate", "processed"]:
        data_dir = PROJECT_ROOT / "data" / subdir
        files = [f for f in data_dir.iterdir() if f.name != ".gitkeep"]
        assert len(files) == 0, f"Unexpected files in data/{subdir}: {files}"
