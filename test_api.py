import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

#!/usr/bin/env python3
"""
Multi-Model Testing Script for Gemini 2.5 Pro and GPT-5.2
Supports both models through a unified interface
"""

# import os
import argparse
import sys
import json
import time
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

# Try to import required packages with error handling
#!/usr/bin/env python3
"""
Simple API Test Script for Gemini and OpenAI
"""

import os
import sys

def test_gemini():
    """Test Gemini API with gemini-1.5-flash"""
    try:
        import google.generativeai as genai
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ GEMINI_API_KEY not found in environment")
            return False
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-pro')
        
        response = model.generate_content("Say 'Hello' in a creative way")
        
        print("✅ Gemini API Test PASSED")
        print(f"Response: {response.text[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ Gemini API Test FAILED: {e}")
        return False

def test_openai():
    """Test OpenAI API with gpt-4o"""
    try:
        from openai import OpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("❌ OPENAI_API_KEY not found in environment")
            return False
        
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Say 'Hello' in a creative way"}],
            max_tokens=50
        )
        
        print("✅ OpenAI API Test PASSED")
        print(f"Response: {response.choices[0].message.content[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API Test FAILED: {e}")
        return False

def check_env(model):
    """Check if environment variables are set for the specified model"""
    print("🔍 Checking environment variables...")
    
    gemini_key = os.getenv("GEMINI_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if model.lower() in ['gemini', 'g']:
        if gemini_key:
            print(f"✅ GEMINI_API_KEY: {gemini_key[:10]}...{gemini_key[-5:]}")
            return True, gemini_key
        else:
            print("❌ GEMINI_API_KEY: NOT SET")
            return False, None
    
    elif model.lower() in ['gpt', 'openai', 'o']:
        if openai_key:
            print(f"✅ OPENAI_API_KEY: {openai_key[:10]}...{openai_key[-5:]}")
            return True, openai_key
        else:
            print("❌ OPENAI_API_KEY: NOT SET")
            return False, None
    
    else:
        print(f"❌ Unknown model: {model}")
        print("   Please specify 'gemini' or 'gpt'")
        return False, None

def main():
    """Main function"""
    print("=" * 50)
    print("API Connection Tester")
    print("=" * 50)
    
    # Get model from command line or user input
    if len(sys.argv) > 1:
        model = sys.argv[1]
    else:
        model = input("Enter model to test (gemini/gpt): ").strip()
    
    # Validate model choice
    valid_models = ['gemini', 'g', 'gpt', 'openai', 'o']
    if model.lower() not in valid_models:
        print(f"❌ Invalid model: {model}")
        print("   Available options: gemini, gpt")
        sys.exit(1)
    
    # Check environment for the selected model
    has_key, _ = check_env(model)
    
    if not has_key:
        if model.lower() in ['gemini', 'g']:
            print("\n💡 Set your Gemini API key:")
            print("   export GEMINI_API_KEY='your-key-here'")
        else:
            print("\n💡 Set your OpenAI API key:")
            print("   export OPENAI_API_KEY='your-key-here'")
        sys.exit(1)
    
    # Test the selected model
    print(f"\n🧪 Testing {model.upper()} API...")
    
    if model.lower() in ['gemini', 'g']:
        success = test_gemini()
        model_name = "Gemini"
    else:
        success = test_openai()
        model_name = "OpenAI GPT-4o"
    
    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"Model: {model_name}")
    print(f"Result: {status}")

if __name__ == "__main__":
    main()