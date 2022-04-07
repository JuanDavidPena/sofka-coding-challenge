
class Question:
    """Question class to organize, obtain and check questions"""
    def __init__(self, question):
        self.prompt = question[0] 
        self.a = question[1]
        self.b = question[2]
        self.c = question[3]
        self.d = question[4]
        self.answer =question[5]

    def check_answer(self, input):
        """Checks if the input option matches the correct answer.
           returns True if the answer is correct, False if not"""
        if input == "a":
            if self.a == self.answer:
                return True
            else: return False
        elif input == "b":
            if self.b == self.answer:
                return True
            else: return False
        elif input == "c":
            if self.c == self.answer:
                return True
            else: return False
        elif input == "d":
            if self.d == self.answer:
                return True
            else: return False
    
    def get_full_prompt(self):
        """Builds the full question prompt Question + options"""
        return self.prompt + "\n (a)" + self.a + "\n (b)" + self.b + "\n (c)" + self.c + "\n (d)" + self.d + "\n\n"