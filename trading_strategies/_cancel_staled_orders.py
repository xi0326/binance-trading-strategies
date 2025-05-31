import os
import json

from binance.error import ClientError

def cancel_staled_orders(self) -> None:
    if not os.path.isfile(self.config['pending_order_file']):
        return

    with open(self.config['pending_order_file'], "r") as f:
        orders = json.load(f)

    self.logger.info("=== Cancelling the staled orders ===")
    still_pending = []
    for order in orders:
        try:
            order = self._bn_client.get_order(symbol=order["symbol"], orderId=order["orderId"])
            if order["status"] in ("NEW", "PARTIALLY_FILLED"):
                self._bn_client.cancel_order(symbol=order["symbol"], orderId=order["orderId"])
                self.logger.info("The stale order id {} for {} is cancelled".format(order['orderId'], order['symbol']))
            else:
                self.logger.info("Order {} already {}".format(order['orderId'], order['status']))
        except ClientError as error:
            self.logger.error("Unable to check the order id.")
            self.logger.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
            still_pending.append(order)  # keep the orders

    # Clear or keep only the orders that are not yet processed.
    with open(self.config['pending_order_file'], "w") as f:
        json.dump(still_pending, f, indent=2)

if __name__ == '__main__':
    pass