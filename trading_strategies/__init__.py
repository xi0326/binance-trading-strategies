class Strategy():
    def __init__(self, config_file_name: str):
        self.config = self.load_config(config_file_name)
        self.logger, self._log_path = self.setup_logging()
        self.is_connected, self._bn_client = self.connect_to_server()

    from ._cancel_staled_orders import cancel_staled_orders
    from ._check_available_balance import check_available_balance
    from ._connect_to_server import connect_to_server
    from ._dca import dca
    from ._email_notification import send_email
    from ._get_flexible_product_position import get_flexible_product_position
    from ._get_symbol_precision import get_symbol_precision
    from ._redeem_flexible_product import redeem_flexible_product
    from ._save_order_to_file import save_order_to_file
    from ._utils import load_config, setup_logging