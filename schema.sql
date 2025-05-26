CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS magazines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    magazine_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (magazine_id) REFERENCES magazines(id)
);

INSERT INTO authors (name) VALUES ('Jane Doe');
INSERT INTO authors (name) VALUES ('John Smith');
INSERT INTO authors (name) VALUES ('Alice Johnson');

INSERT INTO magazines (name, category) VALUES ('Tech Monthly', 'Technology');
INSERT INTO magazines (name, category) VALUES ('Health Weekly', 'Health');
INSERT INTO magazines (name, category) VALUES ('Travel Explorer', 'Travel');


INSERT INTO articles (title, author_id, magazine_id) VALUES ('The Future of AI', 1, 1);
INSERT INTO articles (title, author_id, magazine_id) VALUES ('Staying Healthy in 2025', 2, 2);
INSERT INTO articles (title, author_id, magazine_id) VALUES ('Top 10 Travel Destinations', 3, 3);
INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI in Healthcare', 1, 2);
INSERT INTO articles (title, author_id, magazine_id) VALUES ('Exploring the Mountains', 3, 3);
INSERT INTO articles (title, author_id, magazine_id) VALUES ('Tech Gadgets Review', 1, 1);
INSERT INTO articles (title, author_id, magazine_id) VALUES ('Healthy Eating Tips', 2, 2);
