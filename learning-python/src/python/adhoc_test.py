text = "X-DSPAM-Confidence:    0.8475";
ipos = text.find(' ');
val = text[ipos:].strip()
text.upper()
print float(val)