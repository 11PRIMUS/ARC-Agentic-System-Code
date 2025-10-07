import pandas as pd
from config import DATA_DIR

class ProblemLoader:
    def __init__(self):
        self.data =None
        self.loaded =False
    
    #load problems from train.csv
    def load_data(self, filename="train.csv"): 
        try:
            filepath =DATA_DIR +filename
            self.data = pd.read_csv(filepath)
            self.loaded = True
            print(f" loaded {len(self.data)} problems from {filename}")
            return True
        
        except FileNotFoundError:
            print(f"error could not find {filename}")
            return False
        except Exception as e:
            print(f"error loading data: {e}")
            return False

    #get specific problem by index    
    def get_problem(self, index):
        if not self.loaded:
            return None
        if index >=len(self.data):
            return None
        
        row= self.data.iloc[index]
        return {
            'topic': row['topic'],
            'problem_statement':row['problem_statement'],
            'answer_option_1': row['answer_option_1'],
                'answer_option_2': row['answer_option_2'],
                'answer_option_3': row['answer_option_3'],
                'answer_option_4': row['answer_option_4'],
                'answer_option_5': row['answer_option_5'],
                'index':index
        }
    
    #get all problem for specifc topic
    def get_problem_topic(self, topic):
        if not self.loaded:
            return []
        filtered =self.data[self.data['topic'] == topic]
        problems =[]

        for idx, row in filtered.iterrows():
            problems.append({
                'topic': row['topic'],
                'problem_statement': row['problem_statement'],
                'answer_option_1': row['answer_option_1'],
                'answer_option_2': row['answer_option_2'],
                'answer_option_3': row['answer_option_3'],
                'answer_option_4': row['answer_option_4'],
                'answer_option_5': row['answer_option_5'],
                'index': idx
            })
        
        return problems
    

        