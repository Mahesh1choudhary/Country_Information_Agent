# Country Information AI Agent

A FastAPI-based AI agent that provides country information using natural language queries. The agent leverages LangGraph to process user queries, identify relevant countries and data fields, fetch data from the REST Countries API, and return filtered results.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mahesh1choudhary/Country_Information_Agent.git
cd "Country Information AI Agent"
```

2. Install dependencies:
```bash
pip3 install -r app/requirements.txt
```

## Usage

### Live Demo

The service is deployed on Render: [https://country-information-agent.onrender.com](https://country-information-agent.onrender.com)

**Note**: The first query may take up to 1 minute due to the free tier's cold start.

### Running Locally

Start the FastAPI server:
```bash
python app/main.py
```

The server will run on `http://0.0.0.0:8000`.

### API Usage

Send a POST request to `/query` with a JSON body containing the query:

```bash
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"query": "What is the capital and population of France?"}'
```

For the live demo, replace the URL with `https://country-information-agent.onrender.com/query`.

#### Example Response
```json
[
  {
    "country_name": "French Republic",
    "capital": ["Paris"],
    "population": 67391582
  }
]
```

### Query Examples

- "What is the capital of Germany?"
- "Tell me about the population and languages of Japan"
- "What are the timezones in Brazil?"
- "Give me the area and region of Australia"

## Project Structure

```
Country Information AI Agent/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── requirements.txt        # Python dependencies
│   ├── agent/
│   │   ├── graph.py           # LangGraph workflow definition
│   │   ├── nodes.py           # Workflow nodes (intent, retrieval, synthesis)
│   │   └── state.py           # Agent state definitions
│   ├── commons/
│   │   ├── query_model.py     # Pydantic models
│   │   └── service_logger.py  # Logging configuration
│   ├── config/
│   │   └── config_constants.py # API configuration
│   ├── controller/
│   │   ├── query_controller.py # FastAPI routes
│   │   └── dependency/
│   │       └── dependency_functions.py # Dependency injection
│   ├── data/
│   │   ├── country_names.json  # Country name mappings
│   │   ├── field_names.json    # Field synonym mappings
│   │   └── data_loader.py      # Data loading utilities
│   ├── service/
│   │   └── query_service.py    # Business logic service
│   └── tools/
│       ├── country_api.py      # REST Countries API client
│       └── related_fields.py   # Field and country matching logic
├── scripts/
│   └── all_countries_script.py  # Script to generate country data
└── README.md
```

## Dependencies

- **FastAPI**: Web framework for building APIs
- **Uvicorn**: ASGI server
- **LangGraph**: Framework for building AI agents
- **httpx**: Asynchronous HTTP client
- **Tenacity**: Retry library for resilient API calls
- **Pydantic**: Data validation and serialization

## Data Sources

- **REST Countries API** (`https://restcountries.com/v3.1/`): Provides comprehensive country information including demographics, geography, and administrative data.

## Development

### Data Generation

To update the country names mapping, run the data generation script:

```bash
python scripts/all_countries_script.py > app/data/country_names.json
```

### Logging

The application uses structured logging. Logs are output to the console with different levels (INFO, DEBUG, ERROR).

## API Reference

### POST /query

Processes a natural language query about countries.

**Request Body:**
```json
{
  "query": "string"
}
```

**Response:**
```json
[
  {
    "country_name": "string",
    "field1": "value1",
    "field2": "value2",
    ...
  }
]
```

**Status Codes:**
- 200: Success
- 500: Internal server error
