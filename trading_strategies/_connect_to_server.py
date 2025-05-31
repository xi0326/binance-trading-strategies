from binance.spot import Spot
from binance.error import ClientError

def connect_to_server(self) -> tuple:
    self.logger.info("== Connecting to Binance server... ==")
    bn_client = Spot(self.config['api_key'], self.config['api_secret'])
    
    try:
        bn_client.account()
        self.logger.info("The server is connected.")
        is_connected = True

    except ClientError as error:
        self.logger.error("The server is NOT connected!!!")
        self.logger.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
        is_connected = False
    
    return is_connected, bn_client

if __name__ == '__main__':
    pass