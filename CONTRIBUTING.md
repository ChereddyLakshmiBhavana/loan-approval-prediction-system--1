# Contributing to AI-Driven Loan Approval Prediction System

## Getting Started

1. Clone the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests: `pytest tests/`
5. Commit: `git commit -m 'Add your feature'`
6. Push: `git push origin feature/your-feature`
7. Create a Pull Request

## Development Setup

```bash
# Run setup script
python setup_dev_environment.py

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run tests
pytest tests/ -v

# Start development server
python src/api/app.py
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused
- Write tests for new features

## Testing

- Write unit tests for all functionality
- Aim for >80% code coverage
- Run tests before committing: `pytest tests/ -v`
- Test both happy path and edge cases

## Documentation

- Update README.md for major changes
- Document new API endpoints in docs/API.md
- Add comments for complex logic
- Include examples in docstrings

## Commit Messages

Use clear, descriptive commit messages:
- `add: feature new feature name`
- `fix: bug description`
- `docs: updated documentation`
- `refactor: improved code structure`
- `test: added test cases`

## Pull Request Process

1. Ensure tests pass locally
2. Update documentation if needed
3. Add description of changes
4. Reference any related issues
5. Request review from team members

## Issues and Bugs

- Use clear titles and descriptions
- Include reproducible steps
- Mention expected vs actual behavior
- Include relevant logs or screenshots

## Feature Requests

- Describe use case and value
- Provide examples if possible
- Discuss architectural implications
- Get feedback before implementation

## Review Process

- All PRs require at least one approval
- Address review comments promptly
- Push updates rather than force-pushing
- Merge only when all tests pass

## Questions?

Open an issue or contact the team.

Happy coding!
