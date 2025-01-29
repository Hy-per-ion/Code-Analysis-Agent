import os
import openai
from langchain_openai import ChatOpenAI
from langchain_community.tools import Tool
from langchain.agents import initialize_agent, AgentType
from utils.file_handler import read_code_from_file
from agents.syntax_checker import syntax_analysis_agent
from agents.code_smell import code_smell_agent
from agents.enhancer import code_enhancer_agent
from utils.logger import log

import os
from langchain_openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it as an environment variable.")

# Initialize GPT-4o Model
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

def process_code(file_path):
    try:
        code = read_code_from_file(file_path)
        if not code:
            log("Invalid Code Format", level="ERROR")
            return "Error: Invalid Code Format"

        # Syntax Checking
        syntax_result = syntax_analysis_agent(code, llm)
        if "ERROR" in syntax_result:
            log("Syntax Issues Found", level="ERROR")
            return syntax_result

        # Code Smell Detection
        smell_result = code_smell_agent(code, llm)
        if "ISSUES FOUND" in smell_result:
            log("Code Smell Issues Detected", level="ERROR")
            return smell_result

        # Code Enhancement
        enhanced_code = code_enhancer_agent(code, llm)
        log("Code Successfully Enhanced", level="INFO")
        return enhanced_code

    except Exception as e:
        log(f"System Error: {str(e)}", level="ERROR")
        return "System Error Occurred"

if __name__ == "__main__":
    file_path = "test_code.py" # input file path
    result = process_code(file_path)
    print(result)