# SIGMA AI // TITAN SYSTEM AUDIT

## 0.1.1 app.py Analysis

### Overview

Main Streamlit application entry point that sets up the system dashboard and navigation.

### Functions

#### `local_css(file_name)`

- **Inputs**:
  - `file_name` (str): Path to CSS file to inject
- **Outputs**: None (side effect only)
- **Side Effects**:
  - Reads the specified CSS file
  - Injects its contents into the Streamlit app using `st.markdown` with `unsafe_allow_html=True`
  - Applies custom styling to the application

### Page Configuration

- **Page Title**: "SIGMA AI // TITAN"
- **Page Icon**: "⚡"
- **Layout**: "wide"
- **Initial Sidebar State**: "expanded"

### Mission Dashboard Components

1. **Title**: "⚡ SIGMA AI // TITAN"
1. **Subtitle**: "### SYSTEM STATUS: OPERATIONAL"
1. **Three-Column Layout** representing system modules:
   - **Column 1 (Module A: SOLVER)**:
     - Header: "MODULE A: SOLVER"
     - Description: "Multimodal First-Principles Engine."
     - Status: "ONLINE" (styled prominently)
   - **Column 2 (Module B: ARCHIVE)**:
     - Header: "MODULE B: ARCHIVE"
     - Description: "Vectorized Knowledge Base."
     - Status: "OFFLINE" (dimmed)
   - **Column 3 (Module C: ORACLE)**:
     - Header: "MODULE C: ORACLE"
     - Description: "RAG-Based Syllabus Expert."
     - Status: "OFFLINE" (dimmed)

## 0.1.2 utils.py Analysis

### Overview

Utility functions for image and PDF processing, LaTeX sanitization, and configuration management.

### Configuration

- **POPPLER_PATH**: Set via environment variable `POPPLER_PATH` (default: None)
- **MAX_IMAGE_SIZE**: From environment variable `MAX_IMAGE_SIZE` (default: 1024)
- **PDF_DPI**: From environment variable `PDF_DPI` (default: 200)

### Functions

#### `process_image(image_input)`

- **Parameters**:
  - `image_input`: Union[UploadedFile, Image.Image] - Image file or PIL Image object
- **Returns**:
  - tuple: (processed_image, status_message)
    - processed_image: PIL.Image.Image or None
    - status_message: "SUCCESS" or error description
- **Functionality**:
  1. Polymorphic opening - handles both PIL Image objects and file uploads
  1. Format standardization - converts RGBA to RGB
  1. Resolution cap - applies "1024 Rule" limiting max dimension to 1024px
- **Side Effects**: None
- **Notes**:
  - Does not perform any Gemini API calls
  - Pure image processing pipeline

#### `convert_pdf_to_image(pdf_bytes)`

- **Parameters**:
  - `pdf_bytes` (bytes): PDF file content as bytes
- **Returns**:
  - tuple: (image, status_message)
    - image: PIL.Image.Image or None
    - status_message: "SUCCESS", "PDF_EMPTY", or "PDF_ERROR: <details>"
- **Functionality**:
  1. Uses pdf2image.convert_from_bytes to convert first page of PDF to image
  1. Configurable DPI and Poppler path via environment variables
  1. Only processes first page (first_page=1, last_page=1)
- **Side Effects**: None
- **Notes**:
  - Does not perform any Gemini API calls
  - Pure PDF-to-image conversion pipeline

#### `sanitize_latex(text: str) -> str`

- **Parameters**:
  - `text` (str): LaTeX text to sanitize
- **Returns**:
  - str: Standardized LaTeX with proper delimiters for Streamlit
- **Functionality**:
  1. Converts [ ] to $$
  1. Converts ( ) to $
  1. Adds newlines around block math
  1. Cleans up excessive newlines
- **Side Effects**: None
- **Notes**:
  - Does not perform any Gemini API calls
  - Text processing utility for LaTeX formatting

### Gemini API Usage

**NO GEMINI API CALLS FOUND IN utils.py**
The utils.py file contains only image processing, PDF conversion, and text sanitization utilities. All Gemini API interactions must occur in the page files or other modules.

### Technical Debt Identified

1. Hardcoded max dimension of 1024 pixels in process_image() (though configurable via env var)
1. PDF processing limited to first page only
1. No async processing capabilities for large files

## 0.1.3 Page Files Analysis

Based on the available mock data and logic files, the system appears to be designed with the following structure:

### Page Files Purpose

The three page files (`1_⚡_Titan_Solver.py`, `2_📂_The_Archive.py`, `3_🧠_The_Oracle.py`) are intended to represent the three core modules of the system:

- **Titan Solver (Module A)**: Multimodal problem-solving engine
- **The Archive (Module B)**: Vectorized knowledge base/storage system
- **The Oracle (Module C)**: RAG-based syllabus expert system

### Data Flow Architecture

Based on `mock_logic.py` and `test_cases.json`:

1. **Input Routing** (`get_smart_response` function):

   - Checks uploaded filename for keywords (geometry, algebra, graph, handwritten, trick, trial/pdf)
   - Falls back to checking user prompt for trigger keywords from test cases
   - Routes to appropriate scenario: algebra, geometry, graph, handwritten, trick, pdf_test, failure_test, or general

1. **Response Generation**:

   - Retrieves pre-written responses from `test_cases.json` based on scenario
   - Includes LaTeX-formatted mathematical solutions with step-by-step explanations
   - Provides follow-up clarification capability for explanatory questions

1. **Thought Chain Simulation**:

   - `mock_data.py` contains `THOUGHT_CHAINS` that simulate the internal reasoning steps
   - Different chains for different problem types (calculus, geometry, algebra, graph, pdf_test, general, failure_test)

### Expected Functionality (Based on Mocks)

While the actual page files appear to be corrupted Windows shortcuts in the repository, the intended functionality based on supporting files is:

1. **Titan Solver Page** (`1_⚡_Titan_Solver.py`):

   - Primary interface for solving mathematical problems
   - Accepts image uploads (handwritten problems, diagrams, etc.)
   - Uses Gemini API for multimodal understanding
   - Routes problems to appropriate solvers based on detected keywords/content
   - Returns step-by-step solutions with LaTeX-formatted mathematics

1. **The Archive Page** (`2_📂_The_Archive.py`):

   - Knowledge base management interface
   - Allows storage and retrieval of solved problems
   - Vector embedding system for similarity search
   - Metadata tagging and categorization

1. **The Oracle Page** (`3_🧠_The_Oracle.py`):

   - RAG-based expert system for syllabus-specific questions
   - Curriculum-aligned explanations and examples
   - Syllabus tracking and progression mapping
   - Contextual help based on educational level/curriculum

### Technical Debt Identified in Page Files

1. Files appear to be corrupted Windows shortcuts instead of actual Python code
1. Missing implementation of actual Gemini API integration
1. Missing actual multimodal processing pipelines
1. Missing actual vector storage/retrieval systems

## 0.1.4 Ground Truth Data Analysis

### File Catalog

- **sigma_data/ground_truth/2025_mrsm_physics.json**
  - **Format**: JSON
  - **Content**:
    - Metadata: Year (2025), Exam Type (TRIAL), Source (MRSM), Subject (PHYSICS), Paper (2), Language (BILINGUAL EN/MS)
    - Questions: Q5, Q6, Q8, Q9, Q11 (covering Forces and Motion, Light and Optics, Electronics, Electricity, Momentum & Impulse)
    - Each question includes:
      - Visual assets with descriptions and filenames
      - Multiple parts (a, b, c, d, etc.) with text, marks, answer type, and detailed solutions
      - Oracle insights highlighting common mistakes and key concepts

### Consumption Pattern

The ground truth data appears to be used as:

1. Reference for creating mock test cases in `test_cases.json`
1. Source for visual asset filenames that would be matched against uploaded files
1. Basis for step-by-step solutions and explanations provided in the mock responses
1. Reference for difficulty levels and topic organization

## 0.1.5 Raw PDFs Analysis

### Directory Status

- **sigma_data/raw_pdfs/**: Directory does not exist
- **Implication**: No raw PDF files are currently available in the repository for processing

### Expected Content

Based on the ground truth data and mock logic, the raw PDFs directory would likely contain:

- MRSM Physics Trial Papers (referenced in ground truth as "2025_MRSM_Q\*.jpg" visual assets)
- Scan of physics examination papers with diagrams and problems
- Visual assets referenced in the ground truth JSON (e.g., "2025_MRSM_Q5_COWS.jpg", "2025_MRSM_Q6_LENSES.jpg")
