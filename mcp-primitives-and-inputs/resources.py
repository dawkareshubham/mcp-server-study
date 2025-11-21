from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resources")

@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """
    Returns an overview inventory
    """
    overview = """
    Inventory overview:
    - Coffee
    - Tea
    - Cookies
    """
    return overview.strip()


inventory_id_to_price = {
    "123": "3.5",  
    "456": "2.5",
    "789": "1.5"
}

inventory_id_to_name = {
    "123": "Coffee",
    "456": "Tea",
    "789": "Cookies"
}

@mcp.resource("inventory://{inventory_id}/price")
def get_inventory_price_from_inventory_id(inventory_id: str) -> str:
    """
    Returns the price from inventory id
    Args:
        inventory_id: the ID of the inventory item
    """
    return inventory_id_to_price.get(inventory_id, "Unknown")


@mcp.resource("inventory://{inventory_id}/name")
def get_inventory_name_from_inventory_id(inventory_id: str) -> str:
    """
    Returns the name from inventory id
    Args:
        inventory_id: the ID of the inventory item
    """
    return inventory_id_to_name.get(inventory_id, "Unknown")

if __name__ == "__main__":
    mcp.run()