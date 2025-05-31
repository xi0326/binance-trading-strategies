from binance.error import ClientError

def get_flexible_product_position(self) -> dict:
    try:
        response = self._bn_client.get_flexible_product_position(
            current=1, size=100, recvWindow=5000
        )
        self.logger.debug(response)
        position = [item for item in response['rows'] if item['asset'] == self.config['base_token']][0]
        dic = {'success': True, 'position': position}

        return dic
    
    except ClientError as error:
        self.logger.error("Unable to get position name.")
        self.logger.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
        return {'success': False, 'position': None}
    
    except:
        self.logger.warning("There is no position of the reddem token or it is unsupported.")
        return {'success': False, 'position': None}
    
if __name__ == '__main__':
    pass