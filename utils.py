import re

from pdf2image import convert_from_bytes
from PIL import Image

# --- CONFIGURATION ---
import os

# Poppler path - set via environment variable for cross-platform compatibility
POPPLER_PATH = os.getenv("POPPLER_PATH", None)

# Default configuration values
MAX_IMAGE_SIZE = int(os.getenv("MAX_IMAGE_SIZE", "1024"))
PDF_DPI = int(os.getenv("PDF_DPI", "200"))


def process_image(image_input):
    """
    The Airlock: Sanitizes and optimizes user images.

    Accepts:
    1. StreamlitUploadedFile (Raw upload)
    2. PIL.Image.Image (Already opened PDF page or image)

    Parameters
    ----------
    image_input : Union[UploadedFile, Image.Image]
        Image file or PIL Image object

    Returns
    -------
    tuple
        (processed_image, status_message)
        - processed_image: PIL.Image.Image or None
        - status_message: "SUCCESS" or error description

    Raises
    ------
    Exception
        If image processing fails

    Examples
    --------
    >>> image, status = process_image(uploaded_file)
    >>> if status == "SUCCESS":
    ...     # Use the image
    ...     pass
    """
    try:
        # 1. POLYMORPHIC OPENING
        # If it's already a PIL Image (from PDF converter or app.py), just use it.
        if isinstance(image_input, Image.Image):
            image = image_input
        else:
            # If it's a file upload, open it.
            image = Image.open(image_input)

        # 2. Format Standardization (RGBA -> RGB)
        if image.mode != "RGB":
            image = image.convert("RGB")

        # 3. Resolution Cap (The "1024 Rule")
        max_dimension = 1024
        if max(image.size) > max_dimension:
            # Create a copy to resize (safeguard)
            image = image.copy()
            image.thumbnail((max_dimension, max_dimension))

        return image, "SUCCESS"

    except Exception as e:
        return None, str(e)


def convert_pdf_to_image(pdf_bytes):
    """
    Converts the first page of a PDF into a PIL Image.

    Parameters
    ----------
    pdf_bytes : bytes
        PDF file content as bytes

    Returns
    -------
    tuple
        (image, status_message)
        - image: PIL.Image.Image or None
        - status_message: "SUCCESS", "PDF_EMPTY", or "PDF_ERROR: <details>"

    Examples
    --------
    >>> image, status = convert_pdf_to_image(pdf_file_bytes)
    >>> if status == "SUCCESS":
    ...     # Use the image
    ...     pass
    """
    try:
        images = convert_from_bytes(
            pdf_bytes, dpi=PDF_DPI, poppler_path=POPPLER_PATH, first_page=1, last_page=1
        )
        if images:
            return images[0], "SUCCESS"
        return None, "PDF_EMPTY"
    except Exception as e:
        return None, f"PDF_ERROR: {str(e)}"


def sanitize_latex(text: str) -> str:
    """Standardizes LaTeX delimiters for Streamlit."""
    if not text:
        return ""

    # Convert \[ \] to $$
    text = re.sub(r"\\\[(.*?)\\\]", r"$$\1$$", text, flags=re.DOTALL)
    # Convert \( \) to $
    text = re.sub(r"\\\((.*?)\\\)", r"$\1$", text, flags=re.DOTALL)
    # Add newlines around block math
    text = text.replace("$$", "\n$$\n")
    return re.sub(r"\n{3,}", "\n\n", text).strip()
