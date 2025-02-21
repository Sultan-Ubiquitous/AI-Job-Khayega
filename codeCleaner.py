import re

def clean_code_output(response_text):
    """
    Clean the API response text to extract just the React component code.
    
    Args:
        response_text (str): The raw response text from the API
        
    Returns:
        str: Cleaned React component code ready for use
    """
    # Find the code block between ```jsx and ```
    jsx_pattern = r"```jsx\n(.*?)```"
    match = re.search(jsx_pattern, response_text, re.DOTALL)
    
    if match:
        # Extract the code
        code = match.group(1)
        
        # Remove any trailing whitespace and ensure proper line endings
        code = code.strip()
        
        return code
    else:
        # If no JSX code block is found, try to find any code block
        code_pattern = r"```.*?\n(.*?)```"
        match = re.search(code_pattern, response_text, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        
        return None

def save_code_to_file(code, filename="App.jsx"):
    """
    Save the cleaned code to a file.
    
    Args:
        code (str): The cleaned React component code
        filename (str): The name of the file to save to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(code)

# Example usage
def process_api_response(response_text):
    """
    Process the API response and save the cleaned code to a file.
    
    Args:
        response_text (str): The raw response text from the API
    """
    cleaned_code = clean_code_output(response_text)
    
    if cleaned_code:
        save_code_to_file(cleaned_code)
        print(f"Code has been cleaned and saved to App.jsx")
    else:
        print("No code block found in the response")