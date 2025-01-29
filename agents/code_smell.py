def code_smell_agent(code, llm):
    prompt = f"Analyze the following code for code smells and inefficiencies:\n{code}"
    response = llm.invoke(prompt)
    return response