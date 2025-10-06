class TopicClassifier:
    def __init__(self):
        self.topic_patterns = {
            "spatial": ["spatial", "reasoning", "cube", "geometry", "distance", "room", "direction"],
            "sequence": ["sequence", "solving", "pattern", "series", "next", "number"],
            "mechanism": ["operation", "mechanisms", "machine", "gear", "factory", "mechanical"],
            "riddle": ["classic", "riddles", "riddle", "lateral", "thinking", "puzzle"],
            "optimization": ["optimization", "actions", "planning", "schedule", "minimize", "maximize"],
            "logical_trap": ["logical", "traps", "trap", "paradox", "logic", "impossible"]
        }
    
    def classify(self, topic, problem_text):
        t = topic.lower()
        problem_lower = problem_text.lower()
        
        #classification topic in train data
        if "spatial" in t and "reasoning" in t:
            return "spatial"
        elif "sequence" in t and "solving" in t:
            return "sequence"
        elif "operation" in t and "mechanism" in t:
            return "mechanism"
        elif "classic" in t and "riddle" in t:
            return "riddle"
        elif "lateral" in t and "thinking" in t:
            return "riddle" 
        elif "optimization" in t or ("actions" in t and "planning" in t):
            return "optimization"
        elif "logical" in t and "trap" in t:
            return "logical_trap"
        
        #fallback based on problem content
        if any(word in problem_lower for word in ["cube", "room","door","distance", "paint", "corner", "face", "side"]):
            return "spatial"
        elif any(word in problem_lower for word in ["sequence", "pattern", "next number","series", "continues"]):
            return "sequence"
        elif any(word in problem_lower for word in ["machine", "gear", "factory", "rotation", "mechanism", "cog"]):
            return "mechanism"
        elif any(word in problem_lower for word in ["riddle", "mystery", "puzzle", "strange", "how can this be"]):
            return "riddle"
        elif any(word in problem_lower for word in ["schedule", "planning", "minimize","maximize", "optimal", "time", "task"]):
            return "optimization"
        elif any(word in problem_lower for word in ["paradox", "impossible", "logic","statement", "true", "false"]):
            return "logical_trap"
        
        if "grid" in problem_text or "distance" in problem_text:
            return "spatial"
            
        return "unknown"
    
    def get_all_topics(self):
        return ["spatial", "sequence", "mechanism", "riddle", "optimization", "logical_trap"]
        