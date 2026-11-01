# Changelog

## [Unreleased] — Phase 0: Repo Cleanup & Infrastructure

### Added

- **Project scaffold**: Streamlit multipage app with dashboard, 3 modules (Solver, Archive, Oracle)
- **Dark theme CSS**: Custom "The Void" aesthetic with neon-green accent, JetBrains Mono font
- **Sigma Protocol**: System prompt defining Analysis → First Principles → Solution → Final Answer reasoning
- **Ground truth data**: MRSM Physics 2025 trial paper (5 questions with solutions and oracle insights)
- **Mock infrastructure**: `mock_data.py` (thought chains + responses), `mock_logic.py` (keyword routing), `test_cases.json` (8 scenarios)
- **Utility functions**: `process_image()`, `convert_pdf_to_image()`, `sanitize_latex()` in `utils.py`
- **Phase 0 — `src/` skeleton**: `src/__init__.py`, `src/ai/`, `src/archive/`, `src/config/`, `src/core/` with `__init__.py` stubs
- **Phase 0 — `src/config/settings.py`**: `is_mock_mode()` toggle reading `SIGMA_MOCK_MODE` env var
- **Phase 0 — Mock-aware stubs**: `gemini_generate_content`, `save_uploaded_file`, `process_pdf_to_images`, `load_vector_store`, `search_similar_problems` in `utils.py` — raise `NotImplementedError` when mock mode off
- **Phase 0 — Makefile**: 9 targets (`install`, `lint`, `format`, `typecheck`, `test`, `test-eval`, `test-cov`, `clean`, `all`)
- **Phase 0 — Pre-commit hooks**: 14 hooks configured (ruff, mypy, trailing-whitespace, end-of-file-fixer, check-yaml/toml/json, check-added-large-files, check-merge-conflict, detect-private-key, validate-pyproject, pyupgrade, mdformat)
- **Phase 0 — GitHub templates**: `bug_report.md` (SPM-aware), `feature_request.md` (student impact field), `PULL_REQUEST_TEMPLATE.md` (make-command checklist), `CODEOWNERS`
- **Phase 0 — AGENTS.md**: 18-section restructured document combining system instructions + project rules (610 lines)

### Fixed

- Deduplicated `THOUGHT_CHAINS` in `mock_data.py` (second dict kept, first removed)
- Added `-> None` return type to `local_css()` in `app.py` (mypy strict mode)
- Trailing whitespace and missing EOF newlines across 5 files: `system_instruction.md`, `2025_mrsm_physics.json`, `requirements.txt`, `test_cases.json`, `style.css`

### Changed

- `Makefile`: `install` target now uses `uv pip install -e ".[dev]"` (uv-first convention)
- `pyproject.toml`: Added `pydantic>=2.0`, `pysqlite3-binary`, `watchdog`; migrated ruff config to `[tool.ruff.lint]`
- `.gitignore`: Removed duplicate `.ruff_cache/` entry
- GitHub templates: Generic templates replaced with SPM-context-aware versions

### Removed

- `src/core/model.py` — deleted empty stub (Phase 1 creates proper models)
- `install-dev` target in Makefile — merged into `install`
- Dead `[project.scripts]` entry (`sigma_ai.cli:main`) from `pyproject.toml`
- Global Opencode configs (`~/.config/opencode/opencode.json`, `~/.config/opencode/opencode.jsonc`) — consolidated to project level
- `model`/`provider` keys from `opencode.json` — user specifies via `--model` flag

### Technical Debt

- Page files (`1_⚡_Titan_Solver.py`, `2_📂_The_Archive.py`, `3_🧠_The_Oracle.py`) import 5 functions from `utils.py` that do not exist — awaiting Phase 1
- `src/core/models.py` and `src/core/file_processing.py` don't exist yet — Phase 1 creates them
- No real AI integration — all responses are mocked (Phase 2)
- No vector database integration — Archive page is non-functional (Phase 6)
- No tests exist (Phase 2+ build them alongside modules)
- No Docker or CI/CD configuration (Phase 9-10)
