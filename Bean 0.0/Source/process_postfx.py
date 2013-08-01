from header_common import *
from module_info import *
from module_postfx import *

def write_python_header(postfx_params_list):
  file = open("./ID_postfx_params.py","w")
  for i_postfx_param in xrange(len(postfx_params_list)):
    file.write("pfx_%s = %d\n"%(postfx_params_list[i_postfx_param][0],i_postfx_param))
  file.write("\n\n")
  file.close()

def write_postfx_params(postfx_params_list):
  ofile = open(export_dir + "postfx.txt","w")
  ofile.write("postfx_paramsfile version 1\n")
  ofile.write("%d\n"%len(postfx_params_list))
  for postfx_param in postfx_params_list:
    ofile.write("pfx_%s %d %d"%(postfx_param[0], postfx_param[1],postfx_param[2]))
    params_list1 = postfx_param[3]
    params_list2 = postfx_param[4]
    params_list3 = postfx_param[5]
    ofile.write("  %f %f %f %f"%(params_list1[0], params_list1[1], params_list1[2], params_list1[3]))
    ofile.write("  %f %f %f %f"%(params_list2[0], params_list2[1], params_list2[2], params_list2[3]))
    ofile.write("  %f %f %f %f\n"%(params_list3[0], params_list3[1], params_list3[2], params_list3[3]))
  ofile.close()

print "Exporting postfx_params..."
write_postfx_params(postfx_params)
write_python_header(postfx_params)  
  
# Dunde's Protection
from process_common import *
from process_operations import *
import os  
  
def cut_quick_strings(export_dir, quick_strings):
  file = open(export_dir + "quick_strings.txt", "w")
  file.write("%d\n"%len(quick_strings))
  for i in xrange(len(quick_strings)):
    #file.write("%s %s\n"%(signature[i%sign_length],replace_spaces(quick_strings[i][1])))
    file.write("qstr_%s %s\n"%(str(i),replace_spaces(quick_strings[i][1])))
  file.close()  
  
# Dunde's Protection
if variable_protection==1:
  print "Deleting variables.txt..."
  try:
    os.remove(export_dir + 'variables.txt')
  except:
    print "variables.txt 's not found..."
  print "Deleting variable_uses.txt..."  
  try:
    os.remove(export_dir + 'variable_uses.txt')
  except:
    print "variable_uses.txt 's not found..."
  print "Deleting dialog_states.txt..." 
if dialog_state_protection==1:  
  try:
    os.remove(export_dir + 'dialog_states.txt')
  except:
    print "dialog_states.txt 's not found..."  
if string_protection==1:
  print "Cut quickstrings.txt size..."
  quick_strings = load_quick_strings(export_dir)
  cut_quick_strings(export_dir,quick_strings)


def remove_all_spaces_and_tabs(s0):
  s1 = string.replace(s0," ","")
  s2 = string.replace(s1,"\t","") #Tab
  s3 = string.lower(s2)
  return s3

if export_constants==1:  
  print "Exporting slot related constants"  
  ifile = open("./module_constants.py","r")
  ofile = open("./ID_constants.py","w")
  while 1:
    line = ifile.readline()
    if not line  :
      break     
    clear_line = remove_all_spaces_and_tabs(line)
    if clear_line[0]<>"#":
      signed_line = clear_line.partition("=")
      if (signed_line[2]<>""):
        if (signed_line[0].find("slot_")==0)|(signed_line[0].endswith("begin"))|(signed_line[0].endswith("end")):
          line_is_valid = 1
          try:
            line_value = eval(signed_line[0])
          except:
            line_is_valid = 0
          if line_is_valid==1:            
            if type(line_value)==str:
              try:
                line_value_value = eval(line_value)
              except:
                line_is_valid = 0
              if line_is_valid==1:              
                ofile.write("%s %s %s\n"%(signed_line[0] + " = ", str(line_value_value)+ " # = ", line_value ))
            else:
              ofile.write("%s %s\n"%(signed_line[0]+ " = ", str(line_value)))
  ifile.close()
  ofile.close()        
        