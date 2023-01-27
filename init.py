import math
import os
import shutil
from PIL import Image
import numpy
import zipfile
from os import path
import sys
'''存放颜色与方块的对应关系，初始为 1.16.5 版本所拥有的方块'''
color={'227 223 215':'quartz_pillar','227 221 213':'quartz_bricks','218 214 202':'chiseled_quartz_block','254 245 240':'smooth_quartz','216 216 216':'iron_block','218 222 222':'white_wool','255 255 255':'snow','249 225 77':'horn_coral_block','33 97 220':'tube_coral_block','211 43 46':'fire_coral_block','233 119 195':'brain_coral_block','199 32 192':'bubble_coral_block','83 80 85': 'netherite_block', '118 33 26': 'netherrack', '163 4 0': 'nether_wart_block', '65 72 16': 'jungle_leaves', '172 127 71': 'spruce_planks', '47 72 41': 'spruce_leaves', '239 233 204': 'cut_sandstone', '226 155 17': "jack_o_lantern", '235 191 131': 'stripped_jungle_wood', '159 119 63': 'stripped_spruce_log', '238 202 130': 'stripped_oak_wood', '94 63 31': 'stripped_dark_oak_wood', '237 217 160': 'stripped_birch_wood', '139 58 88': 'stripped_crimson_stem', '184 77 116': 'stripped_crimson_hyphae', '234 134 81': 'stripped_acacia_wood', '169 168 173': 'dispenser', '224 110 215': 'magenta_glazed_terracotta', '210 68 195': 'magenta_concrete', '241 131 233': 'magenta_concrete_powder', '45 11 83': 'crying_obsidian', '162 161 164': 'cobblestone', '99 99 101': 'bedrock', '181 171 169': 'dead_bubble_coral_block', '176 165 163': 'dead_fire_coral_block', '178 169 166': 'dead_tube_coral_block', '166 157 155': 'dead_brain_coral_block', '164 153 151': 'dead_horn_coral_block', '177 177 179': 'andesite', '215 215 218': 'smooth_stone', '242 232 201': 'smooth_sandstone', '202 155 86': 'barrel', '240 237 201': 'end_stone', '217 211 164': 'end_stone_bricks', '119 63 23': 'brown_concrete', '182 127 87': 'brown_concrete_powder', '140 78 34': 'brown_wool', '206 155 120': 'brown_mushroom_block', '100 55 31': 'brown_terracotta', '255 149 9': 'orange_concrete', '254 176 20': 'orange_wool', '210 114 40': 'orange_terracotta', '152 114 65': 'oak_wood', '221 182 114': 'oak_planks', '75 99 19': 'oak_leaves', '240 229 193': 'sand', '183 176 177': 'gravel', '112 61 27': 'dirt', '186 222 253': 'packed_ice', '149 201 216': 'prismarine', '144 229 225': 'prismarine_bricks', '185 184 175': 'light_gray_concrete', '199 198 192': 'light_gray_wool', '192 155 143': 'light_gray_terracotta', '96 218 251': 'light_blue_concrete_powder', '64 211 248': 'light_blue_wool', '72 35 6': 'dark_oak_wood', '80 40 8': 'dark_oak_planks', '69 89 21': 'dark_oak_leaves', '211 210 89': 'wet_sponge', '114 66 7': 'podzol', '103 110 120': 'gray_glazed_terracotta', '59 63 71': 'gray_concrete', '74 80 88': 'gray_wool', '71 47 36': 'gray_terracotta', '84 55 40': 'soul_soil', '92 59 42': 'soul_sand', '25 25 25': 'coal_block', '134 134 134': 'coal_ore', '174 174 178': 'furnace', '225 207 156': 'birch_planks', '64 67 28': 'birch_leaves', '242 218 203': 'white_terracotta', '198 198 200': 'stone', '154 153 155': 'stone_bricks', '195 132 106': 'bricks', '183 183 183': 'lodestone', '191 195 195': 'polished_andesite', '208 151 122': 'polished_granite', '73 66 75': 'polished_blackstone', '55 49 61': 'polished_blackstone_bricks', '249 198 220': 'pink_glazed_terracotta', '255 162 202': 'pink_concrete', '249 190 218': 'pink_wool', '216 117 110': 'pink_terracotta', '205 210 227': 'clay', '212 168 213': 'purpur_block', '219 172 219': 'purpur_pillar', '128 64 161': 'purple_glazed_terracotta', '124 35 188': 'purple_concrete', '165 74 211': 'purple_concrete_powder', '149 50 201': 'purple_wool', '151 86 103': 'purple_terracotta', '250 154 43': 'red_sand', '171 15 0': 'redstone_block', '105 15 11': 'red_nether_bricks', '220 70 47': 'red_glazed_terracotta', '182 38 21': 'red_concrete', '197 44 22': 'red_wool', '225 48 27': 'red_mushroom_block', '187 81 53': 'red_terracotta', '165 32 22': 'crimson_nylium', '137 56 84': 'crimson_stem', '118 18 18': 'crimson_hyphae', '118 141 39': 'green_glazed_terracotta', '88 109 35': 'green_concrete', '101 127 24': 'green_wool', '193 135 109': 'granite', '142 147 132': 'mossy_stone_bricks', '111 138 65': 'grass_block', '241 206 113': 'shroomlight', '162 219 252': 'blue_ice', '37 51 180': 'blue_concrete', '77 89 203': 'blue_concrete_powder', '44 57 187': 'blue_wool', '84 66 111': 'blue_terracotta', '224 190 99': 'bee_nest', '230 191 122': 'beehive', '242 177 63': 'honey_block', '248 202 30': 'honeycomb_block', '119 160 33': 'melon', '4 142 162': 'warped_wart_block', '48 141 147': 'warped_stem', '55 43 82': 'respawn_anchor', '137 127 115': 'acacia_wood', '209 116 55': 'acacia_planks', '67 78 20': 'acacia_leaves', '255 233 78': 'gold_block', '159 158 162': 'chiseled_stone_bricks', '135 244 251': 'diamond_block', '49 53 65': 'smithing_table', '4 142 179': 'cyan_concrete', '40 190 219': 'cyan_concrete_powder', '111 118 122': 'cyan_terracotta', '8 65 176': 'lapis_block', '80 80 84': 'blast_furnace', '144 215 43': 'lime_concrete', '165 220 39': 'lime_wool', '246 226 134': 'yellow_glazed_terracotta', '254 212 17': 'yellow_concrete', '255 192 35': 'yellow_concrete_powder', '254 222 29': 'yellow_wool', '31 23 50': 'obsidian', '46 39 49': 'blackstone', '103 28 24': 'black_glazed_terracotta', '18 22 30': 'black_concrete', '28 32 38': 'black_concrete_powder', '25 27 33': 'black_wool', '53 31 20': 'black_terracotta'}
from numba import jit
@jit(nopython=True, cache=True)     # numba 库加速，将函数直接译为机器语言
def colourdis(rgb_1, rgb_2):
    '''找近似颜色的LAB算法'''
    R_1, G_1, B_1 = rgb_1
    R_2, G_2, B_2 = rgb_2
    rmean = (R_1 + R_2) / 2
    R = R_1 - R_2
    G = G_1 - G_2
    B = B_1 - B_2
    return math.sqrt((2 + rmean / 256) * (R ** 2) + 4 * (G ** 2) + (2 + (255 - rmean) / 256) * (B ** 2))
def find(c):
    '''找最接近的颜色'''
    difference=1e9
    rgb=None
    for i in color:
        nowtry=i.split(" ")
        nowtry=[int(nowtry[0]),int(nowtry[1]),int(nowtry[2])]
        nowtry=tuple(nowtry)
        if colourdis(c,nowtry)<difference:
            difference=colourdis(c,nowtry)
            rgb=i
    return color.get(rgb)
def resurce_path(relative_path):
    '''打包资源需要'''
    base_path=getattr(sys,'_MEIPASS',path.dirname(path.abspath(__file__)))
    return path.join(base_path,relative_path)