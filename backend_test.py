import requests
import sys
import json
from datetime import datetime

class SparkAIHubAPITester:
    def __init__(self, base_url="https://ai-spark-center.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0
        self.test_results = []

    def run_test(self, name, method, endpoint, expected_status, data=None, headers=None):
        """Run a single API test"""
        url = f"{self.api_url}/{endpoint}"
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)

            success = response.status_code == expected_status
            
            result = {
                "test_name": name,
                "method": method,
                "endpoint": endpoint,
                "expected_status": expected_status,
                "actual_status": response.status_code,
                "success": success,
                "response_data": None,
                "error": None
            }

            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    result["response_data"] = response.json()
                except:
                    result["response_data"] = response.text
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    result["error"] = response.json()
                except:
                    result["error"] = response.text

            self.test_results.append(result)
            return success, response

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            result = {
                "test_name": name,
                "method": method,
                "endpoint": endpoint,
                "expected_status": expected_status,
                "actual_status": None,
                "success": False,
                "response_data": None,
                "error": str(e)
            }
            self.test_results.append(result)
            return False, None

    def test_api_root(self):
        """Test API root endpoint"""
        return self.run_test(
            "API Root",
            "GET",
            "",
            200
        )

    def test_contact_form_submission(self):
        """Test contact form submission"""
        contact_data = {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "+971 50 123 4567",
            "subject": "General Inquiry",
            "message": "This is a test message from the contact form."
        }
        
        success, response = self.run_test(
            "Contact Form Submission",
            "POST",
            "contact",
            200,
            data=contact_data
        )
        
        if success and response:
            try:
                response_data = response.json()
                if response_data.get('success') and response_data.get('submission_id'):
                    print(f"   ✅ Contact submission successful with ID: {response_data.get('submission_id')}")
                    return True, response_data.get('submission_id')
                else:
                    print(f"   ❌ Contact submission response missing required fields")
                    return False, None
            except:
                print(f"   ❌ Contact submission response not valid JSON")
                return False, None
        
        return False, None

    def test_onboarding_form_submission(self):
        """Test onboarding form submission"""
        onboarding_data = {
            "fullName": "John Doe",
            "email": "john@example.com",
            "phone": "+971 50 987 6543",
            "organization": "Test Company LLC",
            "interest": "machine-learning",
            "message": "Interested in exploring ML solutions for our business."
        }
        
        success, response = self.run_test(
            "Onboarding Form Submission",
            "POST",
            "onboarding",
            200,
            data=onboarding_data
        )
        
        if success and response:
            try:
                response_data = response.json()
                if response_data.get('success') and response_data.get('application_id'):
                    print(f"   ✅ Onboarding submission successful with ID: {response_data.get('application_id')}")
                    return True, response_data.get('application_id')
                else:
                    print(f"   ❌ Onboarding submission response missing required fields")
                    return False, None
            except:
                print(f"   ❌ Onboarding submission response not valid JSON")
                return False, None
        
        return False, None

    def test_contact_form_validation(self):
        """Test contact form validation with missing required fields"""
        invalid_data = {
            "name": "",  # Missing required field
            "email": "invalid-email",  # Invalid email
            "subject": "",  # Missing required field
            "message": ""  # Missing required field
        }
        
        return self.run_test(
            "Contact Form Validation (Invalid Data)",
            "POST",
            "contact",
            422,  # Expecting validation error
            data=invalid_data
        )

    def test_onboarding_form_validation(self):
        """Test onboarding form validation with missing required fields"""
        invalid_data = {
            "fullName": "",  # Missing required field
            "email": "invalid-email",  # Invalid email
            "phone": "",  # Missing required field
            "interest": ""  # Missing required field
        }
        
        return self.run_test(
            "Onboarding Form Validation (Invalid Data)",
            "POST",
            "onboarding",
            422,  # Expecting validation error
            data=invalid_data
        )

    def print_summary(self):
        """Print test summary"""
        print(f"\n" + "="*60)
        print(f"📊 SPARK AI Hub API Test Summary")
        print(f"="*60)
        print(f"Tests Run: {self.tests_run}")
        print(f"Tests Passed: {self.tests_passed}")
        print(f"Tests Failed: {self.tests_run - self.tests_passed}")
        print(f"Success Rate: {(self.tests_passed/self.tests_run)*100:.1f}%")
        
        if self.tests_passed < self.tests_run:
            print(f"\n❌ Failed Tests:")
            for result in self.test_results:
                if not result["success"]:
                    print(f"   - {result['test_name']}: {result.get('error', 'Status code mismatch')}")
        
        return self.tests_passed == self.tests_run

def main():
    print("🚀 Starting SPARK AI Hub API Tests...")
    print("="*60)
    
    # Initialize tester
    tester = SparkAIHubAPITester()
    
    # Run all tests
    print("\n1. Testing API Root Endpoint...")
    tester.test_api_root()
    
    print("\n2. Testing Contact Form Submission...")
    contact_success, contact_id = tester.test_contact_form_submission()
    
    print("\n3. Testing Onboarding Form Submission...")
    onboarding_success, onboarding_id = tester.test_onboarding_form_submission()
    
    print("\n4. Testing Contact Form Validation...")
    tester.test_contact_form_validation()
    
    print("\n5. Testing Onboarding Form Validation...")
    tester.test_onboarding_form_validation()
    
    # Print summary
    all_passed = tester.print_summary()
    
    # Save detailed results
    with open('/app/backend_test_results.json', 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "tests_run": tester.tests_run,
                "tests_passed": tester.tests_passed,
                "success_rate": (tester.tests_passed/tester.tests_run)*100
            },
            "test_results": tester.test_results
        }, f, indent=2)
    
    print(f"\n📄 Detailed results saved to: /app/backend_test_results.json")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())