.PHONY: help setup test lint clean pipeline features benchmarks figures

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

setup:  ## Create conda environment
	conda env create -f environment.yml

test:  ## Run all tests
	pytest tests/ -v --tb=short

lint:  ## Run linter
	ruff check .

clean:  ## Remove generated artifacts
	rm -rf data/intermediate/* data/processed/*
	find . -type d -name __pycache__ -exec rm -rf {} +

# TODO: Implement pipeline targets (Day 4-5)
pipeline:  ## Run full ETL pipeline
	@echo "TODO: Implement pipeline (Day 4-5)"

# TODO: Implement feature engineering targets (Day 6-7)
features:  ## Run feature engineering
	@echo "TODO: Implement feature engineering (Day 6-7)"

# TODO: Implement benchmark targets (Day 8-10)
benchmarks:  ## Run all benchmarks
	@echo "TODO: Implement benchmarks (Day 8-10)"

# TODO: Implement figure generation (Day 13-14)
figures:  ## Generate all figures
	@echo "TODO: Implement figure generation (Day 13-14)"
