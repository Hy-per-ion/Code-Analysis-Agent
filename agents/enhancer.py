def code_enhancer_agent(code, llm):
    prompt = f"Improve the following code for efficiency and readability:\n{code}"
    response = llm.invoke(prompt)
    return response