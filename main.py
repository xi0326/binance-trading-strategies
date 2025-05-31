import os
import time
from trading_strategies import Strategy

def dca_strategy():
    # get the abs path of config.json
    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(CURRENT_PATH, "config.json")

    client = Strategy(CONFIG_PATH)
    client.logger.info("=== START TASK ===")

    if client.is_connected:
        
        # clear the staled orders
        if client.config['enable_revoke_stale_order']:
            client.cancel_staled_orders()

        redeem_response = client.redeem_flexible_product()

        if redeem_response['success']:
            client.logger.info("Waiting 10 seconds before placing order...")
            time.sleep(10)

        order_response = client.dca()

    else:
        order_response = {'success': False}

    client.logger.info("=== END TASK ===")

    if client.config['enable_email']:
        client.send_email(order_response)

if __name__ == '__main__':
    dca_strategy()