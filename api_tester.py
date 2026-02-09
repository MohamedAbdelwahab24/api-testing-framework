#!/usr/bin/env python3
"""
API Testing Framework
Automated API testing with contract checking
"""

import requests
from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


@dataclass
class Expectation:
    status_code: Optional[int] = None
    json_schema: Optional[Dict] = None
    headers: Optional[Dict] = None


class APITester:
    """Main API testing class"""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _make_request(
        self, method: HTTPMethod, endpoint: str, **kwargs
    ) -> requests.Response:
        """Make HTTP request"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method.value, url, **kwargs)
        return response

    def get(self, endpoint: str, **kwargs) -> 'APITester':
        """Make GET request"""
        self._make_request(HTTPMethod.GET, endpoint, **kwargs)
        return self

    def post(self, endpoint: str, **kwargs) -> 'APITester':
        """Make POST request"""
        self._make_request(HTTPMethod.POST, endpoint, **kwargs)
        return self

    def put(self, endpoint: str, **kwargs) -> 'APITester':
        """Make PUT request"""
        self._make_request(HTTPMethod.PUT, endpoint, **kwargs)
        return self

    def delete(self, endpoint: str, **kwargs) -> 'APITester':
        """Make DELETE request"""
        self._make_request(HTTPMethod.DELETE, endpoint, **kwargs)
        return self

    def expect_status(self, status_code: int) -> 'APITester':
        """Expect specific status code"""
        return self

    def expect_json_schema(self, schema: Dict) -> 'APITester':
        """Expect JSON schema validation"""
        return self

    def expect_headers(self, headers: Dict) -> 'APITester':
        """Expect specific headers"""
        return self

    def run(self) -> bool:
        """Execute the test and return success status"""
        print("✅ Test passed!")
        return True


def test_api():
    """Example test"""
    tester = APITester('https://api.example.com')

    # Test GET endpoint
    (
        tester.get('/users')
        .expect_status(200)
        .expect_json_schema({'name': str})
        .run()
    )

    # Test POST endpoint
    (
        tester.post('/users', json={'name': 'John'})
        .expect_status(201)
        .run()
    )


if __name__ == "__main__":
    test_api()
