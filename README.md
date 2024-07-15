# Web Scraping Real Estate Project Data Using Playwright

## Project Description

This project uses Playwright, a powerful web scraping library, to extract data from the HPRERA website. It navigates through the website, identifies project cards, and retrieves details such as project names, PAN, GSTIN, and addresses from each card. The script can handle a large number of project cards efficiently and prints the extracted data for further processing or analysis.

## Tech Stack

- **Python**: Version 3.10
- **Libraries**:
  - `playwright`

## Prerequisites

- Python 3.10
- Playwright library

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install playwright
    playwright install
    ```

## Usage

To run the script, use the following command:
```bash
python script.py
```

Ensure you replace `script.py` with the actual name of your script file.

## Script Details

The script performs the following actions:

1. Launches a headless Chromium browser.
2. Navigates to the HPRERA Public Dashboard.
3. Waits for the registered projects section to load.
4. Selects and iterates through project cards to extract details.
5. Prints the extracted project details to the console.
6. Closes the browser.

### Functions

- **extract_data_from_card(page, card_div)**: Extracts and prints project details from an individual project card.

### Constants

- `BASE_URL`: The URL of the HPRERA Public Dashboard.
- `REGISTERED_PROJECTS_SELECTOR`, `CARDS_SELECTOR`, `CARD_CLASS_SELECTOR`, `CARD_NAME_SPAN_SELECTOR`, `CARD_DETAILS_BUTTON_SELECTOR`, `CARD_DETAILS_ID_SELECTOR`, `CARD_DETAILS_TABLE_ROW_SELECTOR`, `CARD_DETAILS_NAME_SELECTOR`, `CARD_DETAILS_DATA_SELECTOR`, `CARD_DETAILS_CLOSE_BUTTON_SELECTOR`: Various CSS selectors used to locate elements on the page.
- `TIMEOUT`: Timeout value for waiting for elements to load.
- `NUMBER_OF_CARDS_TO_READ`: The number of project cards to read and extract data from.

## Example Output

```
NAME: Project XYZ
Name: Project XYZ Name data not available
PAN No.: ABCDE1234F
GSTIN No.: 22ABCDE1234F1Z5
Permanent Address: 123 Main St, City, State
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the Playwright team for creating such a robust web scraping tool.

## Contact

For any questions or feedback, please visit [kumarsomesh.in](https://kumarsomesh.in).

---

PS: This README file was generated using GPT.