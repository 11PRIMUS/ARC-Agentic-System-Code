from config import DATA_DIR
from agents.base_agent import Baseagent

def main():
    print("ARC-Agentic Reasoning Code")
    print(f"Data dir : {DATA_DIR}")

    try:
        print("BaseAgent class loaded")
    except Exception as e:
        print(f"error: {e}")


if __name__=="__main__":
    main()