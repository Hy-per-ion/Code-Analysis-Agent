def syntax_analysis_agent(code, llm):
    prompt = f"Check the following code for syntax errors:\n{code}"
    response = llm.invoke(prompt)
    return response
