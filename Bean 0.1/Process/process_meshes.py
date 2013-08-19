import string
from header_common import *
from module_info import *
from module_meshes import *

from process_common import *
from process__swyhelper import *

def save_meshes():
  ofile = open(export_dir + "meshes.txt","w")
  ofile.write("%d\n"%len(meshes))
  for i_mesh in xrange(len(meshes)):
    mesh = meshes[i_mesh]
    ofile.write("mesh_%s %d %s %s %s %s %s %s %s %s %s %s\n"%(mesh[0],mesh[1],replace_spaces(mesh[2]),swytrailzro(mesh[3]),swytrailzro(mesh[4]),swytrailzro(mesh[5]),swytrailzro(mesh[6]),swytrailzro(mesh[7]),swytrailzro(mesh[8]),swytrailzro(mesh[9]),swytrailzro(mesh[10]),swytrailzro(mesh[11])))
  ofile.close()

def save_python_header():
  ofile = open("./ID/ID_meshes.py","w")
  for i_mesh in xrange(len(meshes)):
    ofile.write("mesh_%s = %d\n"%(meshes[i_mesh][0],i_mesh))
  ofile.write("\n\n")
  ofile.close()

print "Exporting meshes..."
save_python_header()
save_meshes()
