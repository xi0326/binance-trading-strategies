from binance.error import ClientError

def check_available_balance(self) -> dict:
    try:
        account_info = self._bn_client.account()
        self.logger.debug(account_info)
        available_balance = float([item['free'] for item in account_info['balances'] if item['asset'] == self.config['base_token']][0])
        dic = {'success': True, 'available_balance': available_balance}

        return dic
    
    except ClientError as error:
        self.logger.error("Unable to check available balance.")
        self.logger.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
        return {'success': False, 'available_balance': None}
    
if __name__ == '__main__':
    pass