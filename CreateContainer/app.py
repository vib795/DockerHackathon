import logging
from new_service import voice_assistant

logging.basicConfig(filename='logger.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(threadName)-10s %('
                                                                      'message)s',)

def app():
    voice_assistant()

if __name__ == "__main__":
    app()