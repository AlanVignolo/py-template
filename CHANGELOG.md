# Changelog

## [0.1.0] - 2026-08-27

### Added
- Project template with `src/` layout and `uv`
- Configuration with `pydantic-settings` and `.env`
- `Predictor` protocol for ML testing without real models
- Custom exception hierarchy with chained exceptions
- Logging with `getLogger(__name__)` pattern
- Image preprocessing function (resize, normalize, HWC→CHW)
- Full test suite: parametrized, fixtures, monkeypatch, tmp_path, coverage
- mypy strict mode
- pre-commit with ruff, ruff-format, large-files check and nbstripout
- GitHub Actions CI with --locked and Python 3.13
- Branch protection ruleset on master
