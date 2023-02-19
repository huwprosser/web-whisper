# Web Whisper

## Description
This project combines a few really awesome open source projects to bring state-of-the-art speech recognition to the web. It uses the collects and qualifies the audio on the client-side using Voice Activity Detection [This is my new favourite package!](https://github.com/ricky0123/vad) and then sends it to the Python/Flask server for processing with [OpenAI Whisper](https://github.com/openai/whisper) for processing.

I wanted this project to remain two main files, one for front-end web code WITHOUT a framework and one for back-end Python code WITHOUT bloat. I think this is a good way to keep the code simple and easy to understand.

PRs are welcome!

## Installation

1. Clone the repo

2. Install the dependencies
   `pip install -r requirements.txt`

3. Run the server
   `python server.py`
