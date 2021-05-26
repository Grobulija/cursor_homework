ALTER TABLE products
ADD COLUMN user_id INT NOT NULL;

UPDATE products
SET user_id = 1 
WHERE id = 1;

ALTER TABLE products
ADD FOREIGN KEY (user_id) REFERENCES users(id);
