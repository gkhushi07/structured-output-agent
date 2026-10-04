from app.models import Article


article = Article(
    title="Apple Revenue Growth",
    summary="Apple revenue increased by 10%.",
    sentiment="positive"
)

# print(article)

print(article.model_dump())
