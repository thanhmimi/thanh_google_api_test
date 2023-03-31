import pytest
from api.place_search_api import *


@pytest.fixture
def get_a_place_id(place_name):
    res = find_place_by_text('json', place_name)
    res_status = parse_status_from_search_place(res)
    if res.status_code != 200 and res_status != 'OK':
        raise Exception("Unable to get Place_ID due to status %s" % res_status)
    else:
        return parse_place_id_from_search_by_text(res)
