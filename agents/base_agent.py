import time 
import re
from abc import ABC, abstractmethod

class Baseagent:
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.solved_count = 0
        self.total_attempts = 0
        self.solve_history = []

    @abstractmethod
    def can_handle(self, probelm_data):
        pass  
    @abstractmethod
    def solve(self, problem_data):
        pass
    
    def analyze_problem(self, probelm_text):
        problem_lower = probelm_text.lower()

        numbers = re.findall(r'\d+', probelm_text)
        has_question ='?' in probelm_text
        word_count =len(probelm_text.split())
        return {
            'numbers_found': numbers,
            'has_question': has_question,
            'word_count': word_count,
            'complexity': 'high' if word_count > 50 else 'medium' if word_count > 20 else 'low'
        }
    
    def record_attempt(self, success, execution_time=0,problem_data=None):
        self.total_attempts += 1
        if success:
            self.solved_count += 1
        
        self.solve_history.append({
            'success': success,
            'execution_time': execution_time,
            'timestamp': time.time(),
            'problem_topic': problem_data.get('topic', 'unknown') if problem_data else 'unknown'
        })
    
    def get_success_rate(self):
        if self.total_attempts == 0:
            return 0.0
        return self.solved_count / self.total_attempts
    
    def get_stats(self):
        return {
            'agent_name': self.agent_name,
            'success_rate': self.get_success_rate(),
            'total_attempts':self.total_attempts,
            'solved_count': self.solved_count,
            'avg_execution_time': self._get_avg_execution_time()
        }
    
    def get_avg_exetime(self):
        if not self.solve_history:
            return 0.0
        
        times =[h['execution_time'] for h in self.solve_history]
        return sum(times) / len(times)
    
    