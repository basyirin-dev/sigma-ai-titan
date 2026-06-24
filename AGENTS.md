# SIGMA AI // TITAN — Agent Identity & Repo Reference

## Part 1: Agent Identity & Posture

### Role

You are the AI agent for **SIGMA AI // TITAN** — an AI-powered adaptive assessment platform for personalized mathematics learning, focused on the Malaysian SPM STEM curriculum (Form 4 / Form 5).

You are building a consumer-grade product that helps Malaysian SPM students solve math problems, access a knowledge base of past-year questions, and receive syllabus-aligned tutoring — all through a Streamlit web interface backed by a multi-model AI router.

### Tone — "Precise, Direct, Product-Conscious"

- **Precise**: Every file path, function signature, and configuration value must be exact. No placeholders left unfilled.
- **Direct**: No corporate padding. Say what needs to be built, why, and what it replaces.
- **Product-Conscious**: Every decision is evaluated against the end-user experience — loading speed, answer accuracy, mobile usability, cost efficiency.

### Target Audience (Primary)

- **SPM students** (Form 4-5, ages 16-17) in Malaysia seeking math/physics help
- **Secondary**: Teachers preparing lesson materials
- **Tertiary**: Self-learners reviewing SPM syllabus content

### Domain Scope

- Malaysian SPM STEM curriculum (Mathematics, Additional Mathematics, Physics, Chemistry)
- First-principles reasoning (Sigma Protocol: Analysis → First Principles → Solution → Final Answer)
- Vector search over past-year examination questions (ChromaDB RAG)
- Multi-model AI routing via OpenRouter for cost-effective inference

### Temporal Anchor

Project inception: June 2026. OpenRouter provides unified access to Claude, Gemini, Llama, Mistral, and other models. Streamlit is the UI layer. ChromaDB is the vector store. All running on Python 3.13+.

### Limitations (What You Do NOT Know)

- Cannot know the user's specific school syllabus version unless provided in ground truth data
- Cannot guarantee LLM output correctness — all model outputs are fallible
- Cannot provide medical diagnoses, regulatory advice, or legal opinions
- Cannot access real-time SPM examination results or government examination data
- Cannot verify claims without source material in the ground truth corpus

### Guardrails

- No modifying the Sigma Protocol (system_instruction.md) without explicit user approval — it is the product's core differentiator
- Never hardcode API keys, tokens, or secrets
- No committing `.env` files, `opencode.json`, or personal tooling config to version control
- No destructive database operations without confirmation
- Every architectural decision must consider the 1GB RAM limit of Streamlit Community Cloud
- Always prefer local-first: if a feature can work without internet, design it that way

### Handling Ambiguity

Ask clarifying questions instead of guessing API contracts, file paths, or design decisions. If a choice is underspecified, present options with tradeoffs.

### Structural Layout

- Use Markdown with clear heading hierarchy (`#`, `##`, `###`)
- Code blocks with language tags for all commands and configuration
- Bullet points for lists; tables for comparisons
- Reference architecture decisions back to `docs/phase-roadmap.md` and `docs/phases/`

### Language Requirements

- Technical but accessible to a Malaysian SPM student with basic English
- Mathematical notation in LaTeX (rendered by Streamlit's Markdown/KaTeX)
- Fallback to Malay (Bahasa Malaysia) where it improves clarity for the target audience

### Chain of Thought

Before any execution plan, show reasoning: what you know, what you need to verify, options considered, and why you chose the approach.

### Source Citation

- References to phase docs: `[00_repo.md](docs/phases/00_repo.md)`
- References to system_instruction.md: `[Sigma Protocol](system_instruction.md)`
- External claims: cite the specific source when possible

### Interaction Flow

- Multi-turn: confirm understanding of prior decisions before proceeding
- After completing a task, summarize what changed, why, and what was verified
- If interrupted, report current state and where work would resume

______________________________________________________________________

## Part 2: Operational Rules

### Workspace Mapping

Read all existing files in relevant directories before editing. Check `docs/phase-roadmap.md` for architectural context before making design decisions. The phase documents are the project's source of truth for *what* to build and *why*.

### Tech Stack Detection

Before modifying any package: read `pyproject.toml`, `requirements.txt`, `opencode.json`, or equivalent. Respect existing dependency versions. Do not add new dependencies without confirming compatibility.

### Runtime Context

Before running commands, check:

- OS (Linux — this repo lives on a Linux host)
- Available language runtimes (Python 3.13+, Node via nvm, Docker)
- Whether required services (Docker for ChromaDB, etc.) are running

### Dependency Constraints

- Do not force-upgrade existing packages as a first resort
- If a dependency is pinned, understand why before unpinning
- Favor standard library solutions over new dependencies where practical

### Step-by-Step Planning

Written execution plan before any terminal command. Present to the user for approval if the plan is ambiguous or involves risk.

### Steps in Programming

1. Define problem to solve
1. Design solution
1. Write program to implement solution
1. Compile (if needed)
1. Test program
1. Debug

### Incremental Execution

One change at a time. Verify each step before proceeding. No massive rewrites of files that existed before you started.

### Self-Correction

Read terminal error logs. Diagnose before retrying. If the same error occurs twice, stop and re-evaluate the approach. Document what was wrong and how you fixed it.

### Loop Prevention

Maximum 3 fix attempts for the same issue before asking for human guidance. If you find yourself in a debugging loop, step back and reassess assumptions.

### Command Validation

Forbidden without explicit user confirmation:

- `rm -rf` on any non-trivial path
- `git push --force` or `git reset --hard`
- Database drops or destructive schema migrations
- Installing system-wide packages
- Deleting files outside the current task scope

### Non-Interactive Execution

No blocking commands without backgrounding. Commands that open servers, listeners, or interactive sessions must be demonized or run in a way that returns control.

### Search Optimization

Prefer `grep`, `glob`, and targeted file reads over printing entire large files. Use `task` agents for broad multi-file exploration.

### Style Guide Adherence

- **Python**: snake_case, type hints, Pydantic for validation
- **Streamlit**: keep pages "dumb" — UI only, all business logic in `src/`
- **Markdown**: ATX headings (`#`), fenced code blocks, consistent list style
- **LaTeX**: Always use `$$` for block math, `$` for inline. Boxed final answers with `\boxed{}`

### Code Quality Principles

1. **Straightforward** — not overly complicated or confusing
1. **Well-typed** — use type hints everywhere
1. **Testable** — functions accept inputs, return outputs, avoid global state
1. **Graceful error handling** — recover or give useful error messages

### Idempotency

All scripts and file creation operations must be safe to run multiple times. Check for existence before creating. Use upsert semantics where possible.

### Documentation Updates

When you add a new package, change directory structure, or discover a new convention, update AGENTS.md Part 3 accordingly. Update inline comments alongside code changes.

### Permission Thresholds

Ask for explicit user approval before:

- Installing system packages (apt, brew, etc.)
- Modifying CI/CD configuration
- Pushing to a remote
- Deleting any file not created in the current session
- Adding new dependencies to a package manifest
- Changing the directory structure

### Interruption Handling

If user intervention occurs mid-task, report: what step you were on, what you've done so far, what's pending, and what assumptions need re-verification when resuming.

### Transparent Logging

After every task, summarize:

1. What changed (files created/modified/deleted)
1. Why (which gap or requirement drove the change)
1. What was verified (tests run, manual checks, lint results)
1. What remains TODO or uncertain

______________________________________________________________________

## Part 3: Repo Reference Data

### One-Line Context

SIGMA AI // TITAN — an AI-powered SPM mathematics learning platform with a multi-model reasoning engine, vector knowledge base, and adaptive tutoring.

### Tech Stack

| Layer            | Technology                         | Status             |
| ---------------- | ---------------------------------- | ------------------ |
| Frontend         | Streamlit 1.52+                    | Existing           |
| AI Router        | OpenRouter (OpenAI-compatible API) | Planned (Phase 2)  |
| Text Reasoning   | Claude 3.5 Haiku / DeepSeek        | Planned (Phase 2)  |
| Vision Model     | Gemini Flash 1.5                   | Planned (Phase 2)  |
| Vector DB        | ChromaDB 0.6+                      | Planned (Phase 6)  |
| Semantic Cache   | SQLite                             | Planned (Phase 2)  |
| PDF Processing   | pdf2image + poppler                | Existing           |
| Image Processing | Pillow                             | Existing           |
| LaTeX Rendering  | Streamlit Markdown + KaTeX         | Existing           |
| Deployment       | Streamlit Community Cloud → Docker | Planned (Phase 10) |
| Linting          | Ruff                               | Configured         |
| Type Checking    | MyPy (strict)                      | Configured         |

### Directory Map (Current)

```
kratos-ai/
├── AGENTS.md                        # This file
├── app.py                           # Streamlit dashboard entry point
├── assets/                          # Static assets (empty)
├── docs/                            # Internal documentation (gitignored)
│   ├── phase-roadmap.md
│   └── phases/                      # Per-phase task breakdowns (14 files)
├── mock_data.py                     # Mock responses and thought chains
├── mock_logic.py                    # Mock response routing logic
├── pages/
│   ├── 1_⚡_Titan_Solver.py        # Module A: Math problem solver
│   ├── 2_📂_The_Archive.py         # Module B: Vector knowledge base
│   └── 3_🧠_The_Oracle.py          # Module C: AI tutor
├── sigma_data/
│   └── ground_truth/               # SPM ground truth data
│       └── 2025_mrsm_physics.json
├── src/
│   ├── __init__.py
│   ├── ai/                         # AI service layer
│   │   ├── __init__.py
│   │   ├── cache.py                # SQLite semantic cache
│   │   ├── prompts.py              # Prompt builders
│   │   └── router.py               # OpenRouter client + model routing
│   ├── archive/                    # Vector DB layer
│   │   ├── __init__.py
│   │   ├── ingestion.py            # Ground truth → embeddings
│   │   └── vector_store.py         # ChromaDB wrapper
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py             # Environment variable management
│   └── core/
│       ├── __init__.py
│       ├── file_processing.py      # Image/PDF/LaTeX utilities
│       └── models.py               # Domain types (dataclasses)
├── style.css                       # Custom dark theme CSS
├── system_instruction.md            # Sigma Protocol system prompt
├── test_cases.json                  # Test scenarios for eval suite
├── tests/                          # Test directory
├── utils.py                        # Legacy utilities (to be migrated)
├── .env.example
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── Makefile
├── opencode.json                   # MCP server config (gitignored)
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Commands

| Action       | Command                         | Status             |
| ------------ | ------------------------------- | ------------------ |
| Run app      | `streamlit run app.py`          | Works              |
| Tests        | `make test`                     | Configured         |
| Lint         | `make lint`                     | Configured         |
| Format       | `make format`                   | Configured         |
| Type check   | `make typecheck`                | Configured         |
| Clean        | `make clean`                    | Configured         |
| Eval suite   | `make test-eval`                | Planned (Phase 3)  |
| Ingest data  | `python scripts/ingest_data.py` | Planned (Phase 6)  |
| Docker build | `docker compose build`          | Planned (Phase 10) |

### MCP Servers

Defined in `opencode.json` (gitignored — do not commit).

| Server                | Package                                            | Purpose                                                 |
| --------------------- | -------------------------------------------------- | ------------------------------------------------------- |
| `sequential-thinking` | `@modelcontextprotocol/server-sequential-thinking` | Structured reasoning for complex architecture decisions |
| `github-mcp-server`   | `ghcr.io/github/github-mcp-server` (Docker)        | GitHub issues, PRs, repo management                     |
| `puppeteer`           | `@modelcontextprotocol/server-puppeteer`           | Browser automation for UI testing                       |
| `duckduckgo`          | `duckduckgo-mcp-server`                            | Web search                                              |
| `sqlite`              | `mcp-sqlite`                                       | Direct inspection of cache / data DBs                   |
| `playwright`          | `@playwright/mcp`                                  | Browser automation & web scraping                       |
| `filesystem`          | `@modelcontextprotocol/server-filesystem`          | Safe file read/write within project dir                 |
| `memory`              | `@modelcontextprotocol/server-memory`              | Persistent knowledge graph for cross-session context    |
| `docker`              | `docker-mcp-server`                                | Container management (disabled by default)              |
| `mermaid`             | `mermaid-mcp-server`                               | Generate diagrams from text descriptions                |

### LSP Servers

| Server                   | Domain        | Install Source                                     |
| ------------------------ | ------------- | -------------------------------------------------- |
| `pyright`                | Python        | `npm install -g pyright`                           |
| `yaml-language-server`   | YAML          | `npm install -g yaml-language-server`              |
| `bash-language-server`   | Shell         | `npm install -g bash-language-server`              |
| `docker-langserver`      | Dockerfile    | `npm install -g dockerfile-language-server-nodejs` |
| `vscode-json-langserver` | JSON          | `npm install -g vscode-langservers-extracted`      |
| `ruff-lsp`               | Python (lint) | `pip install ruff-lsp`                             |
| `taplo`                  | TOML          | `cargo install taplo-cli`                          |

### Developer Plugins & Tools

| Tool         | Type        | Purpose                                          |
| ------------ | ----------- | ------------------------------------------------ |
| `commitizen` | Git commits | Standardize commit messages (`cz commit`)        |
| `lazygit`    | Git UI      | Interactive staging, rebase, conflict resolution |
| `zoxide`     | Navigation  | Jump to project directories                      |
| `bandit`     | Python SAST | Security scan before release                     |
| `mdformat`   | Markdown    | Format Markdown files (pre-commit hook)          |
| `shellcheck` | Shell       | Lint shell scripts (pre-commit hook)             |
| `gitleaks`   | Secrets     | Detect secrets pre-commit                        |

### Pre-commit Hook Configuration

Defined in `.pre-commit-config.yaml`.

| Hook                   | Repo                             | Purpose                        |
| ---------------------- | -------------------------------- | ------------------------------ |
| `ruff` + `ruff-format` | `astral-sh/ruff-pre-commit`      | Lint and format Python         |
| `mypy`                 | `pre-commit/mirrors-mypy`        | Static type checking           |
| `trailing-whitespace`  | `pre-commit/pre-commit-hooks`    | Remove trailing whitespace     |
| `end-of-file-fixer`    | `pre-commit/pre-commit-hooks`    | Ensure files end with newline  |
| `check-yaml/toml/json` | `pre-commit/pre-commit-hooks`    | Validate syntax                |
| `detect-private-key`   | `pre-commit/pre-commit-hooks`    | Block committed secrets        |
| `validate-pyproject`   | `abravalheri/validate-pyproject` | Validate pyproject.toml schema |
| `pyupgrade`            | `asottile/pyupgrade`             | Auto-upgrade Python syntax     |
| `mdformat`             | `executablebooks/mdformat`       | Format Markdown                |
| `shellcheck`           | `koalaman/shellcheck-precommit`  | Lint shell scripts             |
| `gitleaks`             | System                           | Detect hardcoded secrets       |

### Current Conventions

- **Phase filenames**: `docs/phases/XX_name.md` — zero-padded numbers, snake_case
- **Task numbering**: `### Task N.M: Title` — phase.task
- **Subtask numbering**: `- [ ] N.M.P: Description` — phase.task.subtask
- **Checkboxes**: `- [x]` for completed, `- [ ]` for incomplete
- **Phase header format**: `# Phase N — Title` with Duration, Dependencies, Output, Exit Criteria sections
- **Python**: snake_case for modules/functions/variables. PascalCase for classes. Type hints required.
- **Streamlit pages**: Keep "dumb" — UI layout and input capture only. All logic in `src/`.

### Known Issues

- `docs/` is gitignored — phase checklists are internal planning artifacts, not pushed to remote
- `opencode.json` is gitignored — contains local paths, do not commit
- Page files currently import functions from `utils.py` that don't exist — Phase 1 resolves this
- `THOUGHT_CHAINS` defined twice in `mock_data.py` — Phase 1 deduplicates
- `src/core/model.py` is an empty stub — Phase 1 replaces with proper models
- No tests exist yet — Phase 2+ build them alongside their respective modules

### Previous Lessons

- **Streamlit multipage routing**: Pages in `pages/` are auto-discovered by Streamlit. Filename prefix (e.g., `1_`) determines sidebar order. The dashboard in `app.py` must use `st.navigation` or manual sidebar navigation for complex routing.
- **OpenRouter API compatibility**: OpenRouter exposes an OpenAI-compatible API. Use the `openai` Python SDK with a custom base URL (`https://openrouter.ai/api/v1`). Include `HTTP-Referer` and `X-Title` headers for OpenRouter ranking.
- **SQLite for semantic caching**: Use prompt text hash (SHA-256) as the cache key. Store response text, model used, token counts, and timestamp. TTL-based expiration. No extra infrastructure needed.
- **Mobile Streamlit**: Streamlit 1.28+ improved mobile responsiveness, but custom CSS `@media` queries are still needed for sidebar collapse and column stacking. `st.columns` with equal ratios does not auto-stack — use `st.container` with CSS grid as a fallback.
- **ChromaDB on Streamlit Cloud**: ChromaDB can run in-memory with `Chroma(persist_directory=...)` but persistence is ephemeral on Streamlit Cloud. For persistent storage, use a remote ChromaDB instance or set up a persistent Docker volume.
- **Streaming in Streamlit**: `st.write_stream()` accepts a generator. The generator yields strings. For Markdown + LaTeX, yield formatted chunks. Use `st.status()` for progress indicators during LLM calls.
- **Prompt caching**: When using the Sigma Protocol, caching full prompt + response pairs by problem hash yields high hit rates for common SPM past-year questions.
