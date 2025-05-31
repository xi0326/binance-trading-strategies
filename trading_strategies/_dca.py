import math

# from ._get_symbol_precision import get_symbol_precision
# from ._save_order_to_file import save_order_to_file

from binance.error import ClientError

def dca(self) -> dict:
    self.logger.info("== Making DCA order... ==")

    try:
        self.logger.info("Getting the price...")
        ticker = self._bn_client.ticker_24hr(self.config['quote_token'] + self.config['base_token'])
        self.logger.debug(ticker)

    except ClientError as error:
        self.logger.error("Unable to get the price.")
        self.logger.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
        return {'success': False, 'response': {}}
    
    symbol = ticker['symbol']
    avg_price = avg_price = float(ticker['lastPrice']) + (float(ticker['openPrice']) - float(ticker['lastPrice'])) / 2
    current_price = float(ticker['lastPrice'])

    if current_price - self.config['offset'] < avg_price:
        target_price = current_price - self.config['offset']
    else:
        target_price = avg_price

    if target_price > self.config['max_price']:
        self.logger.warning(f"Target price {target_price} is higher than max allowed {self.config['max_price']}. Skip placing order.")
        return {'success': False, 'response': {}}

    symbol_precision_response = self.get_symbol_precision(symbol)

    if (symbol_precision_response['success']):
        buy_quantity = math.floor(self.config['dca_amount'] / (current_price - self.config['offset']) * (10 ** symbol_precision_response['quantity_precision'])) / 10 ** symbol_precision_response['quantity_precision']
        buy_price = round(target_price, symbol_precision_response['price_precision'])
    else:
        self.logger.error("The order has failed.")
        return {'success': False, 'response': {}}

    params = {
    'symbol': symbol,
    'side': 'BUY',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': buy_quantity,
    'price': buy_price
    }

    try:
        response = self._bn_client.new_order(**params)
        self.logger.info(response)
        self.logger.info("Order successful! The price is {}.".format(buy_price))
        self.save_order_to_file(response['symbol'], response['orderId'])

        dic = {'success': True, 'response': response}
        
        return dic
    
    except ClientError as error:
        self.logger.error("The order has failed.")
        self.logger.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
        return {'success': False, 'response': {}}

if __name__ == '__main__':
    pass