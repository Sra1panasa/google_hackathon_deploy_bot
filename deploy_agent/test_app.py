"""
Test file for deployment agent functions.
Tests all the main functions used by the deployment automation agent.
"""
import sys
import os

# Add parent directory to path to import agent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent import ask_cloud_platform, confirm_deployment

def test_ask_cloud_platform_gcp():
    """Test GCP platform selection."""
    result = ask_cloud_platform("gcp")
    assert result["status"] == "success"
    assert result["platform"] == "Google Cloud Platform (GCP)"
    print("✓ test_ask_cloud_platform_gcp PASSED")

def test_ask_cloud_platform_google():
    """Test Google Cloud platform selection."""
    result = ask_cloud_platform("google cloud")
    assert result["status"] == "success"
    assert result["platform"] == "Google Cloud Platform (GCP)"
    print("✓ test_ask_cloud_platform_google PASSED")

def test_ask_cloud_platform_aws():
    """Test AWS platform selection."""
    result = ask_cloud_platform("aws")
    assert result["status"] == "info"
    assert result["platform"] == "AWS"
    assert "coming soon" in result["message"].lower()
    print("✓ test_ask_cloud_platform_aws PASSED")

def test_ask_cloud_platform_azure():
    """Test Azure platform selection."""
    result = ask_cloud_platform("azure")
    assert result["status"] == "info"
    assert result["platform"] == "Azure"
    assert "coming soon" in result["message"].lower()
    print("✓ test_ask_cloud_platform_azure PASSED")

def test_ask_cloud_platform_invalid():
    """Test invalid platform selection."""
    result = ask_cloud_platform("invalid platform")
    assert result["status"] == "error"
    assert "specify a cloud platform" in result["message"].lower()
    print("✓ test_ask_cloud_platform_invalid PASSED")

def test_confirm_deployment_yes():
    """Test deployment confirmation with yes."""
    result = confirm_deployment("yes")
    assert result["status"] == "confirmed"
    assert "deployment" in result["message"].lower()
    print("✓ test_confirm_deployment_yes PASSED")

def test_confirm_deployment_y():
    """Test deployment confirmation with y."""
    result = confirm_deployment("y")
    assert result["status"] == "confirmed"
    print("✓ test_confirm_deployment_y PASSED")

def test_confirm_deployment_proceed():
    """Test deployment confirmation with proceed."""
    result = confirm_deployment("proceed")
    assert result["status"] == "confirmed"
    print("✓ test_confirm_deployment_proceed PASSED")

def test_confirm_deployment_no():
    """Test deployment cancellation."""
    result = confirm_deployment("no")
    assert result["status"] == "cancelled"
    assert "cancelled" in result["message"].lower()
    print("✓ test_confirm_deployment_no PASSED")

def run_all_tests():
    """Run all test functions."""
    tests = [
        test_ask_cloud_platform_gcp,
        test_ask_cloud_platform_google,
        test_ask_cloud_platform_aws,
        test_ask_cloud_platform_azure,
        test_ask_cloud_platform_invalid,
        test_confirm_deployment_yes,
        test_confirm_deployment_y,
        test_confirm_deployment_proceed,
        test_confirm_deployment_no,
    ]
    
    print("Running deployment agent tests...\n")
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} ERROR: {e}")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Test Results: {passed} passed, {failed} failed")
    print(f"{'='*50}")
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
