import string
import types

# Dunde's ============================================
pro_ver = "v0.092"
signature = "dunde"

# Protection options
script_protection       = 0 # set it to 1, scripts numbering will be removed from scripts.txt.
variable_protection     = 0 # set it to 1, variables.txt and variable_uses.txt will be deleted at compiling time
dialog_state_protection = 0 # set it to 1, dialog_states.txt will be deleted at compiling time
string_protection       = 0 # set it to 1, strings id will be cut into minimalis morm

# More options
use_wse                 = 0 # set it to 0 if you don't use WSE. (Note : this must be set to 1 if you want to use generic on shield hit on process_items.py) 
export_imod_data        = 1 # set it to 1 to export item_modifiers.txt from module_item_modifiers.py
export_constants        = 1 # set it to 1 to export slot_*, *_begin and *_end of module_constants.py to id_constants.py
ignore_troop_get_type   = 1 # set it to 0 if you want every troop_get_type operation should be followed by val_and operation (useful for mods with custom skins only)

# initializations, in case there's no WSE SDK installed
if use_wse==0:
  try_for_attached_parties = 15 # WSE
  try_for_active_players   = 16 # WSE
  try_for_prop_instances   = 17 # WSE
  try_for_dict_keys        = 18 # WSE

sign_length = len(signature)  
# Dunde's ============================================

def convert_to_identifier(s0):
  s1 = string.replace(s0," ","_")
  s2 = string.replace(s1,"'","_")
  s3 = string.replace(s2,"`","_")
  s4 = string.replace(s3,"(","_")
  s5 = string.replace(s4,")","_")
  s6 = string.replace(s5,"-","_")
  s7 = string.replace(s6,",","")
  s8 = string.replace(s7,"|","")
  s9 = string.replace(s8,"\t","_") #Tab
  s10 = string.lower(s9)
  return s10

def convert_to_identifier_with_no_lowercase(s0):
  s1 = string.replace(s0," ","_")
  s2 = string.replace(s1,"'","_")
  s3 = string.replace(s2,"`","_")
  s4 = string.replace(s3,"(","_")
  s5 = string.replace(s4,")","_")
  s6 = string.replace(s5,"-","_")
  s7 = string.replace(s6,",","")
  s8 = string.replace(s7,"|","")
  s9 = string.replace(s8,"\t","_") #Tab
  return s9

def replace_spaces(s0):
  return string.replace(string.replace(s0,"\t","_")," ","_")
