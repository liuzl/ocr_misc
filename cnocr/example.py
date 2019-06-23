import sys
from cnocr import CnOcr
ocr = CnOcr()
res = ocr.ocr(sys.argv[1])
print("Predicted Chars:", res)
