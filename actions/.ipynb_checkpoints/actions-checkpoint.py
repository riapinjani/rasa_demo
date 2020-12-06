from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class balanceform(FormAction):

    def name(self):
        return "balance_form" # define form name
        
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
         return["card_number"] # define slots that are required
         
    def slot_mappings(self) -> Dict[Text, Any]:
     
        return{"card_number" : self.from_entity(entity = "card_number", intent = "check_balance")}
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
     
        import random
        import pandas as pd

        first_6=400000 # IIN For Banking Industry(6 digits)
        def luhn():
            global first_6  
            card_no = [int(i) for i in str(first_6)]  # To find the checksum digit on
            card_num = [int(i) for i in str(first_6)]  # Actual account number
            seventh_15 = random.sample(range(9), 9)  # Acc no (9 digits)
            for i in seventh_15:
                card_no.append(i)
                card_num.append(i)
            for t in range(0, 15, 2):  # odd position digits
                card_no[t] = card_no[t] * 2
            for i in range(len(card_no)):
                if card_no[i] > 9:  # deduct 9 from numbers greater than 9
                    card_no[i] -= 9
        s = sum(card_no)
        mod = s % 10
        check_sum = 0 if mod == 0 else (10 - mod)
        card_num.append(check_sum)
        card_num = [str(i) for i in card_num]
        return ''.join(card_num)

        numbers = []
        for i in range(100):
            n = luhn()
        numbers.append(n)
    
    

        balance = []
        for i in range(0,100):
            n = random.randint(0,10000)
        balance.append(n)
    

        df = pd.DataFrame()
        df['card_number'] = numbers
        df['account_balance'] = balance        
        card_number = tracker.get_slot("card_number") #pull current value
        account_balance = df["account_balance"][df["card_number"] == card_number]
            
        if account_balance is None:
                   dispatcher.utter_message("Card number not found! Please try again.")
        else:
                   dispatcher.utter_message("Account balance :")
                   return[]
                    

                   
        
    
    

    
    

                   
        
    
    

    
    
