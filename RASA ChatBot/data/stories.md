## story1
* goodbye
    - utter_first_bye
    - action_restart

## story1
* greet
    - utter_greet
* goodbye
    - utter_first_bye
    - action_restart

## story1
* greet
    - utter_greet
* deny
    - utter_first_bye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* iamabot
    - utter_iamabot
* affirm{"affirm": "ok"}
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet   
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
    - action_restart


## interactive_story_1   
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
    - action_restart


## interactive_story_1
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "roorkee"}
    - slot{"location": "roorkee"}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
    - action_restart



## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email 
* giving_email{"email": "deepaksjce2010@gmail.com"}
    - slot{"email": "deepaksjce2010@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* giving_email{"email": "deepaksjce2010@gmail.com"}
    - slot{"email": "deepaksjce2010@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart




## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "officail.tarang6@gmail.com"}
    - slot{"email": "officail.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": " Bangalore"}
    - slot{"location": " Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Bangalore"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": " Bangalore"}
    - slot{"location": " Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Bangalore"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart


## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
* affirm
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": " Bangalore"}
    - slot{"location": " Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Bangalore"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_location
* restaurant_search{"location": "Thiruvananthapuram"}
    - slot{"location": "Thiruvananthapuram"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Thiruvananthapuram"}
    - slot{"is_restaurant_avail": true}
* affirm
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "ludhiana"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
    - action_restart

## interactive_story_1
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "ludhiana"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
    - action_restart

## interactive_story_1
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "ludhiana"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
    - action_restart

## interactive_story_1
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "ludhiana"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Delhi"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_verify_budget
    - slot{"is_budget_valid": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "sahibabad"}
    - slot{"location": "sahibabad"}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "taranggpt6@gmail.com"}
    - slot{"email": "taranggpt6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "saharanpur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "saharanpur"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_verify_budget
    - slot{"is_budget_valid": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "19sagar94@gmail.com"}
    - slot{"email": "19sagar94@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart



## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart


    
## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

    
## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "Bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bangalore"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bangalore"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bangalore"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bangalore"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart




## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "balliya"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "balliya"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": false}
* affirm
    - utter_no_service
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_2
* restaurant_search{"cuisine": "mexican", "location": "Bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bangalore"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* affirm
    - utter_get_emailID
* giving_email{"email": "official.tarang6@gmail.com"}
    - slot{"email": "official.tarang6@gmail.com"}
    - action_send_email
    - slot{"is_mail_sent": true}
* affirm
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_location_check
    - slot{"is_location_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"is_cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs.300"}
    - slot{"budget": "Lesser than Rs.300"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"is_restaurant_avail": false}
    - utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - action_verify_budget
    - slot{"is_budget_valid": true}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"is_restaurant_avail": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart
