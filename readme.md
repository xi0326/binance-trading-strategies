# Trading strategies for Binance
[![Python version](https://img.shields.io/pypi/pyversions/binance-connector)](https://www.python.org/downloads/)

This is a lightweight python library that contains some trading strategies for Binance.

### Prerequisite
```bash
pip install binance-connector
```
https://github.com/binance/binance-connector-python

## Usage examples:
```python
from trading_strategies import Strategy

client = Strategy("config.json")

# Check available balance
dic = client.check_available_balance()

# Get flexible earning product position
dic = client.get_flexible_product_position()

# Redeem from flexible earning product
dic = client.redeem_flexible_product()

# Clear the staled orders
client.cancel_staled_orders()

# Run DCA
order_response = client.dca()

# Send the log file to a specified email
client.send_email(order_response)
```

### Using crontab to do the strategy automatically
Edit crontab setting
```bash
crontab -e
```
E.g. Do the strategy at every Monday 10:30 AM
```text
30 10 * * 1 bash /home/opc/binance/run_dca.sh
```
Edit the path in the example bash file
```bash
#!/bin/bash

# activate conda env
source /home/<user name>/anaconda3/etc/profile.d/conda.sh
conda activate <environment name>

# run python script
python <the absolutely path>/main.py
```

## Filling the information in config.json
```json
{
    "api_key": "",
    "api_secret": "",
    "base_token": "USDT", // the base token name 
    "dca_amount": 50,   // the amount of the token redeeming from the flexible earning product
    "quote_token": "BNB",  // the quote token name
    "offset": 50,   // the offset
    "max_price": 1000,  //
    "log_dir": "./logs",
    "pending_order_file": "pending_orders.json",
    "enable_revoke_stale_order": true,  // cancel the staled order
    "enable_email": false,  // send the task log to a specified email address

    "email": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 465,
    "sender": "",
    "app_password": "",
    "receiver": "",
    "subject": "Binance Automated Trading Result"
  }
}
```