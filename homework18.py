import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

file = logging.FileHandler("homework.log", encoding="utf-8")
file.setLevel(logging.DEBUG)

logger.addHandler(console)
logger.addHandler(file)

def divide(a, b):
    logger.debug("divide(a=%s, b=%s)", a, b)

    try:
        result = a / b
        logger.info("Result: %s", result)
        return result
    except ZeroDivisionError:
        logger.error("Error: division by zero")
        return None

divide(10, 2)
divide(10, 0)