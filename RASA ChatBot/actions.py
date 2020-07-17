# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

 #from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import location
import zomatopy
import email_p
import json
    


class ActionLocationValidation(Action):

    def name(self):
        return "action_location_check"

    # def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    def run(self, dispatcher,tracker,domain):
        loc = tracker.get_slot('location')
        obj = location.Validate_Location()
        check = obj.location_val(loc)
        if check:
            dispatcher.utter_message("Good news! We serve in this city!")
            return [SlotSet('is_location_verified',True)]
        else:
            dispatcher.utter_message("Sorry, We don't provide services in your area as of now but we are coming soon in your area.")
        return [SlotSet('is_location_verified',False)]

	#Below Class is used for Restaurant Search

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={"user_key":"d407d7041129c9c1395aaff316fa6749"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'mexican':73,'chinese':25,'american':1,'italian':55,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 25)
		d = json.loads(results)
		response=""
		less_than_3 = []
		t3_s7 = []
		more_than_7 = []
		global less_than_3_email
		global t3_s7_email
		global more_than_7_email
		less_than_3_email = []
		t3_s7_email = []
		more_than_7_email = []
		if d['results_found'] == 0:
			response= "no results"
			dispatcher.utter_message("-----"+response)
		else:
			for restaurant in d['restaurants']:
				if float(restaurant['restaurant']['average_cost_for_two']) < 300:
					less_than_3.append("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated : {}".format(restaurant['restaurant']['user_rating']['aggregate_rating']))
					less_than_3_email.append("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " and average budget for two people is {}".format(restaurant['restaurant']['average_cost_for_two']) + " which has been rated : {} ".format(restaurant['restaurant']['user_rating']['aggregate_rating']))
				elif float(restaurant['restaurant']['average_cost_for_two']) >= 300 and float(restaurant['restaurant']['average_cost_for_two']) <= 700:
					t3_s7.append("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated : {}".format(restaurant['restaurant']['user_rating']['aggregate_rating']))
					t3_s7_email.append("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " and average budget for two people is {}".format(restaurant['restaurant']['average_cost_for_two']) + " which has been rated : {} ".format(restaurant['restaurant']['user_rating']['aggregate_rating']))
				elif float(restaurant['restaurant']['average_cost_for_two']) >= 700:
					more_than_7.append("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated : {}".format(restaurant['restaurant']['user_rating']['aggregate_rating']))
					more_than_7_email.append("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " and average budget for two people is {}".format(restaurant['restaurant']['average_cost_for_two']) + " which has been rated : {} ".format(restaurant['restaurant']['user_rating']['aggregate_rating']))
		
			if(budget=='Lesser than Rs.300'):
				if len(less_than_3) == 0:
					dispatcher.utter_message("Sorry, We don't have any restaurant in "+ loc + " under selected budget range."+"\n".join(less_than_3[:5]))
					return[SlotSet('is_restaurant_avail',False)]
				else:
					dispatcher.utter_message("-----"+"\n".join(less_than_3[:5]))
			elif(budget=='Rs. 300 to 700'):
				if len(t3_s7) == 0:
					dispatcher.utter_message("Sorry, We don't have any restaurant in "+ loc + " under selected budget range."+"\n".join(t3_s7[:5]))
					return[SlotSet('is_restaurant_avail',False)]
				else:
					dispatcher.utter_message("-----"+"\n".join(t3_s7[:5]))
			elif(budget=='More than Rs. 700'):
				if len(more_than_7) == 0:
					dispatcher.utter_message("Sorry, We don't have any restaurant in "+ loc + " under selected budget range."+"\n".join(more_than_7[:5]))
					return[SlotSet('is_restaurant_avail',False)]
				else:
					dispatcher.utter_message("-----"+"\n".join(more_than_7[:5]))
		
		
		return [SlotSet('location',loc), SlotSet('is_restaurant_avail',True)]




class ActionVerifyBudget(Action):

    def name(self):
        return "action_verify_budget"

    def run(self, dispatcher, tracker, domain):
        #Initialize variables
        correct_budget = ['Lesser than Rs.300','Rs. 300 to 700','More than Rs. 700']
        error_msg = "Sorry!! price range not supported, please select from the dropdown list."
        
        selected_budget = tracker.get_slot('budget')
        if selected_budget in correct_budget:
            return [SlotSet('is_budget_valid', True)]
            #if(selected_budget == 'Lesser than Rs.300'):
            #    pass
            #elif(selected_budget == 'Rs. 300 to 700'):
            #   pass
            #elif(selected_budget=='More than Rs. 700'):
            #    pass
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('is_budget_valid', False)]

class ActionVerifyCuisine(Action):

    def name(self):
        return "action_verify_cuisine"

    def run(self, dispatcher, tracker, domain):
        #Initialize variables
        supported_cuisines = ['american','mexican','italian','chinese','south indian','north indian']
        error_msg = "Sorry!! this cuisine is currently not supported, please select from the dropdown list."
        
        selected_cuisine = tracker.get_slot('cuisine')
        if selected_cuisine.lower() in supported_cuisines:
            return [SlotSet('is_cuisine_valid', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('is_cuisine_valid', False)]

	#Below Class is used for Send the Email

class ActionSendEmail(Action):
    def name(self):
        return "action_send_email"

    # def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    def run(self, dispatcher,tracker,domain):
        em = tracker.get_slot('email')
        import re

        budget = tracker.get_slot('budget')
        obj = email_p.SendEmail()
        result = obj.send_Email(em,budget,less_than_3_email,t3_s7_email,more_than_7_email)
        if result == True:
            dispatcher.utter_message("Here you go, Email Sent! Bon Appetit!!")
            return [SlotSet('is_mail_sent',True)]
        else:
            dispatcher.utter_message("We are sorry :( unable to send the email. Please try again")
            return [SlotSet('is_mail_sent',False)]