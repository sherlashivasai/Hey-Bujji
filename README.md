# Hey-Bujji
This is an AI agent "Bujji" .which works as an personal assistant to his master.and when a unknown user interacts with it provides insights on behalf of his master..
# Bujji

Bujji is an AI-powered project built using CrewAI framework, designed to create and manage intelligent agent crews for various tasks.

## Overview

Bujji is a Python-based project that leverages the CrewAI framework to create and orchestrate AI agents. The project is structured to provide a flexible and extensible platform for building AI-powered solutions.

## Features

- Built on CrewAI framework
- Modular architecture with separate tools and configuration
- Command-line interface for easy interaction
- Support for training and testing agents
- Replay functionality for reviewing agent interactions

## Functionality

Bujji is designed as an intelligent portfolio description agent with the following key capabilities:

### Core Features

1. **Portfolio Analysis**
   - Analyzes and processes portfolio information from multiple sources
   - Extracts relevant information from PDF documents
   - Integrates data from web sources (LinkedIn, GitHub)

2. **Intelligent Response Generation**
   - Uses the Mistral 7B model for natural language processing
   - Generates personalized and professional descriptions
   - Provides concise and relevant information based on user queries

3. **Knowledge Integration**
   - Processes multiple knowledge sources:
     - PDF documents (resumes, research papers)
     - Web content (professional profiles)
     - Custom knowledge bases

4. **Interactive Capabilities**
   - Responds to user queries about portfolio information
   - Provides detailed insights based on available data
   - Maintains context-aware conversations

### Technical Capabilities

1. **Agent System**
   - Sequential processing of tasks
   - Customizable agent roles and goals
   - Integration with Ollama for local LLM processing

2. **Training and Testing**
   - Supports iterative training with customizable parameters
   - Provides testing capabilities for agent performance
   - Includes replay functionality for reviewing agent interactions

3. **Knowledge Management**
   - PDF document processing
   - Web content integration
   - Custom knowledge base support

## Requirements

- Python 3.10 or higher (but less than 3.13)
- Dependencies:
  - crewai[tools] >= 0.121.1
  - docling >= 2.36.1

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bujji
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Usage

The project provides several command-line interfaces:

- `bujji`: Main entry point
- `run_crew`: Run the AI crew
- `train`: Train the agents
- `replay`: Review agent interactions
- `test`: Run tests

Example usage:
```bash
bujji run_crew
```

## Project Structure

```
bujji/
├── src/
│   └── bujji/
│       ├── config/     # Configuration files
│       ├── tools/      # Custom tools and utilities
│       ├── crew.py     # Crew implementation
│       └── main.py     # Main entry point
├── tests/             # Test files
├── knowledge/         # Knowledge base
└── Agent_data/       # Agent-related data
```

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Add your license information here]

## Contact

- Author: Shiva sai
- Email: shivasaisherla9@gmail.com
