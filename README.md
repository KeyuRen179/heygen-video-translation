# Heygen Video Translation

## Project Description
This is a simulation of the Heygen Video Translation backend and client library project.

## Functionality
- Server side implementation of the `/status` interface, returning `pending`, `completed` or `error`.
- Client-side library implements polling logic, using exponential backoff to optimize resource calls.
- Integration tests are provided to demonstrate server-client interaction.

## Guidelines

### 1. Install dependencies
``bash
pip install -r requirements.txt
2. Start the server
bash
Copy the code
python server.py
3. Use the client library
python
Copy the code
from translation_client import TranslationClient

client = TranslationClient(“http://localhost:5000”)
status = client.get_status()
print(“Translation Status:”, status)
4. Run the integration test
bash
Copy the code
python integration_test.py
yaml
Copy the code

---

### 6. **Post-deployment Maintenance**
- **Update code:** After modifying code, commit and push new changes:
  ```bash
  git add .
  git commit -m “Update feature X”
  git push
Tagging: Use Git tags to mark project versions.
bash
Copy Code
git tag v1.0
git push origin v1.0

Translated with DeepL.com (free version)
