import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    try:
        result = a / b
        logging.info("Division successful")
        return result
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0))