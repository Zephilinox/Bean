import string
from header_common import *
from module_info import *
from module_strings import *

from process_common import *

def save_strings(strings):
  ofile = open(export_dir + "strings.txt","w")
  ofile.write("stringsfile version 1\n")
  ofile.write("%d\n"%len(strings))
  for i_string in xrange(len(strings)):
    strx = strings[i_string]  
    if (string_protection==0):
      ofile.write("str_%s %s\n"%(convert_to_identifier(strx[0]),replace_spaces(strx[1])))
    else:
      ofile.write("str_%s %s\n"%(str(i_string),replace_spaces(strx[1]))) # Dunde cuts the strings.txt size
  ofile.close()

def save_python_header():
  ofile = open("./ID_strings.py","w")
  for i_string in xrange(len(strings)):
    ofile.write("str_%s = %d\n"%(convert_to_identifier(strings[i_string][0]),i_string))
  ofile.write("\n\n")
  ofile.close()

print "Exporting strings..."
save_python_header()
save_strings(strings)
  
