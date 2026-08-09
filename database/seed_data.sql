-- ConnectX — seed data for test table (Task 4) and admin user (Task 8)

INSERT INTO connection_test (name) VALUES ('seed_one');
INSERT INTO connection_test (name) VALUES ('seed_two');
INSERT INTO connection_test (name) VALUES ('seed_three');

-- Admin account: email admin@connectx.local, password user@123
INSERT INTO user (username, email, password_hash, role) VALUES (
  'admin',
  'admin@example.com',
  'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f',
  'admin'
);

-- User1 account: email user1@example.com, password user@123
INSERT INTO user (username, email, password_hash, role) VALUES (
  'user1',
  'user1@example.com',
  'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f',
  'user'
);

-- Profile for user1 (user_id = LAST_INSERT_ID() from user1 insert above)
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'User One', 'Hello, I am user1.');

-- Dummy users (user2–user11): password user@123 for all. Each pair: user insert then profile with LAST_INSERT_ID().
INSERT INTO user (username, email, password_hash, role) VALUES ('user2', 'user2@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Alex Rivera', 'Designer & coffee enthusiast.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user3', 'user3@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Sam Chen', 'Developer. Building things that matter.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user4', 'user4@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Jordan Lee', 'Writer. Ideas over algorithms.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user5', 'user5@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Taylor Kim', 'Product lead. User-first.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user6', 'user6@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Morgan Bell', 'QA engineer. Breaking things to fix them.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user7', 'user7@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Casey Brooks', 'DevOps. Keeping the lights on.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user8', 'user8@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Riley Davis', 'Data analyst. Stories in numbers.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user9', 'user9@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Quinn Foster', 'Support lead. Helping users win.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user10', 'user10@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Drew Morgan', 'Marketing. Connecting product and people.');

INSERT INTO user (username, email, password_hash, role) VALUES ('user11', 'user11@example.com', 'pbkdf2:sha256:260000$HYDf4SrncUh0q8JX$31e8438b37421cfade0e6706a55ffb159a0bd2b0b6b74af209fa03069e6fe91f', 'user');
INSERT INTO profile (user_id, display_name, bio) VALUES (LAST_INSERT_ID(), 'Skyler Hayes', 'Founder. Building in public.');

-- Dummy posts for user1 (user_id = 2; admin is 1)
INSERT INTO posts (user_id, content) VALUES (2, 'Hello ConnectX! Excited to be here.');
INSERT INTO posts (user_id, content) VALUES (2, 'Just set up my profile. Looking forward to connecting with everyone.');
INSERT INTO posts (user_id, content) VALUES (2, 'What are you building this week?');
INSERT INTO posts (user_id, content) VALUES (3, 'Coffee and code – the best combination.');
INSERT INTO posts (user_id, content) VALUES (3, 'Sharing some thoughts on productivity. Less context-switching, more deep work.');
INSERT INTO posts (user_id, content) VALUES (3, 'Weekend project: finally learning that new framework.');

-- Dummy likes (Task 12). UNIQUE(user_id, post_id) prevents duplicates.
INSERT INTO likes (user_id, post_id) VALUES (2, 1);
INSERT INTO likes (user_id, post_id) VALUES (2, 2);
INSERT INTO likes (user_id, post_id) VALUES (3, 1);
INSERT INTO likes (user_id, post_id) VALUES (3, 3);

-- Dummy comments (Task 13). Linked to existing users/posts.
INSERT INTO comments (user_id, post_id, content) VALUES (2, 1, 'Great start! Looking forward to more posts.');
INSERT INTO comments (user_id, post_id, content) VALUES (3, 1, 'Welcome to ConnectX!');
INSERT INTO comments (user_id, post_id, content) VALUES (2, 2, 'Nice profile update.');
INSERT INTO comments (user_id, post_id, content) VALUES (3, 3, 'I am building a Flask app this week.');

-- Task 15: reported content demo (requires reported_content table in db_schema.sql).
INSERT INTO reported_content (content_type, content_id, reason) VALUES
('post', 2, 'Misleading content'),
('comment', 2, 'Inappropriate language');
