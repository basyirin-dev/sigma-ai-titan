# SIGMA AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.52+-red.svg)](https://streamlit.io/)

**AI-Powered Adaptive Assessment Platform for Personalized Mathematics Learning**

SIGMA AI is an intelligent educational platform that provides personalized diagnostic feedback on Mathematics through multimodal AI processing. The system leverages Google's Gemini AI to analyze mathematical problems, generate step-by-step solutions, and deliver adaptive learning experiences.

______________________________________________________________________

## 🚀 Features

### Core Capabilities

- **Multimodal Problem Analysis**: Process mathematical problems from text, images, and PDF documents
- **Adaptive Learning Engine**: Personalized feedback based on individual student performance
- **First-Principles Reasoning**: Deep analytical approach to mathematical problem-solving
- **Real-time Diagnostics**: Instant identification of conceptual gaps and misconceptions

### System Architecture

- **Module A: Titan Solver** - Multimodal first-principles engine for mathematical problem solving
- **Module B: The Archive** - Vectorized knowledge base for comprehensive topic coverage
- **Module C: The Oracle** - RAG-based syllabus expert for curriculum-aligned guidance

### Technical Features

- Streamlit-based web interface
- Google Generative AI integration (Gemini 1.5/3.0)
- ChromaDB vector database for knowledge retrieval
- PDF and image processing capabilities
- Responsive and modern UI design

______________________________________________________________________

## 📦 Installation

### Prerequisites

- Python 3.13 or higher
- pip package manager

### Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/your-username/sigma-ai.git
cd sigma-ai
```

2. **Create and activate virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   Create a `.env` file in the root directory:

```bash
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

5. **Run the application**

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

______________________________________________________________________

## 🏗️ Architecture

### System Overview

```
SIGMA AI Architecture
├── Frontend (Streamlit)
│   ├── Dashboard
│   ├── Titan Solver
│   ├── The Archive
│   └── The Oracle
├── AI Engine (Google Gemini)
│   ├── Multimodal Processing
│   ├── Reasoning Engine
│   └── Response Generation
├── Vector Database (ChromaDB)
│   ├── Knowledge Storage
│   └── Semantic Search
└── Data Pipeline
    ├── PDF Processing
    └── Image Analysis
```

### Data Flow

1. **Input**: User uploads mathematical problem (text, image, or PDF)
1. **Processing**: System processes and standardizes input format
1. **Analysis**: AI engine analyzes problem using first-principles reasoning
1. **Retrieval**: Vector database retrieves relevant knowledge and examples
1. **Generation**: System generates personalized solution and feedback
1. **Output**: Display step-by-step solution with adaptive learning insights

______________________________________________________________________

## 📖 Usage

### Running the Application

```bash
streamlit run app.py
```

### Module Guide

#### ⚡ Titan Solver

- Upload mathematical problems as text, images, or PDFs
- Receive step-by-step solutions with detailed explanations
- Get personalized feedback based on your learning style

#### 📂 The Archive

- Browse comprehensive mathematics knowledge base
- Search for specific topics or concepts
- Access curated examples and practice problems

#### 🧠 The Oracle

- Get curriculum-aligned guidance
- Receive personalized learning recommendations
- Track progress and identify areas for improvement

______________________________________________________________________

## 🛠️ Development

### Project Structure

```
sigma-ai/
├── app.py                 # Main Streamlit application
├── utils.py              # Utility functions (image processing, PDF conversion)
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project metadata
├── .env                  # Environment variables (not committed)
├── .gitignore           # Git ignore rules
├── style.css            # Custom CSS styles
├── pages/               # Streamlit pages
│   ├── 1_⚡_Titan_Solver.py
│   ├── 2_📂_The_Archive.py
│   └── 3_🧠_The_Oracle.py
└── sigma_data/          # Data directory
    ├── ground_truth/    # Training data
    └── raw_pdfs/        # PDF documents
```

### Code Standards

- **Python Version**: 3.13+
- **Formatting**: Black (88-character line limit)
- **Type Hints**: Comprehensive type annotations
- **Documentation**: NumPy docstring format
- **Error Handling**: Try-except blocks with proper logging

### Adding New Features

1. Create a new branch for your feature
1. Implement the feature following code standards
1. Add appropriate tests
1. Update documentation
1. Submit a pull request

______________________________________________________________________

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### How to Contribute

1. Fork the repository
1. Create a feature branch (`git checkout -b feature/amazing-feature`)
1. Commit your changes (`git commit -m 'Add amazing feature'`)
1. Push to the branch (`git push origin feature/amazing-feature`)
1. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Run linting
black .
flake8 .
```

______________________________________________________________________

## 📋 Requirements

### Core Dependencies

- **Streamlit** (>=1.52.0) - Web application framework
- **Google Generative AI** (>=1.0.0) - AI engine
- **ChromaDB** (>=0.6.0) - Vector database
- **PDF2Image** (>=1.17.0) - PDF processing
- **Pillow** (>=12.0.0) - Image processing
- **Python Dotenv** (>=1.0.0) - Environment management

### Optional Dependencies

- **Pandas** (>=2.2.0) - Data analysis
- **NumPy** (>=2.0.0) - Numerical computing

______________________________________________________________________

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# Google AI API Key (Required)
GOOGLE_API_KEY=YOUR_API_KEY_HERE

# Optional Configuration
LOG_LEVEL=INFO
MAX_IMAGE_SIZE=1024
PDF_DPI=200
```

### Streamlit Configuration

The application uses `.streamlit/config.toml` for UI customization:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

______________________________________________________________________

## 🚢 Deployment

### Local Development

```bash
streamlit run app.py
```

### Streamlit Cloud

1. Connect your GitHub repository
1. Set environment variables in Streamlit Cloud dashboard
1. Deploy automatically on push to main branch

### Self-Hosted

```bash
# Using Docker (recommended)
docker build -t sigma-ai .
docker run -p 8501:8501 sigma-ai

# Or using Streamlit
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### Production Considerations

- Set `SERVER_ADDRESS=0.0.0.0` for external access
- Configure reverse proxy (Nginx/Apache)
- Enable HTTPS for secure connections
- Set up monitoring and logging

______________________________________________________________________

## 📊 Performance

### System Requirements

- **CPU**: 2+ cores recommended
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB minimum
- **Network**: Stable internet connection (for AI API)

### Optimization Tips

- Use image compression for large uploads
- Implement caching for frequently accessed data
- Monitor API usage for cost optimization
- Regular database maintenance

______________________________________________________________________

## 🔍 Troubleshooting

### Common Issues

**Issue**: PDF processing fails

- **Solution**: Ensure Poppler is installed and configured in `utils.py`

**Issue**: API authentication errors

- **Solution**: Verify `GOOGLE_API_KEY` is set correctly in `.env`

**Issue**: Memory errors with large files

- **Solution**: Files are automatically resized to 1024px maximum dimension

**Issue**: ChromaDB connection errors

- **Solution**: Ensure proper permissions for database directory

### Getting Help

- Check the [Issues](https://github.com/your-username/sigma-ai/issues) page
- Join our community discussions
- Contact: basyirin.amsyar@example.com

______________________________________________________________________

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Basyirin Amsyar bin Basri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

______________________________________________________________________

## 🙏 Acknowledgments

- **Google Generative AI** - For the powerful AI engine
- **Streamlit** - For the excellent web application framework
- **ChromaDB** - For the vector database technology
- **Open Source Community** - For invaluable tools and libraries

______________________________________________________________________

## 📞 Contact

**Basyirin Amsyar bin Basri**

- Email: basyirin.amsyar@example.com
- GitHub: [@your-username](https://github.com/your-username)

______________________________________________________________________

## 🎯 Roadmap

### Phase V & VI (Planned)

- [ ] Enhanced RAG capabilities
- [ ] Multi-language support
- [ ] Mobile application
- [ ] Advanced analytics dashboard
- [ ] Integration with learning management systems

### Future Enhancements

- [ ] Voice input support
- [ ] Collaborative problem-solving features
- [ ] Automated assessment generation
- [ ] Teacher dashboard and reporting

______________________________________________________________________

**Built with ❤️ using Streamlit and Google Gemini AI**
