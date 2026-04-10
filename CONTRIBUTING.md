# Contributing to SIGMA AI

Thank you for your interest in contributing to SIGMA AI! We welcome contributions from the community and are pleased to have you join us.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)
- [Documentation](#documentation)
- [Community](#community)

## 🌟 Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [basyirin.amsyar@example.com](mailto:basyirin.amsyar@example.com).

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- Git
- GitHub account

### Fork the Repository

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/sigma-ai.git
   cd sigma-ai
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/your-username/sigma-ai.git
   ```

## 🤝 How to Contribute

### Ways to Contribute

1. **Bug Reports**: Report bugs by creating issues
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Fix bugs or implement new features
4. **Documentation**: Improve documentation and tutorials
5. **Testing**: Write tests and improve test coverage
6. **Community**: Help other users and contributors

### Contribution Workflow

1. Find an issue or create one
2. Comment on the issue to let others know you're working on it
3. Fork the repository and create a feature branch
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request
7. Address review feedback
8. Celebrate your contribution! 🎉

## 🔧 Development Setup

### Clone and Setup

```bash
# Clone the repository
git clone https://github.com/your-username/sigma-ai.git
cd sigma-ai

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development
```

### Environment Variables

Create a `.env` file:
```bash
GOOGLE_API_KEY=your_api_key_here
```

### Run the Application

```bash
streamlit run app.py
```

## 📝 Coding Standards

### Python Style Guide

- **Python Version**: 3.13+
- **Formatting**: Black (88-character line limit)
- **Linting**: Ruff for static analysis
- **Type Hints**: Comprehensive type annotations required
- **Documentation**: NumPy docstring format

### Code Formatting

Before submitting code, run:
```bash
# Format code
black .

# Lint code
ruff check .

# Type check (if applicable)
mypy .
```

### Commit Messages

Use descriptive commit messages following this format:
```
<type>: <short description>

<optional detailed description>

<optional footer with issue references>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Maintenance tasks

Example:
```
feat: add PDF processing support

Implement PDF to image conversion using pdf2image library.
Add error handling for corrupted PDF files.

Fixes #42
```

### File Structure

Follow the existing project structure:
```
sigma-ai/
├── app.py                 # Main application
├── utils.py              # Utility functions
├── pages/                # Streamlit pages
├── tests/                # Test files
├── docs/                 # Documentation
└── sigma_data/           # Data directory
```

## 📦 Pull Request Process

### Creating a Pull Request

1. **Branch Naming**:
   - Use descriptive names: `feature/add-pdf-support`, `fix/login-bug`
   - Prefix with type: `feature/`, `fix/`, `docs/`, `refactor/`

2. **Commit History**:
   - Squash related commits
   - Rebase on main branch before submitting
   - Keep commit history clean

3. **PR Description**:
   - Include clear title and description
   - Reference related issues
   - Describe testing performed
   - Include screenshots for UI changes

4. **Testing**:
   - Ensure all tests pass
   - Add new tests for new features
   - Test edge cases

### Review Process

1. **Automated Checks**:
   - CI/CD pipeline must pass
   - Code coverage requirements met
   - No security vulnerabilities

2. **Code Review**:
   - At least one maintainer approval required
   - Address all review comments
   - Be responsive to feedback

3. **Merge**:
   - Squash and merge for feature branches
   - Rebase and merge for bug fixes
   - Update documentation if needed

## 🐛 Reporting Issues

### Bug Reports

Use the bug report template when creating issues:

**Title**: Clear, descriptive title

**Description**:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment (OS, Python version, etc.)
- Screenshots if applicable
- Error logs

**Labels**: Use appropriate labels (bug, critical, etc.)

### Security Issues

For security vulnerabilities, please email [basyirin.amsyar@example.com](mailto:basyirin.amsyar@example.com) directly instead of creating a public issue.

## 💡 Feature Requests

### Suggesting Features

1. **Check Existing Issues**: Search for similar features
2. **Use Feature Template**: Fill out the feature request template
3. **Provide Details**:
   - Problem statement
   - Proposed solution
   - Use cases
   - Alternatives considered

### Feature Request Template

```markdown
## Problem
[Description of the problem]

## Proposed Solution
[Description of the proposed solution]

## Use Cases
- [Use case 1]
- [Use case 2]

## Alternatives
[Alternative solutions considered]
```

## 📚 Documentation

### Documentation Standards

- Use clear, concise language
- Include code examples
- Update docstrings for changed functions
- Keep README.md up to date

### Documentation Files

- **README.md**: Project overview and quick start
- **CONTRIBUTING.md**: This file
- **CODE_OF_CONDUCT.md**: Community guidelines
- **API Documentation**: Auto-generated from docstrings

### Writing Documentation

1. **Function Docstrings**:
```python
def process_image(image_input):
    """
    The Airlock: Sanitizes and optimizes user images.

    Parameters
    ----------
    image_input : Union[UploadedFile, Image.Image]
        Image file or PIL Image object

    Returns
    -------
    tuple
        (processed_image, status_message)

    Raises
    ------
    Exception
        If image processing fails
    """
```

2. **Module Docstrings**: Include overview and important classes/functions

3. **Inline Comments**: Explain complex logic, not obvious operations

## 🧪 Testing

### Test Structure

```
tests/
├── __init__.py
├── test_utils.py
├── test_app.py
└── test_pages/
    ├── test_titan_solver.py
    ├── test_archive.py
    └── test_oracle.py
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_utils.py

# Run with coverage
python -m pytest --cov=.

# Run in verbose mode
python -m pytest -v
```

### Test Coverage

- Aim for 80%+ code coverage
- Test edge cases and error conditions
- Mock external API calls
- Use test fixtures for common setup

## 📊 Code Review Guidelines

### For Reviewers

1. **Be Respectful**: Provide constructive feedback
2. **Be Thorough**: Review all changes
3. **Be Helpful**: Suggest improvements
4. **Be Timely**: Respond within 2-3 days

### For Contributors

1. **Be Open**: Accept feedback gracefully
2. **Be Responsive**: Address comments promptly
3. **Be Patient**: Review takes time
4. **Be Clear**: Explain your reasoning

## 🚢 Deployment

### Release Process

1. **Versioning**: Follow Semantic Versioning (MAJOR.MINOR.PATCH)
2. **Changelog**: Update CHANGELOG.md for each release
3. **Git Tag**: Create annotated tag for release
4. **GitHub Release**: Create GitHub release with notes

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in pyproject.toml
- [ ] Git tag created
- [ ] GitHub release created

## 🌍 Community

### Communication Channels

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and community talk
- **Email**: [basyirin.amsyar@example.com](mailto:basyirin.amsyar@example.com)

### Getting Help

1. **Search First**: Check existing issues and discussions
2. **Be Specific**: Include all relevant details
3. **Be Patient**: Community members volunteer their time
4. **Be Grateful**: Thank those who help you

### Recognition

Contributors will be recognized in:
- Release notes
- Contributors list in README.md
- GitHub Contributors page

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Thank you for taking the time to contribute to SIGMA AI. Your efforts help make mathematics education more accessible and personalized for students worldwide.

---

**Happy Contributing! 🚀**
