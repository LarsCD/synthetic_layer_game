"""
Config file used for extra stat information for hardware and software
"""

ITEM_STAT_CONFIG = {
    'ram': {'size': {'min': 1, 'max': 32, 'inverted': False, 'unit': 'GB'}, 'speed': {'min': 10, 'max': 100, 'inverted': False, 'unit': 'Spd'}},
    'cpu': {'cpu_increase': {'min': 1, 'max': 2.5, 'inverted': False, 'unit': 'x'}, 'heat_generation': {'min': 5, 'max': 50, 'inverted': True, 'unit': 'Heat'}},
    'firewall_shield': {'block': {'min': 5, 'max': 95, 'inverted': False, 'unit': '%'}, 'cpu_load': {'min': 1.1, 'max': 10, 'inverted': True, 'unit': 'Load'}, 'size': {'min': 0.2, 'max': 10, 'inverted': True, 'unit': 'GB'}},
    'firewall_block': {'block': {'min': 5, 'max': 100, 'inverted': True, 'unit': 'pts'}, 'cpu_load': {'min': 1.1, 'max': 10, 'inverted': True, 'unit': 'Load'}, 'size': {'min': 0.2, 'max': 10, 'inverted': True, 'unit': 'GB'}},
}