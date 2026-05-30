# OCR Image Text Recognition Project

**Project 4 – Image/Text Recognition (Basic) | AI Engineer Milestone**

---

## Project Overview

This project demonstrates a simple Python pipeline to automatically extract text from images (JPG/PNG, etc.) using the pre-trained Tesseract OCR engine.  
Here, we show how artificial intelligence can interpret visual data and convert it to machine-readable text, moving beyond rule-based or purely tabular AI.

---

## Features

- Extracts readable text from scanned documents, photos, bills, receipts, etc.
- Uses grayscale, Gaussian blur, and adaptive thresholding as image preprocessing for improved OCR accuracy.
- Displays and filters only high-confidence (80%+) results.
- Built with Python, OpenCV, and pytesseract (Python wrapper for Google's Tesseract OCR).

---

## Requirements

- Python 3.x
- **Tesseract-OCR software**  
  [Download for Windows](https://github.com/tesseract-ocr/tesseract/releases)
- Python libraries:
    - pytesseract
    - opencv-python

**How to install:**
```bash
pip install pytesseract opencv-python
```
Make sure Tesseract-OCR is installed on your system and its path is correctly set in the script.

---

## Usage

1. Place your test image (e.g., `sample_text.png`) in the project folder.
2. Open the `ocr_script.py` file.
3. Edit this line to match the actual path to Tesseract on your computer (for Windows):

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

4. Run the script:

```bash
python ocr_script.py
```

5. The extracted text and only high-confidence (≥80%) words will appear in the console.
6. Intermediate pre-processed images (`gray.png`, `blur.png`, `thresh.png`) are also saved for visual verification.

---

## Example

**Input:**  
A screenshot or photo with printed text.

**Console Output:**
```
=== EXTRACTED TEXT ===
Welcome to AI Lab!
Invoice No: 01234
Total: Rs. 450
Thank you!
```

**Only High-Confidence Words:**
```
Word: Welcome, Confidence: 96%
Word: Invoice, Confidence: 99%
Word: Total, Confidence: 90%
...
```

---

## Project Structure

```
ai_project4_ocr/
|-- ocr_script.py
|-- sample_text.png
|-- gray.png
|-- blur.png
|-- thresh.png
|-- README.md
```

---

## Notes

- OCR accuracy depends on image quality and text clarity.
- Only words detected with 80%+ confidence are shown (you can adjust this threshold).
- Intermediate images can help debug and prove your processing steps.

---

## Milestone Checklist

- [x] Tesseract OCR integrated without errors
- [x] Image preprocessing (grayscale, blur, threshold) implemented
- [x] Script processes a sample image
- [x] 80%+ confidence filter active
- [x] Output and intermediate images saved for validation

---

## Credits

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
- [pytesseract (Python OCR wrapper)](https://pypi.org/project/pytesseract/)

---

**Contact:**  
If you face any errors or need help, open an issue on this repository or contact the maintainer.
