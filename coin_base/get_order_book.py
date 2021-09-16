import websocket
import json
import logging

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s %(funcName)s():%(lineno)i: - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#workers
from work_functions.store_functions import print_it
from work_functions.store_functions import store_json
from work_functions.store_functions import  store_change_data



in_stream_proc = [ print_it, store_json,  store_change_data] 

class coin_base_feed:
    def __init__(self):
        self.url = "wss://ws-feed.pro.coinbase.com" 
        self.state                      = "loading"
        self.ws                         = None
        self.connection_state           = "Not Connected"

    def start( self ):
        self.ws = websocket.WebSocketApp(self.url,
                              on_open=self.on_open,
                              on_message=self.on_message,
                              on_error=self.on_error,
                              on_close=self.on_close)
        self.ws.run_forever()

    def on_error(self, ws, error):
        logger.error(error)

    def on_close(self, ws):
        logger.info("### closed ###")

    def on_open(self, ws):
        self.connection_state           = "Connected"
        logger.info("### open ###")

        self.ws.send( json.dumps({
                            "type": "subscribe",
                            "product_ids": [
                            "BTC-USD"
                        ],  
                        "channels": [
                        "level2",
                        "heartbeat",
                            {
                                "name": "ticker",
                                    "product_ids": [
                                        "BTC-USD"
                            ]
                            }
                        ]
                    }))

    def on_message(self, ws, message):
        data = json.loads(message)

        if data['type'] == 'l2update':
            for p in in_stream_proc:
                p(data, None)

cbb_f = coin_base_feed()
cbb_f.start()

