import constants
import Message

apply_item_fail_prompt = Message.Message(constants.PROMPT_RECT,
                                         'You have nothing to apply.',
                                         [255, 255, 255, 255])

apply_item_choose_prompt = Message.Message(constants.PROMPT_RECT,
                                           'Choose an item to apply.',
                                           [255, 255, 255, 255])

# apply_item_choose_direction_prompt = Message.Message(constants.PROMPT_RECT,
#                                                      'Apply the ' +
#                                                      player.action_item.glyph +
#                                                      player.action_item.name +
#                                                      ' in which direction?',
#                                                      [255, 255, 255, 255])

choose_direction_fail_prompt = Message.Message(constants.PROMPT_RECT,
                                               'You must choose a direction first.',
                                               [255, 255, 255, 255])

drop_item_choose_prompt = Message.Message(constants.PROMPT_RECT,
                                          'Choose an item to drop.',
                                          [255, 255, 255, 255])

drop_item_fail_prompt = Message.Message(constants.PROMPT_RECT,
                                        'You have nothing to drop.',
                                        [255, 255, 255, 255])

genoscribe_gene_choose_prompt = Message.Message(constants.PROMPT_RECT,
                                                'Choose a gene to transfer.',
                                                [255, 255, 255, 255])

wall_prompt = Message.Message(constants.PROMPT_RECT,
                              'The wall is unyielding.',
                              [255, 255, 255, 255])
