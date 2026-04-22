"""
Test script for Legal Document Simplifier Backend
Run this to test API endpoints
"""

import requests
import json
import sys

BASE_URL = "http://localhost:5000"

# Sample legal documents for testing
SAMPLE_DOCUMENTS = {
    'rental_agreement': """RESIDENTIAL LEASE AGREEMENT

This Lease Agreement is entered into on this date between Landlord and Tenant.

RENT PAYMENT: Tenant shall pay monthly rent of $1,500 on the 1st of each month. Late fees of $150 apply if payment is received after the 5th.

SECURITY DEPOSIT: A security deposit of $3,000 is required. Landlord may deduct for damages beyond normal wear and tear.

TERMINATION: Either party must provide 60 days written notice to terminate. Early termination without notice results in forfeiture of deposit.

LIABILITY: Landlord assumes no liability for injuries or property damage to Tenant, regardless of cause.

ENTRY RIGHTS: Landlord may enter premises with 24 hours notice for inspections or repairs.

AUTO-RENEWAL: This lease automatically renews for one-year terms unless 60-day notice given.""",

    'employment_contract': """EMPLOYMENT AGREEMENT

Employee agrees to the following terms:

COMPENSATION: Annual salary of $75,000, payable bi-weekly. No overtime compensation provided.

NON-COMPETE: Employee shall not work for any competitor within 50 miles for 18 months after termination.

CONFIDENTIALITY: All company information is confidential indefinitely. Breach results in liquidated damages of $50,000.

INTELLECTUAL PROPERTY: All work product created belongs exclusively to the Company.

TERMINATION AT WILL: Employment may be terminated by either party at any time without cause or notice.

ARBITRATION: All disputes must be resolved through binding arbitration, not court proceedings.""",

    'tos': """TERMS OF SERVICE

By using this service, you agree to:

DATA COLLECTION: We collect all usage data, browsing history, and personal information. This may be shared with third parties.

LICENSE: You grant us perpetual, worldwide rights to use any content you submit for any purpose.

LIMITATION OF LIABILITY: Our liability is capped at $1.00 regardless of damages.

CHANGES TO TERMS: We may modify these terms anytime without notice. Continued use means acceptance.

TERMINATION: We may terminate your account at any time without explanation or refund."""
}


def test_health_check():
    """Test health check endpoint"""
    print("Testing /api/health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}\n")
        return False


def test_simplify_endpoint(document_type='rental_agreement'):
    """Test document simplification endpoint"""
    print(f"Testing /api/simplify endpoint with {document_type}...")
    
    document_text = SAMPLE_DOCUMENTS.get(document_type, SAMPLE_DOCUMENTS['rental_agreement'])
    
    try:
        payload = {"text": document_text}
        response = requests.post(
            f"{BASE_URL}/api/simplify",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nDocument Analysis Results:")
            print(f"Score: {data.get('score')}/100")
            print(f"Assessment: {data.get('score_label')}")
            print(f"Summary: {data.get('summary')}")
            print(f"Clauses found: {len(data.get('clauses', []))}")
            print(f"Negotiation tips: {len(data.get('negotiation_tips', []))}")
            
            # Print first clause as sample
            if data.get('clauses'):
                clause = data['clauses'][0]
                print(f"\nSample Clause ({clause.get('title')}):")
                print(f"  Risk Level: {clause.get('risk')}")
                print(f"  Plain English: {clause.get('plain')[:100]}...")
            
            print()
            return True
        else:
            print(f"Error: {response.text}\n")
            return False
    
    except Exception as e:
        print(f"Error: {e}\n")
        return False


def test_all_document_types():
    """Test with all sample document types"""
    print("=" * 60)
    print("Testing all document types...")
    print("=" * 60 + "\n")
    
    results = {}
    for doc_type in SAMPLE_DOCUMENTS.keys():
        success = test_simplify_endpoint(doc_type)
        results[doc_type] = success
    
    return results


def run_tests():
    """Run all tests"""
    print("=" * 60)
    print("Legal Document Simplifier - Backend Test Suite")
    print("=" * 60 + "\n")
    
    print(f"Testing backend at: {BASE_URL}\n")
    
    # Test 1: Health check
    health_ok = test_health_check()
    
    if not health_ok:
        print("Backend is not running. Start with: python app.py")
        sys.exit(1)
    
    # Test 2: Single endpoint
    print("Testing single endpoint...")
    test_ok = test_simplify_endpoint('rental_agreement')
    
    if not test_ok:
        print("API test failed. Check backend logs.")
        sys.exit(1)
    
    # Test 3: All document types
    print("Testing all document types...")
    results = test_all_document_types()
    
    # Summary
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    print(f"Passed: {passed}/{total}")
    for doc_type, success in results.items():
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {status}: {doc_type}")


if __name__ == '__main__':
    try:
        run_tests()
    except KeyboardInterrupt:
        print("\n\nTests interrupted.")
    except Exception as e:
        print(f"\nFatal error: {e}")
        sys.exit(1)
