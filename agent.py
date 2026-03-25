import random
import pickle

class Agent:
    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.1
        self.epsilon =1.0

        self.epsilon_decay = 0.9995
        self.epsilon_min = 0.05

    def choose_action(self, state, available_actions):
        if random.random()< self.epsilon:
            return random.choice(available_actions)
        else:
            return max(available_actions, key=lambda a : self.get_q(state, a))
            
    def get_q(self, state, action):
        return self.q_table.get(state, {}).get(action, 0.0)
    
    def update(self, state, action, reward, next_state, next_actions, done):
        current_q= self.get_q(state, action)
        if done:
            target = reward
        else:
            best_next_q = max(self.get_q(next_state, a) for a in next_actions)
            target = reward + 0.95*best_next_q
        new_q = current_q + self.learning_rate*(target - current_q)
        
        if state not in self.q_table:
            self.q_table[state] ={}
        
        self.q_table[state][action] = new_q
        
        self.epsilon = max(self.epsilon_min, self.epsilon*self.epsilon_decay) 

    def load_q_table(self, file_path):
        try:
            with open(file_path, "rb") as f:
                self.q_table = pickle.load(f)
            self.epsilon = self.epsilon_min
            print(f"Loaded{len(self.q_table)} states from {file_path}")
        except FileNotFoundError:
            print("no saved q-table found. start from scratch")
