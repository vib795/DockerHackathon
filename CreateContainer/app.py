import logging
from new_service import voice_assistant

logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.DEBUG, filemode='w')

def app():
    voice_assistant()

if __name__ == "__main__":
    app()