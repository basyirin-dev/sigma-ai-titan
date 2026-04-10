# Changelog

All notable changes to SIGMA AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup and configuration
- Streamlit-based web interface
- Google Gemini AI integration
- PDF and image processing capabilities
- Multi-page application structure (Solver, Archive, Oracle)
- Vector database integration with ChromaDB

### Changed
- Updated project name from "sigma-ai-v3" to "SIGMA AI"
- Improved configuration management with environment variables
- Enhanced documentation structure

### Fixed
- Hardcoded paths in utils.py now use environment variables
- Cross-platform compatibility improvements

### Deprecated
- N/A

### Removed
- N/A

### Security
- Added comprehensive .gitignore for security
- Environment variable-based configuration for sensitive data

## [0.1.0] - 2024-12-19

### Added
- Initial release of SIGMA AI
- Core functionality for mathematics problem solving
- Multimodal input support (text, images, PDFs)
- Adaptive learning engine
- Real-time diagnostic feedback
- Streamlit web interface
- Google Generative AI integration
- ChromaDB vector database
- PDF processing capabilities
- Custom CSS styling
- Modular page architecture

### Known Issues
- Phase V & VI features (RAG/Search) not yet implemented
- Some features marked as "OFFLINE" in dashboard

---

## Versioning Strategy

- **Major version (X.0.0)**: Breaking changes, major feature additions
- **Minor version (0.X.0)**: New features, backward compatible
- **Patch version (0.0.X)**: Bug fixes, performance improvements

## Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md with new version
3. Create git tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
4. Push tag: `git push origin vX.Y.Z`
5. Create GitHub release with release notes

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute to this project.
