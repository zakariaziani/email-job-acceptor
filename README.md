# Job Acceptor

## 📋 Functional Specifications

### 1. Email Monitoring
- Continuously monitor an email inbox (Gmail, Outlook, or IMAP server).
- Filter emails by:
  - Sender address (e.g., `alerts@company.com`)
  - Subject pattern (e.g., `"ALERT: *"`)

### 2. Email Parsing
- Extract and print:
  - The email subject
  - The HTML body
- Search for and extract a URL within the email body matching a regex pattern (e.g., `https://example.com/action/*`)

### 3. Web Navigation & Interaction
- Open the extracted link in a headless browser.
- Wait for the page to fully load.
- Locate and click a button with specific attributes (e.g., a button with `id="confirm"`, or text like `"Claim"`).

### 4. Logging & Error Handling
- Log each step and outcome.
- Handle errors such as:
  - No matching email
  - Invalid link
  - Timeout or failure to load the page
  - Button not found

# 👨‍💻 Technical Specifications

| Component | Details |
|-----------|---------|
| Language | Python |
| Email Access | Use local Outlook Desktop via `win32com.client`. |
| Email Parsing | `email`, `bs4` (BeautifulSoup) for HTML parsing |
| Web Automation | `Selenium` with `ChromeDriver` in headless mode |
| Regex Matching | `re` module |
| Logging | `logging` module |

## 🔗 Link Behavior

- Email contains a public link (e.g., `https://example.com/xyz`).
- The page requires login before allowing interaction.

## 🔐 Website Authentication

- Username and password fields are required.
- Login is done with username (not email) and password.
- Login button text: `"Sign in"`

# 🏃 How to run

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the script

```bash
python main.py
```
