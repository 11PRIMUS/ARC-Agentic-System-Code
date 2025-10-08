import time
from typing import List, Dict, Any

class ReasoningEngine: #without topic classification
    
    def __init__(self):
        self.agents = []
        self.solve_history =[]
        self.session_id = None
    
    def register_agent(self, agent):
        self.agents.append(agent)
        print(f"registered {agent.agent_name} agent")
    
    def solve_problem(self, problem_data):
        start_time = time.time()
        
        print(f"\n Analyzing problem: {problem_data.get('topic', 'Unknown topic')}")
        print(f"Problem: {problem_data['problem_statement'][:100]}...")
        #step-1
        agent_evaluations = self.evaluate_agents(problem_data)
        
        if not agent_evaluations:
            return {
                'success': False,
                'error': 'No agents available to handle this problem',
                'execution_time': time.time() - start_time
            }
        
        #step 2
        best_agent, confidence = self.select_best_agent(agent_evaluations)
        
        print(f"Selected {best_agent.agent_name} (confidence: {confidence:.2f})")
        
        #step-3
        try:
            result = best_agent.solve(problem_data)
            execution_time =time.time() - start_time
            self.record_solve(best_agent, result, execution_time, problem_data)
            
            return {
                'success': True,
                'answer': result.get('answer', 'No answer provided'),
                'reasoning': result.get('reasoning','No reasoning provided'),
                'selected_agent': best_agent.agent_name,
                'confidence': confidence,
                'execution_time': execution_time,
                'agent_evaluations':{agent.agent_name: conf for agent, conf in agent_evaluations.items()}
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            print(f" error with {best_agent.agent_name}: {str(e)}")
            return self.fallback_agents(agent_evaluations, problem_data, start_time)
    
    def evaluate_agents(self, problem_data):
        evaluations = {}
        
        print("Agent evaluations:")
        for agent in self.agents:
            try:
                confidence =agent.can_handle(problem_data)
                evaluations[agent] = confidence
                print(f"   {agent.agent_name}:{confidence:.2f}")
            except Exception as e:
                print(f"   {agent.agent_name}: ERROR - {str(e)}")
                evaluations[agent] = 0.0
        
        return evaluations
    
    #confifence best agent selection
    def select_best_agent(self, evaluations):
        if not evaluations:
            return None, 0.0
        
        best_agent =max(evaluations, key=evaluations.get)
        best_confidence = evaluations[best_agent]
        
        return best_agent, best_confidence
    
    def fallback_agents(self, evaluations, problem_data, start_time):
        sorted_agents = sorted(evaluations.items(), key=lambda x: x[1], reverse=True)
        
        for agent, confidence in sorted_agents[1:]:  #first skip
            if confidence>0.3: 
                print(f"Trying fallback: {agent.agent_name} (confidence: {confidence:.2f})")
                try:
                    result = agent.solve(problem_data)
                    execution_time = time.time() - start_time
                    
                    return {
                        'success': True,
                        'answer': result.get('answer', 'No answer provided'),
                        'reasoning': result.get('reasoning', 'Solved with fallback agent'),
                        'selected_agent': f"{agent.agent_name} (fallback)",
                        'confidence': confidence,
                        'execution_time': execution_time
                    }
                except Exception as e:
                    print(f"Fallback {agent.agent_name} also failed: {str(e)}")
                    continue
        
        # All agents failed
        return {
            'success': False,
            'error': 'All capable agents failed to solve the problem',
            'execution_time': time.time() - start_time
        }
    
    def record_solve(self, agent, result, execution_time, problem_data):
        self.solve_history.append({
            'agent_name': agent.agent_name,
            'success':result.get('success', True),
            'execution_time':execution_time,
            'problem_topic': problem_data.get('topic', 'unknown'),
            'timestamp': time.time()
        })
    
    def system_stats(self):
        if not self.solve_history:
            return {
                'total_problems_solved': 0,
                'system_success_rate': 0.0,
                'registered_agents': len(self.agents),
                'agent_stats':[agent.get_stats() for agent in self.agents]
            }
        
        successful_solves = sum(1 for h in self.solve_history if h['success'])
        
        return {
            'total_problems_solved': len(self.solve_history),
            'system_success_rate': successful_solves / len(self.solve_history),
            'registered_agents': len(self.agents),
            'avg_execution_time': sum(h['execution_time'] for h in self.solve_history) / len(self.solve_history),
            'agent_stats':[agent.get_stats() for agent in self.agents]
        }
    
    def list_agents(self):
        if not self.agents:
            print("No agents registered")
            return
        
        print("Registered agents:")
        for agent in self.agents:
            stats = agent.get_stats()
            print(f"  • {agent.agent_name} (Success rate: {stats['success_rate']:.1%})")