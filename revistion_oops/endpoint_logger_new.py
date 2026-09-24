class EndpointLogger:
    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url
        self.failed_payloads = []
        
    # Method 1: Add the payload to the list
    def log_failure(self, payload):
        # We grab our list and append the new item to it
        self.failed_payloads.append(payload)

    # Method 2: Return the count of items in the list
    def get_failure_count(self):
        # We use len() to count how many items are in our list, and return that number
        return len(self.failed_payloads)

# --- Execution ---
logger = EndpointLogger("/api/v1/chat")

# 1. Call the method to log a failure
logger.log_failure("timeout_error_1")

# 2. Print the count
print(logger.get_failure_count())