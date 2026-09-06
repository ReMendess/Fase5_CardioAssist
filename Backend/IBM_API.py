"""
CardioAssist — Configuração e cliente do IBM Watson Assistant.

As credenciais podem ser sobrescritas mediante variáveis de ambiente
(WATSON_API_KEY, WATSON_SERVICE_URL, WATSON_ASSISTANT_ID, WATSON_ENVIRONMENT_ID).
"""

import os

from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Credenciais padrão da instância do projeto
API_KEY = os.getenv(
    "WATSON_API_KEY",
    "rWaXw3Z1IH4BRz81ieCc8vU47-AEVLS04HFi4e_LDjdw",
)
SERVICE_URL = os.getenv(
    "WATSON_SERVICE_URL",
    "https://api.au-syd.assistant.watson.cloud.ibm.com/instances/6a85b3b0-abec-4c29-a049-d5e81cdcf37e",
)
ASSISTANT_ID = os.getenv(
    "WATSON_ASSISTANT_ID",
    "7d7821eb-79cd-41cd-b2d3-aa69a7fb5dfd",
)
ENVIRONMENT_ID = os.getenv(
    "WATSON_ENVIRONMENT_ID",
    "dc384931-f3e6-4535-8cc1-c346993fef48",
)

# Versão da API de Watson Assistant usada pelo SDK
VERSION = "2024-08-25"

# Timeout de rede para as chamadas a Watson (segundos)
WATSON_TIMEOUT = 30


def get_assistant() -> AssistantV2:
    """Retorna un cliente AssistantV2 autenticado y listo para usar."""
    authenticator = IAMAuthenticator(API_KEY)
    assistant = AssistantV2(version=VERSION, authenticator=authenticator)
    assistant.set_service_url(SERVICE_URL)
    assistant.set_http_config({"timeout": WATSON_TIMEOUT})
    return assistant
