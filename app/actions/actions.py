from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType

class ActionCheckOrderStatus(Action):
    def name(self) -> Text:
        return "action_check_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:

        # Extrai o número do pedido da entidade
        order_number = next(tracker.get_latest_entity_values("order_number"), None)

        if order_number:
            dispatcher.utter_message(text=f"Ótimo! Um momento, por favor, enquanto verifico o status do seu pedido {order_number}...")
            # Aqui você deve adicionar a lógica para verificar o status do pedido
            dispatcher.utter_message(text=f"O seu pedido {order_number} está a caminho e deve chegar em 3 dias úteis.")
        else:
            dispatcher.utter_message(text="Desculpe, não consegui entender o número do seu pedido.")

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
