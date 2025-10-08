import re
import time
from ..base_agent import Baseagent

class Spatial(Baseagent):
    def __init__(self):
        super().__init__("spatialagent")
        self.spatial_key=[
            'room', 'corner', 'wall', 'door', 'table', 'lamp', 'chair',
            'cube', 'painted', 'faces', 'smaller', 'divided',
            'circle', 'square', 'triangle', 'rectangle', 'shape',
            'grid', 'coordinate', 'position', 'distance', 'direction',
            'north', 'south', 'east', 'west', 'left', 'right', 'center',
            '3d', '2d', 'dimension', 'rotate', 'mirror', 'flip',
            'volume', 'area', 'perimeter', 'geometry', 'spatial',
            'place', 'arrange', 'layout', 'configuration'
        ]
    def can_handle(self, problem_data):
        problem_text =problem_data.get('problem_statement', '').lower()
        topic=problem_data.get('topic','').lower()

        confidence =0.0
        if 'spatial' in topic:
            confidence+=0.7
        
        #key matching
        key_matches =sum(1 for key in self.spatial_key if key in problem_text)
        confidence +=min(0.4, key_matches*0.05)

        #geometric indicator
        if any(word in problem_text for word in ['painted cube', 'faces painted', 'smaller cubes']):
            confidence +=0.03
        if any(word in problem_text for word in ['room', 'corner', 'place']):
            confidence += 0.2
        
        return min(1.0, confidence)
    