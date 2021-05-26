SELECT users.first_name, 
     users.last_name,
     users.email,
     products.title,
     categories.title,
     products.price,
     product_images.file
FROM
	users
	JOIN products ON users.id = products.user_id
	JOIN categories_products ON products.id = categories_products.product_id
	JOIN categories  ON categories_products.category_id = categories.id
	JOIN product_images ON products.id = product_images.product_id
