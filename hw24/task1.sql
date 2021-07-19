SELECT * FROM articles
    LEFT JOIN article_categories ac ON articles.id = ac.article_id
    LEFT JOIN category c ON ac.category_id = c.id;