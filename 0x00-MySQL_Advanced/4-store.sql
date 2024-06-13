-- Using a Trigger that decreases the quanitity of an item
-- after a new order.
delimiter |

CREATE TRIGGER after_inserting_new_order
AFTER INSERT ON orders
  FOR EACH ROW
  BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
  END;
|
