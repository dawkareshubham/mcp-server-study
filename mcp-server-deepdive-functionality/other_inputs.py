from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List
from pathlib import Path


mcp = FastMCP("Other Inputs")

LOG_FILE = Path(__file__).resolve().with_name("log.txt")

class Person(BaseModel):
    first_name: str = Field(..., description="The person's first name")
    last_name: str = Field(..., description="The person's last name")
    years_of_experience: int = Field(..., description="Number of years of experience")
    previous_addresses: List[str] = Field(default_factory=list, description="List of previous addresses")

@mcp.tool()
def add_person_to_member_database(person: Person) -> str:
    """
    Logs the personal details of the given person to the database.
    Args:
        person (Person): An instance of the Person class containing the following personal details:
            - first_name (str): The person's given name.
            - last_name (str): The person's family name.
            - years_of_experience (int): Number of years of experienceh.
            - previous_addresses (List[str]): A list of the person's previous residential addresses.

    Returns:
        str: A confirmation message indicating that the data has been logged.

    """
    
    # Debug: Print the log file path
    print(f"DEBUG: LOG_FILE path is: {LOG_FILE}")
    print(f"DEBUG: LOG_FILE exists: {LOG_FILE.exists()}")
    
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(f"First Name: {person.first_name}\n")
            log_file.write(f"Last Name: {person.last_name}\n")
            log_file.write(f"Years of Experience: {person.years_of_experience}\n")
            log_file.write("Previous Addresses:\n")
            for idx, address in enumerate(person.previous_addresses, 1):
                log_file.write(f"  {idx}. {address}\n")
            log_file.write("\n")
        print(f"DEBUG: Successfully wrote to {LOG_FILE}")
        return "Data has been logged"
    except Exception as e:
        print(f"DEBUG: Error writing to file: {e}")
        return f"Error logging data: {e}"

if __name__ == "__main__":
    mcp.run()

