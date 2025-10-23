# 📰 Web Scraper for News Headlines

##  Objective
This project automates the collection of top news headlines from a public news website (BBC News in this example) using Python.

---

## Tools & Libraries
- **Python 3.13**
- **requests** - To fetch HTML content
- **BeautifulSoup (bs4)** - To parse and extract data from the webpage

---

## ⚙️ How It Works
1. The script sends an HTTP GET request to a public news website using `requests`.
2. It parses the HTML response with `BeautifulSoup`.
3. It extracts all `<h2>` tags (which usually contain headlines).
4. The extracted headlines are saved into a file named **`headlines.txt`**.

---

##  Concepts Used
| Concept | Description |

| `requests.get()` | Fetches webpage content from the given URL |
| `BeautifulSoup` | Parses HTML structure for easy data extraction |
| `.find_all('h2')` | Finds all `<h2>` tags that contain news titles |
| File I/O | Writes extracted headlines into a `.txt` file |

---

##  How to Run the Project

### 1️ Install Dependencies
```bash
pip install requests beautifulsoup4

---

python headlines.py

