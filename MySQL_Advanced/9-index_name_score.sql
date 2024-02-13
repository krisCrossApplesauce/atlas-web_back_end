-- write an SQL script that creates an index called idx_name_first_score
-- on the table names and the first letter and the score
CREATE INDEX idx_name_first_score ON names (name(1), score);
