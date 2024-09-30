from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckOrderStatus(Action):

    def name(self) -> Text:
        return "action_check_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        order_number = tracker.get_slot('order_number')
        # Aqui você pode buscar o status do pedido em um banco de dados ou API
        # Exemplo de resposta fictícia
        order_status = "O seu pedido {} está a caminho e deve chegar em 3 dias úteis.".format(order_number)
        
        dispatcher.utter_message(text=order_status)
        return []

class ActionInquireReturnPolicy(Action):

    def name(self) -> Text:
        return "action_inquire_return_policy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Mensagem padrão sobre a política de devolução
        return_policy_message = (
            "Você pode devolver produtos em até 30 dias após a compra, "
            "desde que estejam em condições originais. Precisa de ajuda com isso?"
        )
        
        dispatcher.utter_message(text=return_policy_message)
        return []

class ActionInquirePromotions(Action):

    def name(self) -> Text:
        return "action_inquire_promotions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Mensagem padrão sobre promoções
        promotions_message = (
            "Atualmente, temos uma promoção de 20% em todas as roupas de verão! "
            "Gostaria de saber mais sobre algum produto específico?"
        )
        
        dispatcher.utter_message(text=promotions_message)
        return []

class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        goodbye_message = "Até logo! Se precisar de mais ajuda, estou aqui."
        dispatcher.utter_message(text=goodbye_message)
        return []
