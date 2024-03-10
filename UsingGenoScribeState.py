import pygame
import render_ui
import Message
import constants
import controls
from State import State


class UsingGenoScribeState(State):
    def __init__(self, game, player, actor):
        super().__init__(game, player)
        self.actor = actor

    def enter(self):
        if self.actor.genome:
            self.actor.genome[0].is_selected = True
            render_ui.genome_to_render = (self.actor, self.actor.genome)
            render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                         'Select a gene to transfer.',
                                                         [255, 255, 255, 255])

    def exit(self):
        self.player.action_item = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                direction_keys_list = list(controls.direction_keys.keys())
                all_genes = self.actor.genome + self.player.action_item.inventory
                active_list = None
                selected_gene_index = None
                for gene in all_genes:
                    if gene.is_selected is True:
                        if gene in self.actor.genome:
                            active_list = self.actor.genome
                            selected_gene_index = self.actor.genome.index(gene)
                        elif gene in self.player.action_item.inventory:
                            active_list = self.player.action_item.inventory
                            selected_gene_index = self.player.action_item.inventory.index(gene)
                if event.key == direction_keys_list[1]:  # up
                    if len(active_list) > 1:
                        if selected_gene_index == 0:
                            selected_gene_index = active_list.index(active_list[-1])
                        else:
                            selected_gene_index -= 1
                    else:
                        pass
                elif event.key == direction_keys_list[7]:  # down
                    if len(active_list) > 1:
                        if selected_gene_index == active_list.index(active_list[-1]):
                            selected_gene_index = active_list.index(active_list[0])
                        else:
                            selected_gene_index += 1
                    else:
                        pass
                elif event.key == direction_keys_list[3]:  # left
                    if active_list == self.player.action_item.inventory:
                        pass
                    else:
                        if not self.player.action_item.inventory:
                            pass
                        else:
                            active_list = self.player.action_item.inventory
                            selected_gene_index = active_list.index(active_list[0])
                elif event.key == direction_keys_list[5]:  # right
                    if active_list == self.actor.genome:
                        pass
                    else:
                        if not self.actor.genome:
                            pass
                        else:
                            active_list = self.actor.genome
                            selected_gene_index = active_list.index(active_list[0])
                elif event.key == controls.keybinds['confirm']:
                    for gene in active_list:
                        if gene.is_selected:
                            if gene in self.actor.genome:
                                active_list = self.player.action_item.inventory
                                self.player.action_item.inventory.append(gene)
                                self.actor.genome.remove(gene)
                                selected_gene_index = active_list.index(gene)
                            elif gene in self.player.action_item.inventory:
                                active_list = self.actor.genome
                                self.actor.genome.append(gene)
                                self.player.action_item.inventory.remove(gene)
                                selected_gene_index = active_list.index(gene)
                for gene in all_genes:
                    if gene in active_list:
                        if active_list.index(gene) == selected_gene_index:
                            gene.is_selected = True
                        else:
                            gene.is_selected = False
                    else:
                        gene.is_selected = False
