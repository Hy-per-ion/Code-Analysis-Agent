## Requirements

Make sure you have the following dependencies installed:

- openai
- langchain
- langchain_openai
- langchain_community

You can install the required dependencies using the following command:

```sh
pip install -r requirements.txt
```
## Setting the OpenAI API Key
Before running the code, you need to set the OpenAI API key as an environment variable. You can do this using the set command in your terminal:
```sh
set OPENAI_API_KEY="your_openai_api_key"
```
Replace ```your_openai_api_key``` with your actual OpenAI API key.

## Running the code

You can run this script by running the following command:
```sh
python main.py
```
By default, the script processes the ```test_code.py``` file. You can modify the file_path variable in main.py to process a different file.
