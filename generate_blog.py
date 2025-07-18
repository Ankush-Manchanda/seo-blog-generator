from openai import OpenAI, RateLimitError

client=OpenAI(api_key = "your_api_key")

def generate_blog(product, keywords):
    prompt = (
        f"Write a 150-200 word SEO-friendly blog post about '{product}'. "
        f"Use these keywords naturally: {', '.join(keywords)}."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except RateLimitError:
        return "🚫 API quota exceeded. Please check your OpenAI account usage."
