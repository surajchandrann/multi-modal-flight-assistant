from src.database import get_ticket_price

from src.database import get_ticket_price

price_function = {
    "name": "get_ticket_price",
    "description": "Get return ticket price to destination city",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {"type": "string", "description": "Travel destination city"}
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

TOOLS = [{"type": "function", "function": price_function}]
