# 특별 경로 조작
import sys, os

if "code" not in os.path.abspath("."):
    sys.path = [p for p in sys.path if "PythonMistakes" not in p]

# "표준" 프로그램
import re

pat = re.compile("hello", re.I)
s = "Hello World!"
if re.match(pat, s):
    print(s)
