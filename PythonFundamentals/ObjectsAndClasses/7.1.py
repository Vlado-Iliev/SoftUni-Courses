article = Article(
'Highest Recorded Temperature';,
'Temperatures across Europe are unprecedented, according to scientists'.,
'Ben Turner'
)
article.edit(
'Syracuse, a city on the coast of the
Italian island of Sicily, registered
temperatures of 48.8 degrees Celsius''
)
article.rename(
'Temperature in Italy'
)
article.change_author(
'B. T.'
)
print(article)