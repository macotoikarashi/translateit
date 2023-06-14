import placeholders as ph
import json,copy,random

class DialogueData:
    def __init__(self,dia_json="",trans_json="") -> None:
        self.dia_json = dia_json
        self.trans_json = trans_json
        self.dia_dict = json.loads(dia_json) if dia_json else {}
        self.trans_dict = json.loads(trans_json) if trans_json else {}
        self.x = 0
        self.y = 0
        self.q_dict = {}

    def set(self,dia_json,trans_json):
        self.dia_json = dia_json
        self.trans_json = trans_json
        self.dia_dict = json.loads(dia_json) if dia_json else {}
        self.trans_dict = json.loads(trans_json) if trans_json else {}
        self.x = 0
        self.y = 0
        self.q_dict = {}

    def set_question(self):
        self.x = random.randint(0,len(self.dia_dict["dialogue"])-1)
        self.y = random.randint(0,len(self.dia_dict["dialogue"][self.x]["content"])-1)
        self.q_dict = copy.deepcopy(self.dia_dict)
        self.q_dict["dialogue"][self.x]["content"][self.y] = copy.copy(self.trans_dict["dialogue"][self.x]["content"][self.y])

    def q_english(self):
        if (not self.q_dict) and self.q_dict["dialogue"][self.x]["content"][self.y]==self.trans_dict["dialogue"][self.x]["content"][self.y]:
            return self.dia_dict["dialogue"][self.x]["content"][self.y]
        else:
            return False
    def q_japanese(self):
        if (not self.q_dict) and self.q_dict["dialogue"][self.x]["content"][self.y]==self.trans_dict["dialogue"][self.x]["content"][self.y]:
            return self.trans_dict["dialogue"][self.x]["content"][self.y]
        else:
            return False


if __name__=="__main__":
    data = DialogueData()
    dia_json = ph.returnDialogue("test keywords")
    trans_json = ph.returnJapanese(dia_json)
    data.set(dia_json,trans_json)
    data.set_question()

    print(data.q_dict)
    print(data.dia_dict["dialogue"][data.x]["content"][data.y])

