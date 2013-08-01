import string

from process_common import *
from module_items import *

# Dunde's Generic on shield hit BEGIN
#generic_on_shield_hit = ()
if use_wse==1:
  generic_on_shield_hit = (ti_on_shield_hit, 
    [(store_trigger_param_1, ":victim_id"),      # Trigger Param 1: receiver agent no
    (store_trigger_param_2, ":attacker_id"),    # Trigger Param 2: dealer agent no
	(store_trigger_param, ":missile_id", 7),    # Trigger Param 7: missile item kind no
	(call_script, "script_cf_shield_clash", ":attacker_id", ":victim_id", ":missile_id")])
# Dunde's Generic on shield hit END
    
def save_python_header():
  file = open("./ID_items.py","w")
  for i_item in xrange(len(items)):
    file.write("itm_%s = %d\n"%(convert_to_identifier(items[i_item][0]),i_item))
  file.close()

def write_items(variable_list,variable_uses,tag_uses,quick_strings):
  itemkinds_file_name = export_dir + "item_kinds1.txt"
  ofile = open(itemkinds_file_name,"w")
  ofile.write("itemsfile version 3\n")
  ofile.write("%d\n"%len(items))
  i_item = 0
  for item in items:
    if (item[3] & itp_merchandise) > 0:
      id_no = find_object(items,convert_to_identifier(item[0]))
      add_tag_use(tag_uses,tag_item,id_no)
    #ofile.write(" itm_%s %s %s %d "%(convert_to_identifier(item[0]),replace_spaces(item[1]),replace_spaces(item[1]),len(item[2])))
    #ofile.write(" %s %s %s %d "%(signature[(find_object(items,convert_to_identifier(item[0])))%sign_length],replace_spaces(item[1]),replace_spaces(item[1]),len(item[2])))
    ofile.write(" itm_%s %s %s %d "%(str(i_item),replace_spaces(item[1]),replace_spaces(item[1]),len(item[2])))
    item_variations = item[2]
    for item_variation in item_variations:
      ofile.write(" %s %d "%(item_variation[0],item_variation[1]))
    # weight begin  
    if isinstance(item[6],list):
      ofile.write(" %d %d %d %d %f %d %d %d %d %d %d %d %d %d %d %d %d\n"%(item[3], item[4], item[5], item[7],
                                                   item[6][0],
                                                   get_abundance(item[6][1]),                  
                                                   get_head_armor(item[6][1]),
                                                   get_body_armor(item[6][1]),
                                                   get_leg_armor(item[6][1]),
                                                   get_difficulty(item[6][1]),
                                                   get_hit_points(item[6][1]),
                                                   get_speed_rating(item[6][1]),
                                                   get_missile_speed(item[6][1]),
                                                   get_weapon_length(item[6][1]),
                                                   get_max_ammo(item[6][1]),
                                                   get_thrust_damage(item[6][1]),
                                                   get_swing_damage(item[6][1]),
                                                               ))
    else:      
      ofile.write(" %d %d %d %d %f %d %d %d %d %d %d %d %d %d %d %d %d\n"%(item[3], item[4], item[5], item[7],
                                                   get_weight(item[6]),
                                                   get_abundance(item[6]),                  
                                                   get_head_armor(item[6]),
                                                   get_body_armor(item[6]),
                                                   get_leg_armor(item[6]),
                                                   get_difficulty(item[6]),
                                                   get_hit_points(item[6]),
                                                   get_speed_rating(item[6]),
                                                   get_missile_speed(item[6]),
                                                   get_weapon_length(item[6]),
                                                   get_max_ammo(item[6]),
                                                   get_thrust_damage(item[6]),
                                                   get_swing_damage(item[6]),
                                                               ))
    # weight end
    if (len(item) > 9):
      ofile.write(" %d\n"%(len(item[9])))
      for item_faction in item[9]:
        ofile.write(" %d"%item_faction)
      ofile.write("\n")
    else:
      ofile.write(" 0\n")
    trigger_list = []
    if (len(item) > 8):
      trigger_list = item[8]
    # Dunde's Generic on shield hit BEGIN
    if (use_wse==1):
      type = item[3] & 0x000000ff 
      if type==itp_type_shield & len(generic_on_shield_hit)>0 & use_wse==1:
        trigger_list += [generic_on_shield_hit,]  
    # Dunde's Generic on shield hit END  
    save_simple_triggers(ofile,trigger_list, variable_list,variable_uses,tag_uses,quick_strings, "itm_" + item[0])
    i_item+=1

  ofile.close()
  
print "Exporting item data..."
save_python_header()

from module_info import *

from process_common import *
from process_operations import *

variable_uses = []
variables = load_variables(export_dir,variable_uses)
tag_uses = load_tag_uses(export_dir)
quick_strings = load_quick_strings(export_dir)
write_items(variables,variable_uses,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_tag_uses(export_dir,tag_uses)
save_quick_strings(export_dir,quick_strings)
#print "Finished with Items."

#Dunde's imod begin
if export_imod_data ==1:
  from module_item_modifiers import * 
  def write_imods():
    imods_file_name = export_dir + "data/item_modifiers.txt"
    ofile = open(imods_file_name,"w")
    for imod in item_modifiers:
      ofile.write("%s %s %f %f\n"%("imod_" + imod[0], imod[1] + "_%s", imod[2], imod[3]))
    ofile.close()
  print "Exporting item modifiers data..."
  write_imods()
#Dunde's imod end