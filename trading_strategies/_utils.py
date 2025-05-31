import os
import json
import logging
from datetime import datetime

def load_config(self, path: str = "config.json") -> dict:
    with open(path, 'r') as file:
        return json.load(file)

def setup_logging(self) -> tuple:
    # for jupyter
    root_logger = logging.getLogger()
    if root_logger.hasHandlers():
        root_logger.handlers.clear()
    
    os.makedirs(self.config['log_dir'], exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = "log_{}.txt".format(timestamp)
    log_path = os.path.join(self.config['log_dir'], log_filename)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_path, mode='w', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__), log_path

if __name__ == '__main__':
    pass