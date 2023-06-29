import asyncio
import os

from Client import WebClient
import Explainer
import ExplainerSystem
import JsonWriter
import MakeQuery
import WebAPI
from PowerpointReader import PowerpointReader


def test_system():
    WebAPI.start()
    ExplainerSystem.start()
    client = WebClient()
    while True:
        uid = client.upload(input("Please enter path to a powerpoint\n"))
        client.status(uid)

    print("end")
