# pdf2djvu-bw

This program converts a PDF file to a [much smaller] black-and-white DjVu file.
Most useful for scanned documents.

Usage: 
```bash
  $ pdf2djvu-bw.py3.py input.pdf output.bw.djvu <resolution> <losslevel>
```

Where <resolution> is the DjVu file resolution in dpi, and <losslevel> is the
DjVu losslevel parameter.

Example:
```bash
  $ pdf2djvu-bw.py3.py scanned-paper.pdf paper.bw.djvu 300  100
```


Suggested values:

for a scanned paper, resolution = 300,  losslevel = 100

for a scanned handwritten document resolution = 400,  losslevel = 20

**Installation for one user**
```bash
   $ mkdir -pv ~/bin
   $ cd ~/bin/
   $ git clone https://gitlab.com/maxim.leyenson/pdf2djvu-bw
```

and then add the lines

```bash
   PATH=$PATH:$HOME/bin/pdf2djvu-bw
   export PATH
```
to your .bashrc file.


**Requirements**

 * djvulibre
 * poppler-utils
 * netpbm-progs

Say, in Fedora Linux you can install them with 

```bash
  $ sudo dnf install -y djvulibre poppler-utils netpbm-progs 
```  

and in Ubuntu you can install the first two packages with
```bash
  $ sudo apt install -y djvulibre-bin
  $ sudo apt install -y poppler-utils 
```  

Then the trouple comes: Ubunutu Linux has an ultra-old version of the netpbm with no pamthreshold.

So do the following:

```bash
   $ sudo apt remove netpbm    # if you have this troubled version installed 
   $ wget https://sourceforge.net/projects/netpbm/files/super_stable/10.73.38/netpbm-sf-10.73.38_amd64.deb

   $ sudo apt install -y libjpeg62       # this is a dep

   $ sudo dpkg -i netpbm-sf-10.73.38_amd64.deb && rm -vf netpbm-sf-10.73.38_amd64.deb
```  

This installs the deb package from the [official NetPBM page, stable releases](http://sourceforge.net/projects/netpbm/files/super_stable/)

[Home page](http://netpbm.sourceforge.net/doc/directory.html)

[Docs on installing netpbm](http://netpbm.sourceforge.net/getting_netpbm.php)


See also the following bugs and discussions:

NetPBM home page says:
    "But if you use Debian or Ubuntu, note that their Netpbm package is
    essentially Netpbm 9.25 from 2002, *minus a bunch of 'unimportant'
    programs. Also note that the Debian version numbering is not
    consistent with Sourceforge Netpbm, so a program may appear to be from
    e.g. Sourceforge Netpbm 10.0, but is actually 9.25. 
 
    In 2002, Debian decided for various reasons not to distribute regular
    Netpbm and instead created its own variation of it. That variation was
    too hard to update with ongoing development on the main branch of
    Netpbm, so no one has done so. .. There is a Debian bug report and
    a Ubuntu bug report about this. The Debian bug report was opened in
    2006 .."

Bug reports:

  * https://bugs.launchpad.net/ubuntu/+source/netpbm-free/+bug/270479  opened in 2008
  * https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=380172 
  

**Remark:** if you would like to get a greyscale or color DjVu file which 
would would keep the
[shades of gray](https://en.wikipedia.org/wiki/Shades_of_gray)
or the colors but would be much larger  in size I suggest to use 
an [excellent pdf2djvu program by Jakub Wilk](http://jwilk.net/software/pdf2djvu).
