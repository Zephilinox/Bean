from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
#import string

from xgm_mod_options_header import *

############################################################################
## 0) overlay id (not used atm, but can allow searches in future. just put something unique)
## 1) overlay type (defined in xgm_mod_options_header)
## 2) overlay type specific parameters (e.g. for number box, it can be lower/upper range, for cbobox, it would be the cbo items etc)
##    a) xgm_ov_numberbox : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    b) xgm_ov_combolabel/xgm_ov_combobutton  : list of combo items. e.g. ["option1", "option2", "option3"]
##    c) xgm_ov_slider : lower_bound(inclusive), upper_bound(exclusive). e.g. [0,101] for range of values from 0-100
##    d) xgm_ov_checkbox : not used fttb. just leave empty. e.g. []
## 3) text label
## 4) reserved for text label flags
## 5) description (unused for now. may be used for stuff like tooltip in future)
## 6) reserved for description flags
## 7) initialization op block.  Used for updating the overlay values from game values. Must assign the desired value to reg1.
## 8) update op block.  Used for updating game values from overlay values. The overlay value is in reg1.
## 9) optional. reserved for option page id. unused for now. leave out for options using general page.
############################################################################

mod_options = [
    # sample checkbox to switch the in-game cheat mode.  Comment out this if you don't want it.

  ("general_title_bar", xgm_ov_title, [], "General Options", tf_center_justify|tf_with_outline),

  ##BEAN BEGIN - Sort Party Troops
  ("perisno_sort_party", xgm_ov_checkbox,
    [
    ],
    "Sort Parties:", 0,
    "If Enabled, party sorting will be turned on.^^This will sort all NPC parties (including garrisons), as well as allow the possibility of sorting player party and player fiefs^^Default = Enabled", 0,
    [
      (assign, reg1, "$bean_options_sort_party"),
    ],
    [
      (assign, "$bean_options_sort_party", reg1),
    ],
  ),

  ("perisno_sort_player_party", xgm_ov_checkbox,
    [
    ],
    "Sort Player Party:", 0,
    "If Enabled, the player party will be sorted automatically (Must enable party sorting)^^Default = Disabled", 0,
    [
      (assign, reg1, "$bean_options_sort_player_party"),
    ],
    [
      (try_begin),
        (neq, "$bean_options_sort_party", 1),
        (display_message, "@You must enable NPC party sorting for player party sorting to take effect."),
      (try_end),

      (assign, "$bean_options_sort_player_party", reg1),
    ],
  ),

  ("perisno_sort_player_fiefs", xgm_ov_checkbox,
    [
    ],
    "Sort Player Fiefs:", 0,
    "If Enabled, all garrisons in player fiefs will be sorted automatically (Must enable party sorting)^^Default = Enabled", 0,
    [
      (assign, reg1, "$bean_options_sort_player_fiefs"),
    ],
    [
      (try_begin),
        (neq, "$bean_options_sort_party", 1),
        (display_message, "@You must enable NPC party sorting for player fief sorting to take effect."),
      (try_end),

      (assign, "$bean_options_sort_player_fiefs", reg1),
    ],
  ),
  ##BEAN END - Sort Party Troops

	# ("companion_title_bar", xgm_ov_title, [], "Companion Options", tf_center_justify|tf_with_outline),

	# ("pbod_npc_complaints", xgm_ov_checkbox, [], "Disable Companions' complaints:", 0,
	# 	"Disabling NPC Complaints will mute your companion's complaints about each other or your decisions.  While disabled, companions will not leave the party regardless of how they feel about your leadership.", 0,
	# 	[(assign, reg1, "$disable_npc_complaints"),],
	# 	[(assign, "$disable_npc_complaints", reg1),],),

	# ("battle_title_bar", xgm_ov_title, [], "Battle Options", tf_center_justify|tf_with_outline),

 #  ("perisno_charge_when_dead", xgm_ov_checkbox,
 #    [
 #    ],
 #    "Charge On Death:", 0,
 #    "If Enabled, your units will break formation and charge when you die.^^Default = Enabled", 0,
 #    [
 #      (assign, reg1, "$g_perisno_charge_when_dead"),
 #    ],
 #    [
 #      (assign, "$g_perisno_charge_when_dead", reg1),
 #    ],
 #  ),

	# ("toggle_battle_mini_map", xgm_ov_checkbox, [], "Battle Overview Map:", 0,
	#   "When enabled a small transparent map of the current battle will appear in the upper right corner of the combat screen.^^If unchecked, this will not appear.", 0,
	#   [(assign, reg1, "$g_show_minimap"),],
	#   [(assign, "$g_show_minimap", reg1),],),

 #  ("perisno_reinforcement_limit", xgm_ov_numberbox,
 #    [
 #      0, 10001
 #    ],
 #    "Reinforcement Waves:", 0,
 #    "This sets the maximum number of reinforcement waves.^^Default = 2", 0,
 #    [
 #      (assign, reg1, "$g_perisno_defender_reinforcement_limit"),
 #    ],
 #    [
 #      (assign, "$g_perisno_defender_reinforcement_limit", reg1),
 #      (assign, "$g_perisno_attacker_reinforcement_limit", reg1),
 #    ],
 #  ),

 #  ("perisno_reinforcement_threshold", xgm_ov_numberbox,
 #    [
 #      2, 10001
 #    ],
 #    "Reinforcement Threshold:", 0,
 #    "This sets the threshold for troops before a reinforcement is spawned.^^For instance, if there are 8 enemies and the threshold is 8, on the next enemy death a new enemy reinforcement will be spawned^^Default = 8", 0,
 #    [
 #      (assign, reg1, "$g_perisno_defender_reinforcement_threshold"),
 #    ],
 #    [
 #      (assign, "$g_perisno_defender_reinforcement_threshold", reg1),
 #      (assign, "$g_perisno_attacker_reinforcement_threshold", reg1),
 #    ],
 #  ),

 #  ("perisno_reinforcement_amount", xgm_ov_numberbox,
 #    [
 #      1, 10001
 #    ],
 #    "Reinforcement Amount:", 0,
 #    "This sets the number of troops that appear in each reinforcement wave.^^Is not limited by battle size amount^^Default = 8", 0,
 #    [
 #      (assign, reg1, "$g_perisno_defender_reinforcement_amount"),
 #    ],
 #    [
 #      (assign, "$g_perisno_defender_reinforcement_amount", reg1),
 #      (assign, "$g_perisno_attacker_reinforcement_amount", reg1),
 #    ],
 #  ),

	# ("overworld_title_bar", xgm_ov_title, [], "Over-world Options", tf_center_justify|tf_with_outline),

 #  ("perisno_wait_time_multiplier", xgm_ov_numberbox,
 #    [
 #      1, 21
 #    ],
 #    "Wait Time Multiplier:", 0,
 #    "This sets the time multiplier while resting and waiting.^^Default = 8", 0,
 #    [
 #      (assign, reg1, "$g_perisno_wait_time_multiplier"),
 #    ],
 #    [
 #      (assign, "$g_perisno_wait_time_multiplier", reg1),
 #    ],
 #  ),

 #  ("perisno_center_wait_hours", xgm_ov_numberbox,
 #    [
 #      8, 49
 #    ],
 #    "Center Waiting Time:", 0,
 #    "This sets how many hours you will spend while resting at a town or village.^^Default = 24", 0,
 #    [
 #      (assign, reg1, "$g_perisno_center_wait_hours"),
 #    ],
 #    [
 #      (assign, "$g_perisno_center_wait_hours", reg1),
 #    ],
 #  ),

 #  ("perisno_zann_invasion_date", xgm_ov_numberbox,
 #    [
 #      0, 10001
 #    ],
 #    "Zann Invasion Date:", 0,
 #    "After this date, the Zann will invade^^Default = 156", 0,
 #    [
 #      (assign, reg1, "$g_perisno_zann_invasion_date"),
 #    ],
 #    [
 #      (assign, "$g_perisno_zann_invasion_date", reg1),
 #    ],
 #  ),

	("diplomacy_title_bar", xgm_ov_title, [], "Diplomacy Options", tf_center_justify|tf_with_outline),

	("dipl_horse_speed", xgm_ov_checkbox, [], "Horse speed limitation:", 0,
		"When enabled, this causes horses to travel slower as they take damage.^^Default = Disabled", 0,
		[(assign, reg1, "$g_dplmc_horse_speed"),],
		[(assign, "$g_dplmc_horse_speed", reg1),],),

	("diplo_terrain_adv", xgm_ov_checkbox, [], "Terrain advantage in Autocalc battles:", 0,
	  "Ticked, autocalculated battles give advantage to factions on their home terrain. Unticked, as in Native and auto-battles are only based on party size and troop levels.^^Default = Enabled", 0,
	  [(store_add, reg1, "$g_dplmc_terrain_advantage", 1),],
	  [(store_sub, "$g_dplmc_terrain_advantage", reg1, 1),], #1->0; 0-> -1
	),

	("diplo_exile", xgm_ov_combobutton, ["Disabled", "Enabled", "Frequent"], "Lords returning from exile:", 0,
	  "Allows exiled lords to be pardoned after a time and rejoin a faction to prevent 'lord-drain' in the late game.&&Default = Enabled", 0,
	  [(store_add, reg1, "$g_dplmc_lord_recycling", 1),],
	  [(store_sub, "$g_dplmc_lord_recycling", reg1, 1),], #1->0; 0-> -1 etc
	),

	("diplo_change_ai", xgm_ov_combobutton, ["Disabled", "Low", "Medium", "High/Experimental"], "Diplomacy AI changes:", 0,
	  "Default = Medium^^Low:^^ - Center points for fief allocation are calculated (villages 1 / castles 2 / towns 3) instead of (villages 1 / castles 1 / towns 2).^^ - For qst_rescue_prisoner and qst_offer_gift, the relatives that can be a target of the quest have been extended to include uncles and aunts and in-laws.^^ - Alterations to script_calculate_troop_score_for_center (these changes currently are only relevant during claimant quests).^^ - When picking a new faction, lords are more likely to return to their original faction (except when that's the faction they're being exiled from), if the ordinary conditions for rejoining are met.  A lord's decision may also be influenced by his relations with other lords in the various factions, instead of just his relations with the faction leaders.^^Medium:^^ - Some changes for lord relation gains/losses when fiefs are allocated.^^ - Kings overrule lords slightly less frequently on faction issues.^^ - In deciding who to support for a fief, minor parameter changes for certain personalities. Some lords will still give priority to fiefless lords or to the lord who conquered the center if they have a slightly negative relation (normally the cutoff is 0 for all personalities).^^ - When a lord can't find any good candidates for a fief under the normal rules, instead of automatically supporting himself he uses a weighted scoring scheme.^^ - In various places where 'average renown * 3/2' appears, an alternate calculation is sometimes used.^^High:^^ - The 'renown factor' when an NPC lord or the player courts and NPC lady is adjusted by the prestige of the lady's guardian.^^ - When a faction has fiefless lords and no free fiefs left, under some circumstances the king will redistribute a village he owns.^^", 0,
	  [(store_add, reg1, "$g_dplmc_ai_changes", 1),],
	  [(store_sub, "$g_dplmc_ai_changes", reg1, 1),], #1->0; 0-> -1 etc
	),

	("diplo_change_econ", xgm_ov_combobutton, ["Disabled", "Low", "Medium", "High/Experimental"], "Diplomacy economic changes:", 0,
	  "Default = Medium^^Low:^^ - Caravan trade benefits both the source and the destination^^ - When the player surrenders, there is a chance his personal equipment will not be looted, based on who accepted the surrender and the difficulty setting. (This is meant to address a gameplay issue. In the first 700 days or so, there is no possible benefit to surrendering rather than fighting to the last man.) Also, a bug that made it possible for books etc. to be looted was corrected.^^ - AI caravans take into consideration distance when choosing their next destination and will be slightly more like to visit their own faction. This strategy is mixed with the Native one, so the trade pattern will differ but not wildly.^^ - Scale town merchant gold by prosperity (up to a maximum 40% change).^^ - Food prices increase in towns that have been under siege for at least 48 hours.^^ - In towns the trade penalty script has been tweaked to make it more efficient to sell goods to merchants specializing in them.^^Medium:^^ - Food consumption increases in towns as prosperity increases.^^   Consumption also increases with garrison sizes.^^ - Lords' looting skill affects how much gold they take from the player when they defeat him.^^ - Lords' leadership skill modifies their troop wage costs the same way it does for the player.^^ - The player can lose gold when his fiefs are looted, like lords.^^ - The same way that lord party sizes increase as the player progresses, mercenary party sizes also increase to maintain their relevance. (The rate is the same as for lords: a 1.25% increase per level.)^^ - If the player has a kingdom of his own, his spouse will receive part of the bonus that ordinarily would be due a liege.  The extent of this bonus depends on the number of fiefs the players holds. This bonus is non-cumulative with the marshall bonus.^^ - Attrition is inflicted on NPC-owned centers if they can't pay wages, but only above a certain threshold.^^ - Strangers cannot acquire enterprises (enforced at 1 instead of at 0, so you have to do something).^^High: - The total amount of weekly bonus gold awarded to kings in Calradia   remains constant: as kings go into exile, their bonuses are divided among the remaining kings.^^ - If lord's run a personal gold surplus after party wages, the extra is divided among the lord and his garrisons budgets (each castle and town has its own pool of funds to pay for soldiers) on the basis of whether the lord is low on gold or any of his fortresses are. (If none are low   on gold, the lord takes everything, like before.)^^ - The honor loss from an offense depends in part on the player's honor   at the time.  The purer the reputation, the greater the effect of a single disagrace.^^ - Raiding change: village gold lost is removed from uncollected taxes before the balance (if any) is removed from the lord.^^ - Cash for prisoners", 0,
	  [(store_add, reg1, "$g_dplmc_gold_changes", 1)],
	  [(store_sub, "$g_dplmc_gold_changes", reg1, 1),], #1->0; 0-> -1 etc
	),

	("diplo_prejudice", xgm_ov_combobutton, ["Disabled", "Default", "High"], "Anti-woman prejudice level:", 0,
	  "Default = Default^^Disabled levels the playing-field for female player characters. Default as in Native. High increases the sexism/anti-woman prejudice of the medieval setting for female player characters.", 0,
	   [(try_begin),
			(this_or_next|eq, "$g_disable_condescending_comments", 2),
			(eq, "$g_disable_condescending_comments", 3),
			(assign, reg1, 0),
		(else_try),
			(this_or_next|eq, "$g_disable_condescending_comments", -1),
			(eq, "$g_disable_condescending_comments", -2),
			(assign, reg1, 2),
		(else_try),
			(assign, reg1, 1),
		(try_end),
	   ],
	   [(try_begin),
			(eq, reg1, 0),
			(assign, "$g_disable_condescending_comments", 2),
		(else_try),
		    (eq, reg1, 2),
			(assign, "$g_disable_condescending_comments", -2),
		(else_try),
		    (assign, "$g_disable_condescending_comments", 0),
		(try_end),
	   ],
	),
] # mod_options

## utility functions

from util_wrappers import *

# helper wrapper to access mod_options
class ModOptionWrapper(BaseWrapper):

    def __init__(self, _data):
        # verify _data
        if( not isinstance(_data,TupleType) or (len(_data)<2)):
            raise ValueError("ItemSetWrapper: Wrapped must be a tuple.")
        BaseWrapper.__init__(self,_data)


    def GetId(self):
        return self.data[0]

    def GetType(self):
        return self.data[1]

    def GetParameters(self):
        if len(self.data) >2:
            return self.data[2]
        return None

    def GetParameter(self, i):
        if len(self.data) >2:
            return self.data[2][i]
        return None

    def GetTextLabel(self):
        if len(self.data) >3:
            return self.data[3]
        return None

    def GetTextLabelFlags(self):
        if len(self.data) >4:
            return self.data[4]
        return None

    def GetDescription(self):
        if len(self.data) >5:
            return self.data[5]
        return None

    def GetDescriptionFlags(self):
        if len(self.data) >6:
            return self.data[6]
        return None

    def GetInitializeBlock(self):
        if len(self.data) >7:
            return OpBlockWrapper(self.data[7])
        return None

    def GetUpdateBlock(self):
        if len(self.data) >8:
            return OpBlockWrapper(self.data[8])
        return None

    def GetHeight(self):
        if self.GetType() == xgm_ov_line:
            return xgm_mod_options_line_height
        elif self.GetType() in [xgm_ov_checkbox, xgm_ov_numberbox, xgm_ov_combolabel, xgm_ov_combobutton, xgm_ov_title]:
            return xgm_mod_options_property_height
        # elif self.GetType() in [xgm_ov_title]:
            # return (xgm_mod_options_property_height * 1)
        return 0 # no other types supported

## class ModOptionWrapper



# this function will compute the total height required for a list of mod_options.
def mod_options_get_total_height(_mod_options = mod_options):
    height = 0
    for x in _mod_options:
        aModOption = ModOptionWrapper(x)
        height += aModOption.GetHeight()
    # for x in _mod_options:
    return height;
## mod_options_get_total_height
