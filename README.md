# py-template
[![CI](https://github.com/AlanVignolo/py-template/actions/workflows/ci.yml/badge.svg)](https://github.com/AlanVignolo/py-template/actions/workflows/ci.yml)

Click "Use this template" on GitHub, name the new repo, clone it, then run `uv sync`.

This isn't a project. It's the starting point I use for one — dependency management, tests, linting, type checking and CI already wired together, so a new repo doesn't start from a blank pyproject.toml.

## What's in here and why

- **uv** for environment and dependency management. One tool instead of pip + venv + pip-tools, and `uv.lock` pins exact versions so CI installs the same thing every time (`uv sync --locked`).
- **src/ layout**. The package lives under `src/py_template/`, not at the repo root. That way `import py_template` only works if the package is actually installed, so tests catch import errors that a flat layout would hide.
- **pytest** with fixtures, parametrization, monkeypatch and `tmp_path` already used in the test suite (`tests/`), plus `pytest-cov` for coverage. Meant as a reference for how to structure tests, not just that tests exist.
- **ruff** for linting and formatting. Replaces flake8 + black + isort with one binary.
- **mypy in strict mode**. Catches type errors before runtime, which matters more once a project has more than one contributor.
- **pre-commit hooks**: `check-added-large-files` (stops you from committing a dataset or a model checkpoint by accident), ruff and ruff-format (so bad style never reaches CI), and nbstripout (strips notebook output before it's committed, since notebook diffs are unreadable otherwise).
- **GitHub Actions CI** that runs lint, format check, mypy and tests on every push and pull request against `master`, using the locked dependency set.
- **pydantic-settings** for configuration, reading from environment variables and `.env` with validation instead of raw `os.environ` calls.

## Workflow

`master` is protected. You can't push to it directly — changes go through a pull request, and the PR can't merge until CI is green. That's deliberate: it forces the lint/type/test gate to actually run before anything lands, not just when someone remembers to run it locally.

## About .gitattributes and Git LFS

`.gitattributes` has a line to route `*.pt` files (PyTorch checkpoints) through Git LFS. That line only does anything if Git LFS is installed and `git lfs install` has been run in the clone — otherwise git ignores the filter and commits the file as a normal blob. Nothing in this repo enforces that: no pre-commit hook checks for it, and CI doesn't either. If you clone this template and add a model checkpoint without LFS set up, it'll go into normal git history, and by the time you notice, it's already in there.

## Structure

```
src/py_template/   # package code
tests/             # test suite
.env.example       # environment variables the app reads
```

## Known gaps

- Not published to PyPI — it's a template, not a package.
- The dependencies (numpy, pandas, opencv-python-headless) are placeholders to demonstrate the setup, not something the template actually uses for anything.
- No secrets management beyond `.env` — fine for local dev, not meant for production.
- I haven't tested what happens if you actually try to commit a `.pt` file without LFS installed — the risk above is inferred from how git filters work, not from reproducing it end to end.
