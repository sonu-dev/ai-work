import os
from pathlib import Path
from langchain_core.tools import tool

WORKSPACE = Path("output")
WORKSPACE.mkdir(exist_ok=True)


@tool
def save_code_tool(code: str, filename: str = "output.py") -> str:
    
    """
    MANDATORY tool for saving ALL generated code.
    Use this tool whenever the user asks to:
    - generate code
    - create a program
    - write python code
    - build an API
    - create any file

    The input must be the COMPLETE raw code only.
    Do not include markdown formatting.
    """  
    print("TOOL CALLED")  # debug
    
    safe_path = WORKSPACE / Path(filename).name
    
    print(f"Saving code to {safe_path}...")  # debug
    
    with open(safe_path, "w", encoding="utf-8") as f:
        f.write(code)
        
    return f"Saved to {safe_path}"