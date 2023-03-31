import requests
from base_config import *
import json


def find_place_by_text(output_type: str, input_str: str, api_key=google_api_key):
    """
    :param output_type: a string value is json or xml
    :param input_str:
    :param api_key:
    :return:
    """
    if ' ' in input_str:
        input_str = input_str.replace(' ', '%20')
    if ',' in input_str:
        input_str = input_str.replace(',', '%2C')
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/%s?input=%s&inputtype=textquery&key=%s" % \
          (output_type, input_str, api_key)

    response = requests.request("GET", url, headers={}, data={})
    return response


def find_place_by_phone_number(output_type: str, input_phone_number: str, api_key=google_api_key):
    """
    :param output_type: a string value is json or xml
    :param input_phone_number:
    :param api_key:
    :return:
    """
    input_phone_number_val = input_phone_number.replace('+', '%2B')
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/%s?input=%s&inputtype=phonenumber&key=%s" % \
          (output_type, input_phone_number_val, api_key)

    response = requests.request("GET", url, headers={}, data={})
    return response


def parse_place_id_from_search_by_text(response) -> str:
    res_body = json.loads(response.content)
    parsed_result = parse_status_from_search_place(response)
    if parsed_result == 'ZERO_RESULTS':
        return res_body['candidates']
    elif parsed_result == 'OK':
        return res_body['candidates'][0]['place_id']


def parse_place_ids_from_search_by_text(response) -> list:
    place_id_list = []
    res_body = json.loads(response.content)
    for i in res_body['candidates']:
        place_id_list.append(i['place_id'])
    return place_id_list


def parse_status_from_search_place(response) -> str:
    res_body = json.loads(response.content)
    return res_body['status']


def parse_error_msg_from_search_place(response) -> str:
    res_body = json.loads(response.content)
    if parse_status_from_search_place(response) == 'REQUEST_DENIED':
        return res_body['error_message']
    else:
        pass


def place_detail(output_type: str, place_id: str, api_key=google_api_key):
    """
    :param output_type: a string value is json or xml
    :param place_id: Place ID that gets from find place API
    :param api_key:
    :return:
    """
    url = "https://maps.googleapis.com/maps/api/place/details/%s?place_id=%s&key=%s" % (output_type, place_id, api_key)

    response = requests.request("GET", url, headers={}, data={})
    return response


def parse_formatted_phone_number_from_place_detail(response) -> str:
    res_body = json.loads(response.content)
    return res_body['result']['formatted_phone_number']


def parse_status_from_place_detail_request(response) -> str:
    res_body = json.loads(response.content)
    return res_body['status']




