# HTTP File Server Automation

This Python program automates the client-side interaction with an HTTP server application on a PC. It is specifically designed to work with the "HTTP File Server" Android app, which can be found on the Google Play Store: [HTTP File Server on Google Play Store](https://play.google.com/store/apps/details?id=slowscript.httpfileserver).

## Prerequisites

- Python 3.x installed on your PC
- `requests` library installed (can be installed via `pip install requests`)

## Setup

1. Clone this repository into your user folder for the best experience.
2. Install the `requests` library if you haven't already: `pip install requests`.

## Usage

1. Make sure the "HTTP File Server" app is installed on your Android device.
2. Launch the app and start the HTTP server.
3. Update the `url` variable in the Python code with the actual URL of the file you want to retrieve from the server. For example: `url = 'http://server-address/filename'`.
4. Run the Python program using `python http_server_automation.py`.
5. The program will send a GET request to the specified URL and attempt to retrieve the file from the server.
6. If the request is successful (status code 200), the file will be downloaded and saved in the same directory as the Python program.

## Enjoy Superfast Share Speed!

## Notes

- Ensure that your PC and Android device are connected to the same network for the program to access the HTTP server.
- Customize the code further based on your specific requirements and the functionality provided by the "HTTP File Server" app or any other server you are working with.

Feel free to reach out if you have any questions or encounter any issues. Enjoy the superfast file sharing experience with HTTP File Server!

