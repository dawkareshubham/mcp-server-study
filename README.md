# MCP Server Study Projects

A collection of Model Context Protocol (MCP) projects demonstrating various MCP server implementations and client interactions.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Projects Overview](#projects-overview)
- [Running the Projects](#running-the-projects)
- [Project Details](#project-details)

## 🔧 Prerequisites

Before running any of these projects, ensure you have the following installed:

- **Python 3.11+** (Python 3.10+ for mcp-client)
- **uv** (Python package installer and environment manager)
- **Git** (for cloning the repository)

### Installing uv

#### Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/dawkareshubham/mcp-server-study.git
cd mcp-server-study
```

### Quick Setup for All Projects

Each project uses `uv` for dependency management. You can set up individual projects as needed:

```bash
# Navigate to a specific project directory
cd <project-name>

# Install dependencies
uv sync

# Activate virtual environment (optional)
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

## 📚 Projects Overview

| Project | Description | Python Version | Key Dependencies |
|---------|-------------|----------------|------------------|
| **client** | Basic MCP client implementation | 3.11+ | mcp[cli] |
| **helloworld** | Simple hello world MCP server | 3.11+ | mcp[cli] |
| **mcp-client** | Advanced MCP client with OpenAI integration | 3.10+ | mcp[cli], openai, dotenv |
| **mcp-primitives-and-inputs** | MCP primitives and input handling examples | 3.11+ | mcp[cli] |
| **mcp-server-deepdive-deployment** | Deployable MCP server package | 3.11+ | mcp[cli] |
| **mcp-server-deepdive-functionality** | MCP server with extended functionality | 3.11+ | mcp[cli], pillow, pyautogui, requests |
| **mcp-server-http-streamable-updated** | HTTP streamable MCP server | 3.11+ | mcp[cli] |
| **mcp-build-chess** | Chess.com API MCP server with player stats | 3.10+ | mcp[cli], requests |
| **mcp-build-memory-tracker** | Vector store memory management with OpenAI | 3.10+ | mcp[cli], openai |
| **mcp-build-client-agent-airbnb-memory** | Multi-server MCP client with Airbnb & memory | 3.10+ | mcp[cli], openai, streamlit |

## 🚀 Running the Projects

### 1. client

Basic MCP client example.

```bash
cd client
uv sync
uv run python main.py
```

Alternative:
```bash
cd client
uv run python client.py  # If using client.py
```

### 2. helloworld

Simple hello world MCP server demonstration.

```bash
cd helloworld
uv sync
uv run python main.py
```

### 3. mcp-client

MCP client with OpenAI integration. Requires environment configuration.

```bash
cd mcp-client
uv sync

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the main client
uv run python main.py

# Or run specific clients
uv run python client_simple.py
uv run python client_query.py

# Run the server
uv run python server.py
```

### 4. mcp-primitives-and-inputs

Examples of MCP primitives and input handling.

```bash
cd mcp-primitives-and-inputs
uv sync

# Run main example
uv run python main.py

# Run specific examples
uv run python prompt.py
uv run python resources.py
```

### 5. mcp-server-deepdive-deployment

Deployable MCP server package with proper structure.

```bash
cd mcp-server-deepdive-deployment
uv sync

# Install the package in development mode
uv pip install -e .

# Run the server using the installed command
mcp-server

# Or run directly
uv run python main.py
```

### 6. mcp-server-deepdive-functionality

MCP server with advanced functionality including screenshot capabilities, crypto operations, and file handling.

```bash
cd mcp-server-deepdive-functionality
uv sync

# Run main server
uv run python main.py

# Run specific functionality
uv run python crypto.py
uv run python screenshot.py
uv run python local.py
uv run python other_inputs.py
```

### 7. mcp-server-http-streamable-updated

HTTP streamable MCP server implementation.

```bash
cd mcp-server-http-streamable-updated
uv sync

# Run the server
uv run python server.py

# Or run main
uv run python main.py
```

### 8. mcp-build-chess

MCP server that provides access to Chess.com player data through the public API.

```bash
cd mcp-build-chess
uv sync

# Install the package in development mode
uv pip install -e .

# Run using the installed command
chess

# Or run with PYTHONPATH
$env:PYTHONPATH="src"  # Windows PowerShell
uv run python -m chess.server
```

**Key Features:**
- Get Chess.com player profiles
- Retrieve player statistics (ratings, wins, losses)
- FastMCP integration
- See detailed README in `mcp-build-chess/` folder

### 9. mcp-build-memory-tracker

MCP server with OpenAI vector store integration for memory management.

```bash
cd mcp-build-memory-tracker
uv sync

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the server
uv run python server.py
```

**Key Features:**
- Save memories to OpenAI vector store
- Search memories using semantic search
- Persistent memory storage
- OpenAI integration

### 10. mcp-build-client-agent-airbnb-memory

Advanced MCP client that connects to multiple MCP servers simultaneously (Airbnb API + Memory server).

```bash
cd mcp-build-client-agent-airbnb-memory
uv sync

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the client
uv run python client.py

# Or run the Streamlit UI
uv run streamlit run chat_ui.py
```

**Key Features:**
- Multi-server MCP client architecture
- Integrates Airbnb search with memory storage
- Streamlit-based chat interface
- OpenAI function calling
- Demonstrates advanced MCP patterns

## 📖 Project Details

### client
Basic MCP client implementation demonstrating fundamental client-side operations.

**Key Files:**
- `main.py` - Main entry point
- `client.py` - Client implementation
- `weather.py` - Weather-related functionality

### helloworld
Minimalist MCP server example, perfect for understanding the basics.

**Key Files:**
- `main.py` - Server entry point
- `weather.py` - Weather service example

### mcp-client
Advanced client implementation with OpenAI integration for AI-powered MCP interactions.

**Key Files:**
- `main.py` - Main client application
- `client_simple.py` - Simple client example
- `client_query.py` - Query-based client
- `server.py` - Local server for testing
- `.env` - Environment configuration (create this)

**Environment Variables:**
```
OPENAI_API_KEY=your_openai_api_key
```

### mcp-primitives-and-inputs
Demonstrates MCP primitives, prompts, and resource handling.

**Key Files:**
- `main.py` - Main examples
- `prompt.py` - Prompt handling
- `resources.py` - Resource management

### mcp-server-deepdive-deployment
Production-ready MCP server with proper package structure for deployment.

**Structure:**
```
mcp-server-deepdive-deployment/
├── src/
│   └── mcpserver/
│       ├── __init__.py
│       ├── __main__.py
│       └── deployment.py
├── main.py
└── pyproject.toml
```

**Key Files:**
- `src/mcpserver/deployment.py` - Deployment logic
- `src/mcpserver/__main__.py` - Package entry point
- `main.py` - Alternative entry point

### mcp-server-deepdive-functionality
Feature-rich MCP server with multiple capabilities.

**Key Files:**
- `main.py` - Main server
- `crypto.py` - Cryptographic operations
- `screenshot.py` - Screenshot functionality (requires display)
- `local.py` - Local file operations
- `other_inputs.py` - Various input handling
- `notes.txt` / `log.txt` - Data files

**Dependencies:**
- `pillow` - Image processing
- `pyautogui` - Screenshot capabilities
- `pyscreeze` - Screen capture
- `requests` - HTTP requests

### mcp-server-http-streamable-updated
Modern HTTP-based MCP server with streaming support.

**Key Files:**
- `server.py` - HTTP server implementation
- `main.py` - Server entry point

### mcp-build-chess
Chess.com API integration server that retrieves player profiles and statistics.

**Key Files:**
- `src/chess/server.py` - Main MCP server with FastMCP
- `src/chess/chess_api.py` - Chess.com API client
- `README.md` - Comprehensive documentation

**Tools:**
- `get_chess_player_profile` - Get player profile info
- `get_chess_player_stats` - Get detailed game statistics

**API Integration:**
Uses Chess.com Public API (no authentication required)

### mcp-build-memory-tracker
Memory management server using OpenAI vector stores for semantic search and storage.

**Key Files:**
- `server.py` - FastMCP server with vector store integration
- `main.py` - Alternative entry point
- `.env` - OpenAI API key configuration

**Tools:**
- `search_memory` - Search memories using semantic similarity
- `save_memory` - Save new memories to vector store

**Dependencies:**
- OpenAI API for vector store operations
- Requires `OPENAI_API_KEY` environment variable

### mcp-build-client-agent-airbnb-memory
Multi-server MCP client demonstrating advanced patterns with Airbnb search and memory integration.

**Key Files:**
- `client.py` - Multi-server MCP client implementation
- `chat_ui.py` - Streamlit-based chat interface
- `main.py` - Alternative client runner
- `.env` - OpenAI API key configuration

**Features:**
- Connects to multiple MCP servers simultaneously
- Integrates Airbnb listings search (via @openbnb/mcp-server-airbnb)
- Memory storage and retrieval (via memory tracker server)
- OpenAI function calling for intelligent tool selection
- Interactive Streamlit UI

**Architecture:**
- Client connects to two servers: Airbnb API server + Memory tracker server
- Combines tools from both servers
- Uses OpenAI for natural language understanding and tool invocation

**Environment Variables:**
```
OPENAI_API_KEY=your_openai_api_key
```

## 🔍 Common Commands

### Install Dependencies
```bash
uv sync
```

### Run a Python File
```bash
uv run python <filename>.py
```

### Activate Virtual Environment
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### Update Dependencies
```bash
uv sync --upgrade
```

### Check Python Version
```bash
python --version
```

## 🐛 Troubleshooting

### Issue: "uv: command not found"
**Solution:** Install uv using the installation commands in the Prerequisites section.

### Issue: Python version mismatch
**Solution:** Ensure you have Python 3.11+ installed. Check with `python --version`.

### Issue: OpenAI API errors in mcp-client
**Solution:** Ensure your `.env` file contains a valid `OPENAI_API_KEY`.

### Issue: Screenshot functionality not working
**Solution:** Ensure you have a display available. On headless systems, screenshot features may not work.

### Issue: Module not found errors
**Solution:** Run `uv sync` in the project directory to install all dependencies.

## 📝 Notes

- Each project is self-contained with its own dependencies
- Use `uv` for better dependency management and faster installations
- Some projects may require additional environment setup (e.g., API keys)
- Check individual project README files for specific configuration details

## 🤝 Contributing

Feel free to explore, modify, and learn from these projects. Each demonstrates different aspects of the Model Context Protocol.

## 📄 License

These are study projects for learning MCP implementations.

## 👤 Author

**Shubham Dawkare**
- GitHub: [@dawkareshubham](https://github.com/dawkareshubham)
- Email: dawkare.shubham@gmail.com
