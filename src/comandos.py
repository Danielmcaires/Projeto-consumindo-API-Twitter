import tweepy
import uvicorn
import src.codigos

from src.conexao import trends_collection
from src.servicos import get_trends
from typing import Any, Dict, List
from pymongo import MongoClient
from datetime import datetime


def InserirDados():
    LimpaDados()
    #Comando inserido no interesse de se renovar as informações sem acúmulo histórico
    for pais, codigo in src.codigos.CodigoWOEID.items():
        TopTrends = get_trends(codigo)
        trends_collection.insert_many(TopTrends)
        ColocarDataePais(pais)

def ColocarDataePais(pais):
    trends_collection.update_many(
        {
            'data': {'$exists' : False}

        },
        {
            '$set' : 
            {
                'data': datetime.now().isoformat(),
                'País': pais
            }
        }
    )

def LimpaDados():
    trends_collection.delete_many({})