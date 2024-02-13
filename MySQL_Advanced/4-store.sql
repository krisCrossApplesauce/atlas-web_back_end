-- write an SQL script that creates a trigger
-- that decreases the quantity of an item after adding a new order.
-- quantity in the table items can be negative
CREATE TRIGGER items_trigger AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = (quantity - orders.number)
WHERE name = orders.item_name;
