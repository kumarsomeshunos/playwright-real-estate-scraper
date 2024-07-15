from playwright.sync_api import sync_playwright

# Define constants for selectors and settings
BASE_URL = "https://hprera.nic.in/PublicDashboard"
REGISTERED_PROJECTS_SELECTOR = "#reg-Projects"
CARDS_SELECTOR = "#reg-Projects > div > div"
CARD_CLASS_SELECTOR = ".col-lg-6"
CARD_NAME_SPAN_SELECTOR = "div > div > span.font-lg.fw-600"
CARD_DETAILS_BUTTON_SELECTOR = "div > div > a"
CARD_DETAILS_ID_SELECTOR = "#project-menu-html > div:nth-child(2) > div:nth-child(1)"
CARD_DETAILS_TABLE_ROW_SELECTOR = "#project-menu-html > div:nth-child(2) > div:nth-child(1) > div > table > tbody > tr"
CARD_DETAILS_NAME_SELECTOR = "td.fw-600"
CARD_DETAILS_DATA_SELECTOR = "td > span.fw-600"
CARD_DETAILS_CLOSE_BUTTON_SELECTOR = "#modal-data-display-tab_project_main > div > div > div.modal-header > button.close > span"
TIMEOUT = 50000
NUMBER_OF_CARDS_TO_READ = 6

def extract_data_from_card(page, card_div):
    """
    Extracts and prints project details from an individual project card.
    
    Args:
        page: The Playwright page object.
        card_div: The div element containing the project card.
    """
    # Click on the details button to open the project details modal
    details_anchor = card_div.query_selector(CARD_DETAILS_BUTTON_SELECTOR)
    details_anchor.click()
    
    # Wait for the project details modal to load
    page.wait_for_selector(CARD_DETAILS_ID_SELECTOR, timeout=TIMEOUT)
    
    # Get all rows in the project details table
    details_data = page.query_selector_all(CARD_DETAILS_TABLE_ROW_SELECTOR)
    
    # Extract and print relevant information from each row
    for data_row in details_data:
        if "Name" in data_row.text_content():
            main_value = data_row.query_selector(CARD_DETAILS_NAME_SELECTOR)
            print("Name: " + (main_value.text_content() if main_value else "Name data not available"))
        if "PAN" in data_row.text_content():
            main_value = data_row.query_selector(CARD_DETAILS_DATA_SELECTOR)
            print("PAN No.: " + (main_value.text_content() if main_value else "PAN No. data not available"))
        if "GSTIN" in data_row.text_content():
            main_value = data_row.query_selector(CARD_DETAILS_DATA_SELECTOR)
            print("GSTIN No.: " + (main_value.text_content() if main_value else "GSTIN No. data not available"))
        if "Permanent Address" in data_row.text_content():
            main_value = data_row.query_selector(CARD_DETAILS_DATA_SELECTOR)
            print("Permanent Address: " + (main_value.text_content() if main_value else "Permanent Address data not available"))
    
    # Close the project details modal
    close_button = page.query_selector(CARD_DETAILS_CLOSE_BUTTON_SELECTOR)
    close_button.click()

with sync_playwright() as p:
    # Launch a new browser instance
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to the base URL
    page.goto(BASE_URL)
    
    # Wait for the registered projects section to load
    page.wait_for_selector(REGISTERED_PROJECTS_SELECTOR, timeout=TIMEOUT)
    
    # Select the container holding all project cards
    content = page.query_selector(CARDS_SELECTOR)
    child_divs = content.query_selector_all(CARD_CLASS_SELECTOR)
    
    # Loop through each project card and extract data
    for index, card_div in enumerate(child_divs):
        if index == NUMBER_OF_CARDS_TO_READ:
            break
        
        # Extract and print the project name from the card
        name_span = card_div.query_selector(CARD_NAME_SPAN_SELECTOR)
        if name_span:
            print("NAME: " + (name_span.text_content() if name_span else None))
            extract_data_from_card(page, card_div)
    
    # Close the browser instance
    browser.close()