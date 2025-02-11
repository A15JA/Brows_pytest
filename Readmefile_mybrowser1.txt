# Python Web Browser

**Overview**

This repository contains a simple web browser application built using Python and PyQt5. It demonstrates fundamental web browsing functionalities, providing a valuable learning experience for GUI development and web rendering with PyQt5.

**Features**

*   **Web Page Rendering:** Displays web pages using the QWebEngineView widget.
*   **Navigation:**
    *   Go Back to previously visited pages.
    *   Go Forward to subsequently visited pages.
    *   Reload the current page.
*   **Home Button:** Quickly return to the specified homepage (default: Google).
*   **URL Bar:** Enter any valid URL to browse the web.
*   **Full-Screen Mode:** Opens the browser in a maximized window for a better viewing experience.

**Installation**

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/A15JA/brows-proj-py-repo.git](https://github.com/A15JA/brows-proj-py-repo.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd brows-proj-py-repo
    ```

3.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv 
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

**Usage**

To run the browser, execute:

```bash
python3 browser.py