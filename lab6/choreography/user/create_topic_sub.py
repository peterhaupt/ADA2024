import logging

from user_consumer import create_subscription
from user_publisher import create_topic

logging.getLogger().setLevel(logging.INFO)
create_topic("vertical-theory-413015", "order_req") # make sure to change the project id
create_subscription("vertical-theory-413015", "order_req", "order_req_sub")
create_topic("vertical-theory-413015", "inventory_status")
create_topic("vertical-theory-413015", "order_status")
create_topic("vertical-theory-413015", "order_status_user")
create_subscription("vertical-theory-413015", "order_status_user", "order_status_user_sub")
create_topic("vertical-theory-413015", "order_req")
create_topic("vertical-theory-413015", "inventory_status")
create_subscription("vertical-theory-413015", "inventory_status",
                    "inventory_status_sub")
create_subscription("vertical-theory-413015", "order_status","order_status_sub")
