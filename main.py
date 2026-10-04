from app.agent import process_article


# article_text = """
# Apple reported that its quarterly revenue increased by 10%.
# The company said strong iPhone sales contributed to the growth.
# """

article_text = """
TechNova reported a sharp decline in its financial performance this quarter.
Revenue fell by 28% compared with the same period last year, while net profit
dropped by 45%. The company also announced that it will lay off 2,000 employees
because of weak demand and rising operating costs. Management warned that the
next quarter could be challenging and lowered its revenue forecast for the year.
Investors reacted negatively to the announcement, and the company's share price
fell 12% following the results.
"""


article = process_article(article_text)


if article:
    print("Title:", article.title)
    print("Summary:", article.summary)
    print("Sentiment:", article.sentiment)
