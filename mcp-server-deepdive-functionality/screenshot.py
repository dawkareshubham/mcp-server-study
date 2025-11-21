from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image

import pyautogui
import tempfile
import os

mcp = FastMCP("Screenshot Demo")

@mcp.tool()
def capture_screenshot() -> Image:
  """
  Captures the current screen and return the image. Use this tool whenever the user request a screenshot of their activity.
  """

  # Create a temporary file for the screenshot
  with tempfile.NamedTemporaryFile(suffix=".jpeg", delete=False) as temp_file:
    temp_path = temp_file.name

  try:
    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(temp_path, format="JPEG", quality=60, optimize=True)
    return Image(temp_path, format="jpeg")
  except Exception as e:
    # Clean up the temp file if there's an error
    if os.path.exists(temp_path):
      os.unlink(temp_path)
    raise e

if __name__ == "__main__":
    mcp.run()