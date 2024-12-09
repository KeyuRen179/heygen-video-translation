# Heygen Video Translation

## Project Overview
This project simulates a video translation backend and provides a client library to interact with it. The backend mimics a translation server with a configurable random delay and returns status updates ("pending", "completed", or "error"). The client library optimizes polling for status updates, demonstrating a customer-centric approach.

## Features
- **Server**: Implements a `/status` API that returns a status of "pending", "completed", or "error" based on configurable delays.
- **Client Library**: Includes a polling mechanism with exponential backoff to reduce unnecessary calls and avoid delays.
- **Integration Test**: Demonstrates the interaction between the server and client, with detailed logs.
- **Customizability**: Configurable parameters for polling behavior, server delay, and error probability.

## Getting Started

### Prerequisites
- Python 3.8+
- Pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/heygen-video-translation.git
   cd heygen-video-translation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Start the Server
The server simulates the video translation backend:
```bash
python server.py
```
The server will start on `http://localhost:5000` by default.

### 2. Use the Client Library
The client library polls the server to get the translation status:
```python
from translation_client import TranslationClient

client = TranslationClient("http://localhost:5000")
status = client.get_status()
print("Translation Status:", status)
```

### 3. Run Integration Test
Run the integration test to demonstrate server and client interaction:
```bash
python integration_test.py
```

## Configuration
### Server Configuration
You can modify the server's behavior by editing `server.py`:
- `DELAY`: The time in seconds before the server returns "completed".
- `ERROR_PROBABILITY`: The probability of returning "error" after the delay.

### Client Configuration
The client library supports customizable parameters:
- `max_retries`: Maximum number of polling attempts.
- `initial_interval`: Initial interval (in seconds) between polling attempts.
- `max_interval`: Maximum interval (in seconds) between polling attempts.

Example:
```python
client = TranslationClient(
    server_url="http://localhost:5000",
    max_retries=15,
    initial_interval=2,
    max_interval=10
)
```

## Project Structure
```
.
├── server.py               # Server implementation
├── translation_client.py   # Client library implementation
├── integration_test.py     # Integration test
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
└── .gitignore              # Ignored files
```

## Testing
The integration test demonstrates the client polling the server until it gets a "completed" or "error" response. Logs are printed to the console for clarity.

Run the integration test:
```bash
python integration_test.py
```

Expected Output Example:
```
Polling status: pending
Polling status: pending
Polling status: completed
Final Translation Status: completed
```

## Future Enhancements
- Add support for multiple language translations.
- Integrate with an actual video processing backend.
- Add a CLI or GUI for ease of use.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request if you'd like to enhance the project.


