# 📝 AI-Based SEO Blog Post Creation Tool

## 🚀 Overview

This project is an AI-powered tool that automates the creation of SEO-optimized blog posts based on trending or best-selling e-commerce products. It scrapes trending items, generates relevant keywords, and produces short blog content using OpenAI's GPT models. Designed with Streamlit, it provides an easy-to-use web interface for content creators and affiliate marketers.

---------------------------------------------------------

## 📌 Features

- 🔎 Scrapes trending products from **Amazon India**
- 📈 Automatically generates 3–4 SEO-friendly keywords per product
- 🧠 Uses **OpenAI GPT-3.5 Turbo** to generate a 150–200 word blog
- 💻 Built with **Streamlit** for a smooth web interface
- ✅ Displays selected keywords and blog post clearly
- 📤 Easily exportable blog content for publishing

---------------------------------------------------------

## 🛠️ Tools & Libraries Used

| Library         | Purpose                           |
|-----------------|-----------------------------------|
| `requests`      | Scrape product data               |
| `BeautifulSoup` | Parse HTML from e-commerce site   |
| `re`            | Clean and simplify product titles |
| `OpenAI`        | Generate blog content (GPT-3.5)   |
| `Streamlit`     | Web interface and app hosting     |

---------------------------------------------------------

## 🔄 Pipeline Workflow

1. **Scrape Products**: Extract trending product names from Amazon.
2. **Generate Keywords**: Clean product names and form SEO keyword variants.
3. **Generate Blog**: Send product + keywords to OpenAI to generate a 150–200 word blog.
4. **Display Output**: Show keywords and blog via Streamlit interface.

---------------------------------------------------------

## 📸 Sample Output

**Product**:  
`Nutripro Juicer Mixer Grinder - Smoothie Maker - 500 Watts`

**SEO Keywords**:
```
• nutripro juicer mixer grinder  
• best nutripro juicer mixer grinder online  
• nutripro juicer mixer grinder price  
• buy nutripro juicer mixer grinder  
```

**Blog**:
> The Nutripro Juicer Mixer Grinder is the perfect kitchen companion for anyone who values efficiency and versatility. With 500 watts of power, it blends, grinds, and juices seamlessly...

---------------------------------------------------------

## ⚙️ How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/ankush-manchanda/seo-blog-generator.git
   cd seo-blog-generator
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API Key**
   - In `generate_blog.py`, set your key:
     ```python
     import openai
     openai.api_key = "sk-..."
     ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---------------------------------------------------------

## 🧪 Project Structure

```
seo-blog-generator/
├── app.py                   # Main Streamlit app
├── scrape_amazon.py         # Scraper for trending products
├── get_keywords.py          # SEO keyword generator
├── generate_blog.py         # Blog content generator (OpenAI)
├── requirements.txt
└── README.md
```

---------------------------------------------------------

## ⚠️ Known Issues

- 🔐 OpenAI API quota limits may restrict repeated blog generation
- 🚫 Amazon product scraping can fail if blocked by their anti-bot systems
- 📶 Requires active internet for scraping and OpenAI calls

---------------------------------------------------------

## 💡 Future Improvements

- Export blog to `.txt` / `.pdf` / `.md`
- Publish directly to Medium or WordPress
- Integrate real-time SEO tools (Ubersuggest, Google Trends)
- Replace OpenAI with open-source models (e.g., LLaMA, Mixtral)
- Add support for other e-commerce sites (Flipkart, eBay)

---------------------------------------------------------

## 👨‍💻 Author

**Ankush Manchanda**  
🔗 [GitHub](https://ankush-manchanda.github.io/masterportfolio) | 📧 ankushmanchanda111@gmail.com

---------------------------------------------------------

## 📄 License

This project is licensed under the MIT License. 
