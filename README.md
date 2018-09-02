# pdf2djvu-bw

This program converts a PDF file to a [much smaller] black-and-white DjVu file.
Most useful for scanned documents.

Usage: 
```bash
  $ pdf2djvu-bw.py input.pdf output.bw.djvu <resolution> <losslevel>
```

Where <resolution> is the DjVu file resolution in dpi, and <losslevel> is the
DjVu losslevel parameter.

Example:
```bash
  $ pdf2djvu-bw.py scanned-paper.pdf paper.bw.djvu 300  100
```


Suggested values:

for a scanned paper, resolution = 300,  losslevel = 100

for a scanned handwritten document resolution = 400,  losslevel = 20


Requires: djvulibre, poppler-utils, netpbm-progs

Say, in fedora Linux you can install them with 

```bash
  $ sudo dnf install -y djvulibre poppler-utils netpbm-progs 
```  


**Remark:** if you would like to get a greyscale or color DjVu file which 
would would keep the
[shades of gray](https://en.wikipedia.org/wiki/Shades_of_gray)
or the colors but would be much larger  in size I suggest to use 
an [excellent pdf2djvu program by Jakub Wilk](http://jwilk.net/software/pdf2djvu).