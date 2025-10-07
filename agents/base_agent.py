class Baseagent:
    def __init__(self, agent_type):
        self.agent_type =agent_type
        self.solved_count=0
        self.total_attempts=0
    
    def solve(self, problem_data):
        raise NotImplementedError("must implement solve method")
    
    def can_handle(self, topic, problem_text):
        return 0.0  #confidence score
    
    def success_rate(self):
        if self.total_attempts==0:
            return 0.0
        return self.solved_count /self.total_attempts
    
    def record_attempt(self, success):
        self.total_attempts +=1
        if success:
            self.solved_count +=1
    
    