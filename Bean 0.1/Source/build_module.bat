@echo off
echo Getting Header Files
copy ".\Header\*.*" ".\" >> garbage.txt
echo Getting ID Files
copy ".\ID\*.*" ".\" >> garbage.txt
echo Getting Process Files
copy ".\Process\*.*" ".\" >> garbage.txt
echo ______________________________

python process_init.py
python process_global_variables.py
python process_strings.py
python process_skills.py
python process_music.py
python process_animations.py
python process_meshes.py
python process_sounds.py
python process_skins.py
python process_map_icons.py
python process_factions.py
python process_items.py
python process_scenes.py
python process_troops.py
python process_particle_sys.py
python process_scene_props.py
python process_tableau_materials.py
python process_presentations.py
python process_party_tmps.py
python process_parties.py
python process_quests.py
python process_info_pages.py
python process_scripts.py
python process_mission_tmps.py
python process_game_menus.py
python process_simple_triggers.py
python process_dialogs.py
python process_global_variables_unused.py
python process_postfx.py

echo ______________________________

echo Deleting Compiled Python
@del *.pyc
echo Deleting Header Files
@del header_*.py
copy ".\Header\header_operations.py" ".\" >> garbage.txt
echo Deleting ID Files
@del ID_*.py
echo Deleting Process Files
@del process_*.py

echo ______________________________

echo Script processing has ended
echo Press any key to exit
pause>nul