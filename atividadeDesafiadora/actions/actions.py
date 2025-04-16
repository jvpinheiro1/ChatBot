from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet  # Importação adicionada aqui

class ActionBuscarLivro(Action):
    def name(self) -> Text:
        return "action_buscar_livro"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        titulo = tracker.get_slot("titulo_livro")
        autor = tracker.get_slot("nome_autor")
        assunto = tracker.get_slot("assunto_livro")

        # Simulando uma busca (substitua pela API real)
        if titulo:
            livros = [f"1. {titulo} (Autor Desconhecido)"]
        elif autor:
            livros = [f"1. Livro A de {autor}", f"2. Livro B de {autor}"]
        else:
            livros = [f"1. Livro sobre {assunto}", f"2. Outro livro sobre {assunto}"]

        resultados = "\n".join(livros)
        
        # Define o slot e envia a mensagem
        dispatcher.utter_message(text=f"Resultados:\n{resultados}")
        
        return [SlotSet("resultados_livros", resultados)]  # Define o slot