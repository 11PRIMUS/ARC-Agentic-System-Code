from config import DATA_DIR
from agents.base_agent import Baseagent
from problem_loader import ProblemLoader

def main():
    print("ARC-Agentic Reasoning Code")
    print(f"Data dir : {DATA_DIR}")

    print("\n1. Initializing components")
    loader = ProblemLoader()

    print("\n2. Loading problem data")
    if not loader.load_data("train.csv"):
        print("failed to load data")
        return
    print("\n3. Data Summary:")
    topic_counts = loader.get_topic_count()
    for topic, count in topic_counts.items():
        print(f"   {topic}: {count} problems")

    print("\n4. Testing with first problem:")
    problem = loader.get_problem(0)
    if problem:
        print(f"   Topic: {problem['topic']}")
        print(f"   Problem: {problem['problem_statement'][:100]}...")
        
        #classified_topic = classifier.classify(problem['topic'], problem['problem_statement'])
        #print(f"   Classified as: {classified_topic}")
        
        print(f"   Answer options:")
        for i in range(1, 6):
            print(f"     {i}. {problem[f'answer_option_{i}']}")
    
    print("\n system ready for reasoning agents!")



if __name__=="__main__":
    main()