#!/usr/bin/python3

# by Maxim Leyenson, <leyenson@gmail.com>
# under the BSD 4-clause license

# requires 'djvulibre', 'poppler-utils' for  'pdftoppm',
# 'netpbm-progs' for 'pamthreshold'

import sys  # to read command line arguments
import os   # to run system commands in shell
import tempfile
import subprocess

# -- getting the options (i.e. input.pdf output.djvu)
try:
    filename =   sys.argv[1];
    output   =   sys.argv[2];
    resolution = sys.argv[3];
    losslevel =  sys.argv[4];
except:
    print('Usage: %s input.pdf output.djvu resolution losslevel ' % sys.argv[0]);  #  sys.argv[0] = program name
    print('suggested resolution 300dpi losslevel 100') ;
    sys.exit(1) 
 

# ---------------- numberOfPagesInPdfFile function --------

# requires poppler-utils  (for pdfinfo)


def numberOfPagesInPdfFile(filename):
    print("[computing number of pages in pdf file]")
    command ="pdfinfo " + filename + " | grep --text Pages | sed 's/Pages://g;' "

    #  --text: for some ridiculous reason, grep sometimes thinks that pdfinfo output is binary
    print("   executing ", command)
    pages = subprocess.getoutput(command)
    print("[got ", pages, " pages]")
    pages = int(pages)
    print("[int() = ", pages, "]")
    return pages


#--  pdftoppm converts to pgm and ppm very well, but not to pbm

firstpage = 1
lastpage = numberOfPagesInPdfFile(filename)

tempfolder = tempfile.mkdtemp()
print("using temporary folder ", tempfolder)

#-- pdf -> pgm -> pbm -> djvu


for i in range (firstpage,lastpage+1):   # 1-(n-1)
    print("--------------- Page", str(i), "/", lastpage, "---------------")
    print("(converting page to pgm with given resolution )")
    cmd = 'pdftoppm -f ' + str(i) + ' -l ' + str(i)     # first and last pages
    cmd = cmd + ' -r ' + resolution                     # resolution in dpi
    cmd = cmd + ' -gray ' + filename + ' ' + tempfolder + '/a'
    os.system(cmd)
# -- created tempfolder/a-(number).pgm; has very strange name conventions;
    pgmName  = tempfolder + '/' + str(i) + '.pgm'
    pbmName  = tempfolder + '/' + str(i) + '.pbm'
    djvuName = tempfolder + '/' + str(i) + '.djvu'    
    os.system('mv ' + tempfolder + '/a-*.pgm ' + pgmName)  # ok!
    print("(converting pamthreshold: pgm -> pam, pamtopnm: pam -> pbm...)")
    cmd='pamthreshold ' + pgmName + ' | pamtopnm > ' + pbmName
    os.system(cmd)
    print("(converting pbm to djvu: )")
# invoking cjb2; main
    cmd = 'cjb2 -dpi '
    cmd = cmd + resolution
    cmd = cmd + ' -losslevel '
    cmd = cmd + losslevel
    cmd = cmd + ' -verbose ' + pbmName + ' ' + djvuName
    print('[', cmd, ']')
    os.system(cmd)
    os.system('rm -vf ' + tempfolder + '*pbm')
    os.system('rm -vf ' + pgmName)
    os.system('rm -vf ' + pbmName)


# -- displaying tempfolder
print("the current contents of ", tempfolder)
os.system("ls " + tempfolder) 


# ---- making filelist to assemble ----

filelist = ""
for i in range (firstpage,lastpage+1):   # 1-(n-1)
    filelist = filelist + " " + tempfolder + "/" + str(i) + ".djvu"

print("filelist: ", filelist)
print("(--------------------------)")

# --------- collecting djvus ----------------
print("(collecting djvus with djvm)")

newName = os.getcwd() + '/' + output;

cmd = "djvm -c " + newName + filelist
print("(", cmd, ")")
result = os.system(cmd)    # = 0, if successful
if result == 0:
    print("(produced", newName, ")")
    print("(cleaning...)")
    os.system("rm -rvf " + tempfolder )
    print("(Done...)")    
else:
    print("---------------------------------------------------------")
    print("(FAILED)")
    print("(TEMPORARY FOLDER", tempfolder, "NOT CLEANED!)")
    print("---------------------------------------------------------")


# ----------------------------------------
    
# running 'cd' before djvm is necessary, since otherwise all filenames start with /tmp/djvu, and
# sort -n gets confused for some unclear reason

# ----------------------------------------
    
