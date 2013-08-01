import string

from module_info import *
from module_presentations import *
from ID_meshes import *

from process_common import *
from process_operations import *

def save_presentations(variable_list,variable_uses,tag_uses,quick_strings):
  ofile = open(export_dir + "presentations.txt","w")
  ofile.write("presentationsfile version 1\n")
  ofile.write(" %d\n"%(len(presentations)))
  i_prsnt=0
  for presentation in presentations:
    #ofile.write("prsnt_%s %d %d "%(presentation[0], presentation[1], presentation[2]))
    if ((presentation[0].startswith("game_")) or (presentation[0].startswith("multiplayer_"))):
      ofile.write("prsnt_%s %d %d "%(presentation[0], presentation[1], presentation[2]))
    else:  
      #ofile.write("%s %d %d "%(signature[(find_object(presentations,presentation[0]))%sign_length], presentation[1], presentation[2]))
      ofile.write("prsnt_%s %d %d "%(str(i_prsnt), presentation[1], presentation[2]))
    save_simple_triggers(ofile,presentation[3], variable_list,variable_uses,tag_uses,quick_strings,"prsnt_"+presentation[0])
    ofile.write("\n")
    i_prsnt+=1
  ofile.close()


def save_python_header():
  file = open("./ID_presentations.py","w")
  for i_presentation in xrange(len(presentations)):
    file.write("prsnt_%s = %d\n"%(presentations[i_presentation][0],i_presentation))
  file.close()

print "Exporting presentations..."
save_python_header()
variable_uses = []
variables = load_variables(export_dir,variable_uses)
tag_uses = load_tag_uses(export_dir)
quick_strings = load_quick_strings(export_dir)
save_presentations(variables,variable_uses,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_tag_uses(export_dir,tag_uses)
save_quick_strings(export_dir,quick_strings)
