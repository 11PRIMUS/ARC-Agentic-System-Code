from config import DATA_DIR
from agents.base_agent import Baseagent
from agents.reasoning import ReasoningEngine
from problem_loader import ProblemLoader

def main():
    print("ARC-Agentic Reasoning Code")
    print(f"Data dir : {DATA_DIR}")

    print("\n1. Initializing components")
    engine = ReasoningEngine()
    loader = ProblemLoader()

    print("\n2. Loading problem data")
    if not loader.load_data("train.csv"):
        print("failed to load data")
        return
    
    print("\n3. Data Summary:")
    topic_counts = loader.get_topic_count()
    for topic, count in topic_counts.items():
        print(f"   {topic}: {count} problems")

    print(f"\n System status:")
    print(f" Registered agents: {len(engine.agents)}")
    print(f" Availabe problems: {loader.get_total_problem()}")

    if len(engine.agents)==0:
        print("\n No reasoning agents registered yet!")
        print("   Next step: Create and register specialized agents")
        print("   Each agent will evaluate problems independently")
        
        print("\n planned Agent Architecture:")
        planned_agents = [
            "SpatialAgent - geometric and spatial reasoning",
            "SequenceAgent - pattern recognition and sequences", 
            "OptimizationAgent - planning and resource allocation",
            "MechanismAgent - system operations and processes",
            "RiddleAgent - lateral thinking and puzzles",
            "LogicalAgent - logical reasoning and deduction"
        ]
        
        for agent in planned_agents:
            print(f"   • {agent}")
        print(f"\n SAMPLE Problems available:")
        sample_problems = loader.get_sample_problem(3)
        for i, problem in enumerate(sample_problems):
            print(f"{i+1}. {problem['topic']}")
            print(f"{problem['problem_statement'][:80]}...")
    else:
        print("\n4. Testing system with first problem:")
        problem =loader.get_problem(0)
        if problem:
            result =engine.solve_problem(problem)
            print(f"\n Result Summary:")
            print(f"   Success: {result['success']}")
            if result['success']:
                print(f"   Selected Agent: {result['selected_agent']}")
                print(f"   Answer: {result['answer']}")
                print(f"   Confidence: {result['confidence']:.2f}")
            else:
                print(f"   Error: {result.get('error', 'Unknown error')}")
    
    print(f"\n Pure agentic reasoning system initialized!")
    print("   Ready for specialized agents that compete based on problem analysis")

if __name__=="__main__":
    main()