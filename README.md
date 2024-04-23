# Simple HTTP POST Logger

This Python script sets up a basic HTTP server that listens for POST requests on a specified port and outputs the contents of the requests to the console. It's useful for debugging or development purposes where capturing incoming POST data is needed.

## Features

- Listens on a configurable HTTP port.
- Handles POST requests and prints their body directly to the console.

## Prerequisites

Before you run the server, make sure you have Python installed on your system. This script has been tested with Python 3.7 and above.

## Installation

### Clone the Repository

```bash
git clone https://github.com/arsaleh/Edge-logging-endpoint.git
cd Edge-logging-endpoint
```

### Install Dependencies

This script uses the `Flask` library to create the HTTP server. You can install it using pip:

```bash
pip install flask
```

## Usage

To start the server, run the script from your terminal:

```bash
python server.py
```

By default, the server will listen on port 8080. You can access the server at:

```
http://localhost:8080/
```

To test the logging of POST requests, you can use `curl` or any other tool to send a POST request:

```bash
curl -X POST http://localhost:8080/ -d "Hello, world!"
```

The server will output the data received in the POST request to the console.

## Configuration

If you need to change the default port or add additional routes, you can modify the `server.py` file. Here is a quick guide to make a common adjustment:

### Changing the Port

Open `server.py` and find the line:

```python
app.run(host='0.0.0.0', port=8080)
```

Change `8080` to your preferred port number.

## Contributing

Contributions to this project are welcome! Just fork the repo, make your changes, and submit a pull request.

## License

This project is released under the MIT License. See the `LICENSE` file for more details.

## Support

If you encounter any issues or have any questions about using the server, please file an issue on the GitHub repository issue tracker.
