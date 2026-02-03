# API Testing Framework 🧪

Automated API testing framework with contract testing and performance testing support.

## Features

- ✅ Contract-based testing
- ✅ Performance benchmarking
- ✅ CI/CD integration
- ✅ Beautiful test reports
- ✅ Easy setup

## Quick Start

```bash
pip install api-testing-framework

# Or use with Docker
docker compose up -d
```

## Usage

```python
from api_tester import APITester

tester = APITester('https://api.example.com')

# Test GET endpoint
tester.get('/users')
  .expect_status(200)
  .expect_json_schema({'name': str})
  .run()

# Test POST endpoint
tester.post('/users', json={'name': 'John'})
  .expect_status(201)
  .run()
```

## License

MIT License

## Topics

api-testing, testing, contracts, ci-cd, performance
