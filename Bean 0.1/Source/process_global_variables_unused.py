from module_info import *
from process_common import *
from process_operations import *


print "Checking global variable usages..."
variable_uses = []
variables = load_variables(export_dir,variable_uses)
i = 0
while (i < len(variables)):
  if (variable_uses[i] == 0):
    if (not variables[i].startswith("$")):
      print "WARNING: Global variable never used    : $" + variables[i]
    else:
      print "WARNING: Global variable never assigned: "  + variables[i]
  i = i + 1
