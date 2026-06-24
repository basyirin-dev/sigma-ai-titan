# Changelog

## [Unreleased] — Initial Project Setup

### Added

- **Project scaffold**: Streamlit multipage app with dashboard, 3 modules (Solver, Archive, Oracle)
- **Dark theme CSS**: Custom "The Void" aesthetic with neon-green accent, JetBrains Mono font
- **Sigma Protocol**: System prompt defining Analysis → First Principles → Solution → Final Answer reasoning
- **Ground truth data**: MRSM Physics 2025 trial paper (5 questions with solutions and oracle insights)
- **Mock infrastructure**: `mock_data.py` (thought chains + responses), `mock_logic.py` (keyword routing), `test_cases.json` (8 scenarios)
- **Utility functions**: `process_image()`, `convert_pdf_to_image()`, `sanitize_latex()` in `utils.py`

### Technical Debt

- Page files (`1_⚡_Titan_Solver.py`, `2_📂_The_Archive.py`, `3_🧠_The_Oracle.py`) import 5 functions from `utils.py` that do not exist
- `src/core/model.py` is an empty stub
- `THOUGHT_CHAINS` defined twice in `mock_data.py` (second overwrites first)
- No real AI integration — all responses are mocked
- No vector database integration — Archive page is non-functional
- No tests exist
- No Docker or CI/CD configuration
- CLI entry point `sigma_ai.cli:main` does not exist
