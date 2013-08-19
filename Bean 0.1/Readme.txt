
  __________________________________
 /  __               ___  ___    __ \ V 1.152
 \ \__ \  \  \ \__\ \__  \   \ \/__  \
  \ __\ \ _\ _\ ___\  __\ \__/  \  \  \
   \__________________________________/
   
  [the enhancement you were waiting for]
   
  | Created by Swyter -- based on the Mount&Blade: Warband Module System

  | For getting documentation and the latest version of the module system check out:
  | <www.taleworlds.com/mb_module_system.html>
  
  
  
  
  _ABOUT__________
  
  I've tried to make the msys maintainable, easier to get used to and less cluttered.
  
  The structure and file name convention has been changed into something more intuitive.
  All the headers, ID, and process files goes in their own separate folders.
  
  The module_* files now they are prefixed and grouped by a meaningful tag.

        _config
        
    —AGENT
        agent_animations
        agent_items
        agent_list
        agent_skins
    
    —SCENE
        scene_list
        scene_missiontemplates
        scene_props
        
    —MAP
        map_icons
        map_parties
        map_partytemplates
    
    —GAME
        game_constants
        game_factions
        game_music
        game_postfx
        game_particlesystems
        game_scripts
        game_simpletriggers
        game_sounds
        game_strings
        game_tableaumaterials
        game_triggers
        game_variables
        
        
    —UI
        ui_dialogs
        ui_infopages
        ui_menus
        ui_meshes
        ui_presentations
        ui_quests
        ui_skills
    
 _CONVERSION_TABLE______
    
 Just put here for quick reference, the nomenclature is very similar:

    module_animations        —> agent_animations
    module_constants         —> game_constants
    module_dialogs           —> ui_dialogs
    module_factions          —> game_factions
    module_game_menus        —> ui_menus
    module_info              —> _config
    module_info_pages        —> ui_info_pages
    module_items             —> agent_items
    module_map_icons         —> map_icons
    module_meshes            —> ui_meshes
    module_mission_templates —> scene_missiontemplates
    module_music             —> game_music
    module_particle_systems  —> game_particlesystems
    module_parties           —> map_parties
    module_party_templates   —> map_partytemplates
    module_postfx            —> game_postfx
    module_presentations     —> ui_presentations
    module_quests            —> ui_quests
    module_scenes            —> scene_list
    module_scene_props       —> scene_props
    module_scripts           —> game_scripts
    module_simple_triggers   —> game_simpletriggers
    module_skills            —> ui_skills
    module_skins             —> agent_skins
    module_sounds            —> game_sounds
    module_strings           —> game_strings
    module_tableau_materials —> game_tableaumaterials
    module_triggers          —> game_triggers
    module_troops            —> agent_list
    module_variables         —> game_variables

  
  Notepad++, Notepad2, Gedit, Geany, Sublime Text 2 or a similar code editor is recommended.

  A Python interpreter, and a standalone, much faster full-featured compiler
  named ModuleSystem++ are included.