
"""
Test cases for Genstore Help Documentation QA.

Each test case includes:
- id: Unique identifier
- name: Human-readable name
- question: The question to ask
- expected_keywords: Keywords that should appear in the answer
- forbidden_keywords: Keywords that should NOT appear (optional)
- doc_reference: Path to the relevant documentation (for verification)
- category: Category for grouping results
- difficulty: easy/medium/hard
"""

from typing import List, Dict


QA_TEST_CASES = [
    # ==================== Definition Questions ====================
    {
        "id": "abandoned-checkout-definition",
        "name": "Abandoned Checkout Definition",
        "question": "What is an abandoned checkout?",
        "expected_keywords": [
            "email address",
            "10 minutes",
            "fails to complete",
            "checkout page"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/orders/abandoned-cart",
        "category": "definition",
        "difficulty": "easy"
    },
    
    # ==================== Process Questions ====================
    {
        "id": "birthday-rewards-setup",
        "name": "Birthday Rewards Setup",
        "question": "How do I set up birthday reward points for customers?",
        "expected_keywords": [
            "loyalty",
            "points",
            "birthday",
            "earn points",
            "add"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/customers/loyalty/points/earnings/birthday",
        "category": "process",
        "difficulty": "medium"
    },
    
    {
        "id": "abandoned-checkout-recover",
        "name": "Recover Abandoned Checkout",
        "question": "How can I recover an abandoned checkout?",
        "expected_keywords": [
            "recovery link",
            "email",
            "marketing automation",
            "complete"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/orders/abandoned-cart",
        "category": "process",
        "difficulty": "medium"
    },
    
    {
        "id": "abandoned-checkout-automation",
        "name": "Abandoned Checkout Automation",
        "question": "How do I set up automatic abandoned checkout recovery emails?",
        "expected_keywords": [
            "marketing",
            "automation",
            "abandoned checkout",
            "template",
            "create"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/orders/abandoned-cart",
        "category": "process",
        "difficulty": "medium"
    },
    
    # ==================== Troubleshooting Questions ====================
    {
        "id": "birthday-not-registered",
        "name": "Birthday Not Registered",
        "question": "What if a customer hasn't registered their birthday in advance for the reward?",
        "expected_keywords": [
            "30 days",
            "manually",
            "register",
            "sign-up"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/customers/loyalty/points/earnings/birthday",
        "category": "troubleshooting",
        "difficulty": "medium"
    },
    
    {
        "id": "birthday-miss-claim",
        "name": "Birthday Claim Period Missed",
        "question": "What happens if a customer misses their birthday reward claim period?",
        "expected_keywords": [
            "cannot claim",
            "manually",
            "email reminder"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/customers/loyalty/points/earnings/birthday",
        "category": "troubleshooting",
        "difficulty": "medium"
    },
    
    # ==================== Data/Report Questions ====================
    {
        "id": "sales-discount-report",
        "name": "Sales by Discount Report",
        "question": "What information is available in the Sales by discount report?",
        "expected_keywords": [
            "discount title",
            "discount amount",
            "total sales",
            "orders",
            "discount method"
        ],
        "forbidden_keywords": [],
        "doc_reference": "expand/genstore-analytics/reports/sales/discount",
        "category": "data",
        "difficulty": "medium"
    },
    
    {
        "id": "discount-report-usage",
        "name": "Discount Report Use Cases",
        "question": "What can I analyze with the Sales by discount report?",
        "expected_keywords": [
            "conversion rates",
            "promotional campaign",
            "discount methods",
            "revenue impact"
        ],
        "forbidden_keywords": [],
        "doc_reference": "expand/genstore-analytics/reports/sales/discount",
        "category": "data",
        "difficulty": "easy"
    },
    
    # ==================== Rules/Policy Questions ====================
    {
        "id": "abandoned-checkout-rules",
        "name": "Abandoned Checkout Rules",
        "question": "What are the rules for abandoned checkouts?",
        "expected_keywords": [
            "email address",
            "$0.00",
            "3 months",
            "declined card"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/orders/abandoned-cart",
        "category": "rules",
        "difficulty": "medium"
    },
    
    {
        "id": "birthday-email-notification",
        "name": "Birthday Email Notifications",
        "question": "When do customers receive email notifications for birthday point rewards?",
        "expected_keywords": [
            "automatic distribution",
            "manual redemption",
            "birthday",
            "email"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/customers/loyalty/points/earnings/birthday",
        "category": "rules",
        "difficulty": "medium"
    },
    
    # ==================== Complex Questions ====================
    {
        "id": "payment-failure-handling",
        "name": "Payment Failure vs Abandoned",
        "question": "How does Genstore handle payment failures differently for Genstore Payments vs third-party payment gateways in abandoned checkouts?",
        "expected_keywords": [
            "declined card",
            "insufficient funds",
            "order",
            "abandoned checkout",
            "third-party"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/orders/abandoned-cart",
        "category": "complex",
        "difficulty": "hard"
    },
    
    {
        "id": "birthday-manual-vs-auto",
        "name": "Birthday Manual vs Auto Distribution",
        "question": "What is the difference between automatic and manual distribution for birthday rewards?",
        "expected_keywords": [
            "auto",
            "manual",
            "automatically added",
            "claim",
            "email notification"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/customers/loyalty/points/earnings/birthday",
        "category": "complex",
        "difficulty": "medium"
    },
    
    # ==================== Navigation Questions ====================
    {
        "id": "find-abandoned-checkouts",
        "name": "Navigate to Abandoned Checkouts",
        "question": "Where can I find the abandoned checkouts page in Genstore admin?",
        "expected_keywords": [
            "store",
            "orders",
            "abandoned checkouts"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/orders/abandoned-cart",
        "category": "navigation",
        "difficulty": "easy"
    },
    
    {
        "id": "find-loyalty-settings",
        "name": "Navigate to Loyalty Settings",
        "question": "How do I navigate to the loyalty program settings?",
        "expected_keywords": [
            "store",
            "customers",
            "loyalty"
        ],
        "forbidden_keywords": [],
        "doc_reference": "operate/customers/loyalty/points/earnings/birthday",
        "category": "navigation",
        "difficulty": "easy"
    },
]


def get_all_test_cases() -> List[Dict]:
    """Get all test cases."""
    return QA_TEST_CASES


def get_test_cases_by_category(category: str) -> List[Dict]:
    """Get test cases filtered by category."""
    return [tc for tc in QA_TEST_CASES if tc["category"] == category]


def get_test_cases_by_difficulty(difficulty: str) -> List[Dict]:
    """Get test cases filtered by difficulty."""
    return [tc for tc in QA_TEST_CASES if tc["difficulty"] == difficulty]


def get_easy_test_cases() -> List[Dict]:
    """Get easy test cases for quick testing."""
    return get_test_cases_by_difficulty("easy")


def get_test_case_by_id(test_id: str) -> Dict:
    """Get a specific test case by ID."""
    for tc in QA_TEST_CASES:
        if tc["id"] == test_id:
            return tc
    return None


def get_categories() -> List[str]:
    """Get all unique categories."""
    return list(set(tc["category"] for tc in QA_TEST_CASES))


def get_test_stats() -> Dict:
    """Get statistics about test cases."""
    categories = {}
    difficulties = {}
    
    for tc in QA_TEST_CASES:
        cat = tc["category"]
        diff = tc["difficulty"]
        
        categories[cat] = categories.get(cat, 0) + 1
        difficulties[diff] = difficulties.get(diff, 0) + 1
    
    return {
        "total": len(QA_TEST_CASES),
        "categories": categories,
        "difficulties": difficulties
    }


if __name__ == "__main__":
    # Print test case stats
    stats = get_test_stats()
    
    print("=== QA Test Cases Stats ===")
    print(f"Total test cases: {stats['total']}")
    print(f"\nBy Category:")
    for cat, count in stats["categories"].items():
        print(f"  {cat}: {count}")
    print(f"\nBy Difficulty:")
    for diff, count in stats["difficulties"].items():
        print(f"  {diff}: {count}")
    
    print("\n=== Sample Test Case ===")
    sample = get_test_case_by_id("abandoned-checkout-definition")
    print(f"ID: {sample['id']}")
    print(f"Question: {sample['question']}")
    print(f"Expected Keywords: {sample['expected_keywords']}")
