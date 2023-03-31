from api.place_search_api import *
from base_config import *
import logging
import pytest


class TestGoogleSearchAPI(object):

    def test_valid_search_place_using_text_query(self):
        res = find_place_by_text('json', valid_search_place_txt)
        assert res.status_code == 200
        assert parse_status_from_search_place(res) == 'OK'
        res_place_id = parse_place_id_from_search_by_text(res)
        assert res_place_id and res_place_id.isidentifier()

    def test_valid_search_place_using_phone_number(self):
        res = find_place_by_phone_number('json', registered_phone_number)
        assert res.status_code == 200
        assert parse_status_from_search_place(res) == 'OK'
        res_place_ids = parse_place_ids_from_search_by_text(res)
        assert len(res_place_ids) >= 1

    @pytest.mark.parametrize("place_name", [valid_search_place_txt])
    def test_get_valid_place_detail(self, get_a_place_id):
        res = place_detail('json', get_a_place_id)
        assert res.status_code == 200
        assert parse_status_from_place_detail_request(res) == 'OK'

    def test_no_search_place_using_text_query(self):
        res = find_place_by_text('json', no_search_place_txt)
        assert res.status_code == 200
        assert parse_status_from_search_place(res) == 'ZERO_RESULTS'
        res_place_id = parse_place_id_from_search_by_text(res)
        assert not res_place_id # the list is null as expected

    def test_invalid_api_key_when_search_place_using_text_query(self):
        res = find_place_by_text('json', no_search_place_txt, api_key='thiskeyiwrongone')
        assert res.status_code == 200
        assert parse_status_from_search_place(res) == 'REQUEST_DENIED'
        assert parse_error_msg_from_search_place(res) == 'The provided API key is invalid.'

    @pytest.mark.parametrize("place_name", [valid_search_place_txt])
    def test_get_valid_formatted_phone_number_from_place_detail(self, get_a_place_id):
        res = place_detail('json', get_a_place_id)
        assert res.status_code == 200
        assert parse_status_from_place_detail_request(res) == 'OK'
        assert parse_formatted_phone_number_from_place_detail(res).replace(' ', '') in registered_phone_number
