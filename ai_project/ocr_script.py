import cv2
import pytesseract

# Windows only (adjust path!)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('sample_text.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
cv2.imwrite('gray.png', gray)
cv2.imwrite('blur.png', blur)
cv2.imwrite('thresh.png', thresh)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(thresh, config=custom_config)
print("\n=== EXTRACTED TEXT ===\n", text)

data = pytesseract.image_to_data(thresh, config=custom_config, output_type=pytesseract.Output.DICT)
print("\n=== WORDS WITH >=80% CONFIDENCE ===\n")
for i in range(len(data['text'])):
    word = data['text'][i]
    conf = int(data['conf'][i])
    if word.strip() and conf >= 80:
        print(f"Word: {word}, Confidence: {conf}%")