class EndpointLogger:
    def __init__(self , endpoint_url ):
        self.endpoint_url = endpoint_url
        self.failed_payloads = []
        
logger = EndpointLogger("/api/v1/chat")
print(logger.failed_payloads)        