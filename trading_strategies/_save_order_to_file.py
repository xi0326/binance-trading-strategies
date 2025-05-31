import os
import json

def save_order_to_file(self, symbol: str, order_id: int) -> None:
    data = []
    
    if os.path.isfile(self.config['pending_order_file']):
        with open(self.config['pending_order_file'], "r") as f:
            data = json.load(f)
    else:
        self.logger.info("Pending order file is not exist.")
        self.logger.info("Creating...")

    data.append({"symbol": symbol, "orderId": order_id})
    with open(self.config['pending_order_file'], "w") as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    pass