from binance.error import ClientError

def redeem_flexible_product(self) -> dict:
    position_response = self.get_flexible_product_position()
    available_balance_response = self.check_available_balance()
    self.logger.info("== Start redeeming... ==")

    if (position_response['success']):
        product_id = position_response['position']['productId']
    else:
        self.logger.error("Unable to get the flexible position.")

    if (available_balance_response['success']):
        redeem_amount = self.config['dca_amount'] - available_balance_response['available_balance']
        if redeem_amount <= 0:
            self.logger.info("The amount in the spot account is enough, no need to redeem.")
        else:
            self.logger.info("Actually redeem amount: {}.".format(redeem_amount))
    else:
        redeem_amount = self.config['dca_amount']
        self.logger.info("Unable to get available balance, actually redeem amount: {}.".format(redeem_amount))

    try:
        response = self._bn_client.redeem_flexible_product(
            product_id, amount=redeem_amount, recvWindow=5000
        )
        self.logger.debug(response)
        self.logger.info("Redeem successful! {} {} is redeemed to spot account.".format(redeem_amount, self.config['base_token']))

    except ClientError as error:
        self.logger.warning(
            "Found warning. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
        return {'success': False, 'response': {}}

    dic = {'success': True, 'response': response}
    return dic

if __name__ == '__main__':
    pass