-- write an SQL script that creates a trigger
-- that decreases the quantity of an item after adding a new order.
-- quantity in the table items can be negative
CREATE TRIGGER items_trigger AFTER INSERT INTO orders
FOR EACH ROW SET UPDATE items
SET quantity = (quantity - orders.number)
WHERE name = orders.item_name
