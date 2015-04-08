from compiler import *
register_plugin()

##Constants Begin
bandit_party_template_begin = "pt_steppe_bandits"
bandit_party_template_end = "pt_deserters"
##Constants End

scripts = [
  ("sort_party_by_troop_level",
    [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":first_stack", 2),

      (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
      (try_begin),
        (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":cur_troop", ":party_no", ":cur_stack"),
          (eq, ":cur_troop", "trp_caravan_master"),
          (party_stack_get_size, ":stack_size", ":party_no", ":cur_stack"),
          (party_remove_members, ":party_no", "trp_caravan_master", ":stack_size"),
          (party_add_leader, ":party_no", "trp_caravan_master", ":stack_size"),
          (assign, ":cur_stack", 0),
          (assign, ":first_stack", 1),
        (try_end),
      (try_end),
      (try_begin),
        (gt, ":num_stacks", ":first_stack"),
        (assign, ":last_stack", ":num_stacks"),

        # start to sort
        (store_sub, ":num_times", ":num_stacks", ":first_stack"),
        (try_for_range, ":unused", 0, ":num_times"),
          # find highest-level troop
          (assign, ":best_stack", -1),
          (assign, ":best_level", -1),
          (try_for_range, ":cur_stack", ":first_stack", ":last_stack"),
            (party_stack_get_troop_id, ":cur_troop", ":party_no", ":cur_stack"),
            (store_character_level, ":troop_level", ":cur_troop"),
            # level*3 with extra bonuse to differentiate troop types with the same level
            (val_mul, ":troop_level", 3),
            (try_begin),
              (troop_is_guarantee_horse, ":cur_troop"),
              (val_add, ":troop_level", 2), # horseman
            (else_try),
              (troop_is_guarantee_ranged, ":cur_troop"), # archers
            (else_try),
              (val_add, ":troop_level", 1), # footman
            (try_end),
            # add 1000-7000 extra bonuse to sort by factions at the same time
            (store_troop_faction, ":troop_faction", ":cur_troop"),
            (try_begin),
              (neg|is_between, ":troop_faction", npc_kingdoms_begin, npc_kingdoms_end),
              (assign, ":faction_bonuse", 1000), # for non-kingdom troops
              (val_add, ":faction_bonuse", ":troop_faction"), ##BEAN - Break Ties
            (else_try),
              (eq, ":troop_faction", "fac_kingdom_1"),
              (assign, ":faction_bonuse", 2000),
            (else_try),
              (eq, ":troop_faction", "fac_kingdom_2"),
              (assign, ":faction_bonuse", 3000),
            (else_try),
              (eq, ":troop_faction", "fac_kingdom_3"),
              (assign, ":faction_bonuse", 4000),
            (else_try),
              (eq, ":troop_faction", "fac_kingdom_4"),
              (assign, ":faction_bonuse", 5000),
            (else_try),
              (eq, ":troop_faction", "fac_kingdom_5"),
              (assign, ":faction_bonuse", 6000),
            (else_try),
              (eq, ":troop_faction", "fac_kingdom_6"),
              (assign, ":faction_bonuse", 7000),
            (try_end),
            (try_begin),
              (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
              (party_stack_get_troop_id, ":cur_leader", ":party_no", 0),
              (store_troop_faction, ":leader_faction", ":cur_leader"),
              (troop_get_slot, ":leader_original_faction", ":cur_leader", slot_troop_original_faction),
              (try_begin),
                (eq, ":troop_faction", ":leader_original_faction"),
                (assign, ":faction_bonuse", 0), # no bonuse for its cur faction
              (else_try),
                (eq, ":troop_faction", ":leader_faction"),
                (is_between, ":leader_faction", npc_kingdoms_begin, npc_kingdoms_end),
                (assign, ":faction_bonuse", 500), # small bonuse
              (try_end),
            (else_try),
              (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_castle),
              (party_slot_eq, ":party_no", slot_party_type, spt_town),
              (neg|party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
              (store_faction_of_party, ":center_faction", ":party_no"),
              (eq, ":troop_faction", ":center_faction"),
              (assign, ":faction_bonuse", 0), # no bonuse for its cur faction
            (try_end),
            (val_add, ":troop_level", ":faction_bonuse"),
            (gt, ":troop_level", ":best_level"),
            (assign, ":best_level", ":troop_level"),
            (assign, ":best_stack", ":cur_stack"),
          (try_end),
          # move to the end
          (try_begin),
            (gt, ":best_level", -1),
            (party_stack_get_troop_id, ":stack_troop", ":party_no", ":best_stack"),
            (party_stack_get_size, ":stack_size", ":party_no", ":best_stack"),
            (party_stack_get_num_wounded, ":num_wounded", ":party_no", ":best_stack"),
            (party_remove_members, ":party_no", ":stack_troop", ":stack_size"),
            (party_add_members, ":party_no", ":stack_troop", ":stack_size"),
            (party_wound_members, ":party_no", ":stack_troop", ":num_wounded"),
            (val_sub, ":last_stack", 1),
          (try_end),
        (try_end),
      (try_end),
    ]
  ),
  
  ("sort_parties_by_troop_level",
    [
      (eq, "$bean_options_sort_party", 1), ##BEAN - Options | Party Sorting
      (try_for_parties, ":party_no"),       
        (neq, ":party_no", "p_temp_party"),
        (assign, ":continue", 0),
        ##BEAN BEGIN - Options | Player Sorting
        (try_begin),
          (eq, ":party_no", "p_main_party"),
          (try_begin),
            (eq, "$bean_options_sort_player_party", 1),
            (assign, ":continue", 1),
            (assign, ":first_stack", 1),
            #(display_message, "@Sorting Player Party"),
          #(else_try),
          #  (display_message, "@Player Party Sorting Disabled"),
          (try_end),
        ##BEAN END - Options | Player Sorting
        (else_try),
          (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
          (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
          (party_is_active, ":party_no"),
          (assign, ":continue", 1),
          (try_begin),
            (party_stack_get_troop_id, ":cur_troop", ":party_no", 0),
            (this_or_next|troop_is_hero, ":cur_troop"),
            (eq, ":cur_troop", "trp_caravan_master"),
            (assign, ":first_stack", 1),
          (else_try),
            (assign, ":first_stack", 0),
          (try_end),
        (else_try),
          (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_castle),
          (party_slot_eq, ":party_no", slot_party_type, spt_town),
          #BEAN BEGIN - Options | Player Fief Sorting
          (try_begin),
            (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
            (try_begin),
              (eq, "$bean_options_sort_player_fiefs", 1),
              (assign, ":first_stack", 0),
              (assign, ":continue", 1),
              #(display_message, "@Sorting Player Fied"),
            #(else_try),
            #  (display_message, "@Player Fief Sorting Disabled"),
            (try_end),
          (else_try),
            (assign, ":first_stack", 0),
            (assign, ":continue", 1),
          (try_end),
          ##BEAN END - Options | Player Fief Sorting
        (else_try),
          (party_get_template_id, ":party_template", ":party_no"),
          (this_or_next|eq, ":party_template", "pt_looters"),
          (is_between, ":party_template", bandit_party_template_begin, bandit_party_template_end),
          (assign, ":continue", 1),
          (try_begin),
            (party_stack_get_troop_id, ":cur_troop", ":party_no", 0),
            (troop_is_hero, ":cur_troop"),
            (assign, ":first_stack", 1),
          (else_try),
            (assign, ":first_stack", 0),
          (try_end),
        (try_end),
        (eq, ":continue", 1),
        (call_script, "script_sort_party_by_troop_level", ":party_no", ":first_stack"),
      (try_end),
    ]
  )
]

simple_triggers = [
  (8,
    [
      (call_script, "script_sort_parties_by_troop_level"),
    ]
  ),
]