
# Website Automation Script

This script automates interactions on a website using Selenium. It simulates login, random interactions with page elements, video playback, and PDF viewing for 30 minutes.

## Features

- Login automation
- Random clicking of non-assignment elements
- Simulated video playback
- PDF link handling
- Auto-scrolling

## Requirements

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (make sure the version matches your Chrome browser)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Cnu12224/lms_website_automation.git
   cd website_automation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the `automate_website_scroll.py` file with:
   - Your website URL
   - Your login credentials
   - The path to `chromedriver`

4. Run the script:
   ```bash
   python automate_website_scroll.py
   ```

## Note

This is intended for educational/demo purposes. Do not use it on websites without permission.
