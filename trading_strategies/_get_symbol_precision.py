import math

from binance.error import ClientError

def get_symbol_precision(self, symbol: str) -> dict:
    self.logger.info("== Getting precision information... ==")
    try:
        info = self._bn_client.exchange_info(symbol=symbol)
        self.logger.info("Got the information from the server.")
        filters = info['symbols'][0]['filters']

        for f in filters:
            if f['filterType'] == 'LOT_SIZE':
                step_size = float(f['stepSize'])
                quantity_precision = abs(round(math.log10(step_size)))
            elif f['filterType'] == 'PRICE_FILTER':
                tick_size = float(f['tickSize'])
                price_precision = abs(round(math.log10(tick_size)))

        dic = {'success': True, 'quantity_precision': quantity_precision, 'price_precision': price_precision}
        return dic
    
    except ClientError as error:
        self.logger.info("Unable to get the information from the server.")
        self.logger.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
        
        dic = {'success': False, 'quantity_precision': None, 'price_precision': None}
        return dic
    
if __name__ == '__main__':
    pass