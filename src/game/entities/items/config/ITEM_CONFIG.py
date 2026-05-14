"""
Config file used for extra stat information for hardware and software
"""
from src.game.ui.config.SYMBOL_CONFIG import *

ITEM_STAT_CONFIG = {
    'ram': {'size': {'min': 1, 'max': 32, 'inverted': True, 'unit': GB_SYMBOL}, 'speed': {'min': 10, 'max': 100, 'inverted': False, 'unit': SPEED_UNIT_SYMBOL}},
    'cpu': {'cpu_increase': {'min': 1, 'max': 2.5, 'inverted': False, 'unit': CPU_MULTIPLIER_SYMBOL}, 'heat_generation': {'min': 5, 'max': 50, 'inverted': True, 'unit': HEAT_UNIT_SYMBOL}},
    'firewall_shield': {'block': {'min': 5, 'max': 95, 'inverted': False, 'unit': FIREWALL_SHIELD_UNIT_SYMBOL}, 'cpu_load': {'min': 1.1, 'max': 10, 'inverted': True, 'unit': CPU_LOAD_UNIT_SYMBOL}, 'size': {'min': 0.2, 'max': 10, 'inverted': True, 'unit': GB_SYMBOL}},
    'firewall_block': {'block': {'min': 5, 'max': 100, 'inverted': False, 'unit': FIREWALL_BLOCK_UNIT_SYMBOL}, 'cpu_load': {'min': 1.1, 'max': 10, 'inverted': True, 'unit': CPU_LOAD_UNIT_SYMBOL}, 'size': {'min': 0.2, 'max': 10, 'inverted': True, 'unit': GB_SYMBOL}},
}

