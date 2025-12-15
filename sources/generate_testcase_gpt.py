from dotenv import load_dotenv
load_dotenv()

#!/usr/bin/env python3
import os
import argparse
import sys
import json
import time
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
from openai import OpenAI
import google.generativeai as genai

api_key_gem = os.getenv("GEMINI_API_KEY")
api_key_gpt = os.getenv("OPENAI_API_KEY")
client_gpt = OpenAI(api_key=api_key_gpt)
# client_gem = OpenAI(api_key=api_key_gem)

def get_prompt(complete_prompt:str, canonical_solution:str) -> str:
    prompt = f'''

           You are a python software testing programmer. 
           Using Python standard unittest format, create 5 test cases as a complete test suite for the following provided prompt. 
           ___________________________________________
           STRICT RULES:
           Do not create the solution function of the prompt in any way. DO NOT LOOK AT THE PROVIDED CANONICAL_SOLUTION GIVEN. CREATE THE TEST SUITE ONLY LOOKING AT THE COMPLETE_PROMPT. 
           ___________________________________________
           More instructions:
           DO NOT CREATE the python markdown (```python...```) for codes at the start and end of your response. Include all appropriate libraries as said in the prompt. Also arrange the entire test suite (with the given below prompt) such that it can be executed. DO NOT TOUCH OR MODIFY THE PROVIDED BELOW PROMPT.
           ___________________________________________
           Here is your prompt:
           {complete_prompt}
           {canonical_solution}
       '''

    return prompt


def extract_code_from_response(response_text):
    """
    Extract Python code from GPT response, handling markdown code blocks.
    """
    # Check for markdown code blocks
    if "```python" in response_text:
        # Extract content between ```python and ```
        pattern = r"```python\n(.*?)\n```"
        match = re.search(pattern, response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
    
    elif "```" in response_text:
        # Extract content between ``` and ``` (any language)
        pattern = r"```\n(.*?)\n```"
        match = re.search(pattern, response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
    
    # If no code blocks found, return the whole response
    return response_text.strip()

def call_gpt():
    
    # Paths to your directories
    prompt_dir = "data/prompt"
    solution_dir = "data/cano_soln"
    output_dir = "data/generated_tests"
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all files from both directories
    prompt_files = sorted([f for f in os.listdir(prompt_dir) if os.path.isfile(os.path.join(prompt_dir, f))])
    solution_files = sorted([f for f in os.listdir(solution_dir) if os.path.isfile(os.path.join(solution_dir, f))])
    
    # Process in parallel (assuming same number and order of files)
    min_files = min(len(prompt_files), len(solution_files))
    
    for i in range(min_files):
        # i = 1
        try:
            # Read prompt
            prompt_path = os.path.join(prompt_dir, prompt_files[i])
            with open(prompt_path, 'r', encoding='utf-8') as f:
                prompt_content = f.read()
            
            # Read solution
            solution_path = os.path.join(solution_dir, solution_files[i])
            with open(solution_path, 'r', encoding='utf-8') as f:
                canonical_solution = f.read()
            
            # Call GPT
            response = client_gpt.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": get_prompt(prompt_content, canonical_solution)}]
            )
            
            # Extract and save test
            generated_test = response.choices[0].message.content
            generated_test = extract_code_from_response(generated_test)
            
            output_filename = f"generated_test_{i:04d}.py"
            output_path = os.path.join(output_dir, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(generated_test)
            
            print(f"Saved: {output_filename} (from {prompt_files[i]} and {solution_files[i]})")
            
        except Exception as e:
            print(f"Error processing file {i+1}: {str(e)}")
            continue
        
        # print ("loop will break. works only for the first case for now.")
        # break
    return 



def main():
    call_gpt()
    # call_gem()


if __name__ == "__main__":
    main()