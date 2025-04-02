ALTER TABLE subscribers
ADD COLUMN subscription_date DATE DEFAULT (CURRENT_DATE);
