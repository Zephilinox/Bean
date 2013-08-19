from time import time
import sys
start = time()
G = ""

def handler():
  global G
  exc_type, exc_value, exc_traceback = sys.exc_info()
  if str(G)!=str(exc_value):
    print("!({0})".format(exc_value))
  G=exc_value

try:
 import process_scripts
except NameError:
 handler()

try:
 import process_mission_tmps
except NameError:
 handler()
 
try:
 import process_game_menus
except NameError:
 handler()
 
try:
 import process_simple_triggers
except NameError:
 handler()
 
try:
 import process_dialogs
except NameError:
 handler()
 
try:
 import process_global_variables_unused
except NameError:
 handler()
 
try:
 import process_postfx
except NameError:
 handler()

print("It took %ss"%(time()-start))