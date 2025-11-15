"""
Simple test case for the agent - just checking if function returns a string response.
This is a prototype to demonstrate the deployment flow.
"""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from agent import get_current_time


def test_get_current_time_returns_dict():
    """Test that get_current_time returns a dictionary with expected structure."""
    result = get_current_time("London")
    
    # Check if result is a dictionary
    assert isinstance(result, dict), "Function should return a dictionary"
    
    # Check if status field exists and is a string
    assert "status" in result, "Result should have 'status' field"
    assert isinstance(result["status"], str), "Status should be a string"
    
    # Check if city field exists and is a string
    assert "city" in result, "Result should have 'city' field"
    assert isinstance(result["city"], str), "City should be a string"
    
    # Check if time field exists and is a string
    assert "time" in result, "Result should have 'time' field"
    assert isinstance(result["time"], str), "Time should be a string"
    
    print(f"[PASS] Test passed! Result: {result}")


def test_get_current_time_with_different_city():
    """Test with a different city to ensure it works consistently."""
    result = get_current_time("New York")
    
    assert isinstance(result, dict), "Function should return a dictionary"
    assert result["city"] == "New York", "City should match the input"
    assert isinstance(result["time"], str), "Time should be a string"
    
    print(f"[PASS] Test passed! Result: {result}")


if __name__ == "__main__":
    # Run tests directly
    print("Running tests...")
    test_get_current_time_returns_dict()
    test_get_current_time_with_different_city()
    print("\n[SUCCESS] All tests passed successfully!")

