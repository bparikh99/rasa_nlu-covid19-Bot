## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  
## what is corona
* corona_intro
  - utter_corona_intro

## about1
*covid
-utter_covid
  
## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  
## about symptoms
* symptoms
  - utter_ans_sym
  - utter_name
* my_name{"NAME":"bhavya"}
  - slot{"NAME":"bhavya"}
  - action_your_name
 
## state_data_with_district
* state{"user_state":"Gujarat","user_district":"Surat"}
  - slot{"user_state":"Gujarat","user_district":"Surat"}
  - action_total_cases
  - utter_email
* my_email{"email_id":"parikhsamir80@gmail.com"}
  - slot{"email_id":"parikh80samir@gmail.com"}
  - utter_mobile
* my_number{"mob_no":"9377642717"}
  - slot{"mob_no":"9377642717"}
  - utter_information
  - action_email_sent
  
## state_data
* how_many_cases{"iso_state":"KA"}
  - slot{"iso_state":"KA"}
  - action_total_cases_in_state
  - utter_email
* my_email{"email_id":"parikhsamir80@gmail.com"}
  - slot{"email_id":"parikh80samir@gmail.com"}
  - utter_mobile{"mob_no":"9377642717"}
  - slot{"mob_no":"9377642717"}
* my_number
  - utter_information
  - action_email_sent
 
## loction_is_not_provided
* location_provider
  - utter_location_enter
* dont_know_anything
  - utter_details_inlink
  - utter_did_that_help1

 
## about_graphics
* graph
 - utter_graph
 - action_graphics_1
 
## about_how_are_you
* fine
 - utter_iamabot
 
## worry_about
* worry
 - utter_worry_ans
 
## dont_provide
* dont_provide
 - utter_provide_info