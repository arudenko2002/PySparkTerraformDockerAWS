import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO) # Set the log level within your code

def handler(event, context):
    logger.info("This is an INFO level log message.")
    logger.warning("This is a WARNING level log message.")
    logger.error("This is an ERROR level log message.")

    # You can also log structured data in JSON format
    logger.info(json.dumps({"message": "Custom event processed", "details": event}))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Alexey Lambda with custom Log Group!')
    }