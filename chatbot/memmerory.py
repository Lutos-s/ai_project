class ChatMemory:
    def __init__(self,system_prompt):
        self.messages = [{"role":"system","content":system_prompt}]
    def add_user(self,user_input):
        self.messages.append({"role":"user","content":user_input})
    def add_assistant(self,assistant):
        self.messages.append({"role":"assistant","content":assistant})
    def get(self):
        return self.messages