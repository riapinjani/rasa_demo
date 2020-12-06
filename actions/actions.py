from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT, FormValidationAction
from rasa_sdk.types import DomainDict

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, 
         dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text= "Hello World!")
        
        return []

class ValidateCheckBalanceForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_balance_form"

    @staticmethod
    def card() -> List[Text]:
        """List of required slots to check balance"""

        return ["card_number"]

    def validate_card_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate card number."""

        if slot_value.lower() in self.card():
            # validation succeeded, set the value of the "card_number" slot to value
            return {"card_number": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"card_number": None}

class BalanceForm(Action):
    def name(self) -> Text:
        print("Entered BalanceForm Class")
        return "action_balance_form"

    def run(self,
        dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any],
        ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text= "Balance Form is working!!!")
        return [AllSlotsReset()]

class AskForSlotAction(Action):
    def name(self) -> Text:
        return "action_ask_card_number"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="What is your card number?")
        return []

   
         

    
    
        

                    

                   
        
    
    

    
    

                   
        
    
    

    
    

                    

                   
        
    
    



                   
        
    
    

    
    

                   
        
    
    

    
    
                    

                   
        
    
    

    
    

                   
        
    
    

    
    
