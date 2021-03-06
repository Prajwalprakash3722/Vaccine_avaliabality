####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 13/03/2021
# Goal: To find a district by its pincode or to find Pincode of the given district
# licensed under MIT
# If you want to build the same app for feel free to fork it from my repo and make the necessary changes, But attriubution
# to the handle @Prajwalprakash3722 in GitHub is mandatory.
###################################################################################################################################################################
import  requests
import json

from requests.models import Response

# Get District by Pincode

def get_pincode(pincode):

    try:
        URl = f'https://api.postalpincode.in/pincode/{pincode}'
        response = requests.get(URl)
        status = response.status_code
        if status == 200:
            json_data = json.loads(response.text)
            for x in json_data:
                readable_json = x['PostOffice']
                for y in readable_json:
                    city_name = y['Name']
                    city_division = y['Division']
                    city_district = y['District']
                    city_state = y['Circle']
                    if city_state == 'Karnataka':
                        return city_name, city_division, city_district
                    else:
                        return 'This service is only enabled for Karnataka. '
    except:
        status = "Enter correct Pincode"
        return status


# Get Pincode by district name

def get_district_name(district_name):

    try:
        URl = f'https://api.postalpincode.in/postoffice/{district_name}'
        response = requests.get(URl)
        status = response.status_code
        if status == 200:
            readable_json_data = json.loads(response.text)
            for x in readable_json_data:
                postoffice = x['PostOffice']
                for y in postoffice:
                    no_of_pincodes = y['Message']
                    city_name = y['Name']
                    city_pincode = y['Pincode']
                    print(no_of_pincodes, city_name, city_pincode)
    except:
        status = "Enter correct Pincode"
        print(status)

def sample_data(pincode):
    
    try:
        url = f'https://api.postalpincode.in/pincode/{pincode}'
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            readableA_json_data = json.loads(response.text)
            for x in readableA_json_data:
                data = x['PostOffice']

        return data
    except:
        return 'No data found'