import json
import pytest

from data.test_data import candidates_keys
from data.test_data import invalid_ides
from data.test_data import symbols_for_candidates_name_or_position
from data.test_data import invalid_headers
from data.redis_db import RedisDB
from data.driven_test_data import DataDriven
from pages.candidates import Candidate


class TestCandidates(object):

    dd = DataDriven()
    db = RedisDB()
    can = Candidate()
    candidate_register = []

    @classmethod
    def ad_to_register(cls, response):
        cls.candidate_register.append(response.text.split('"id": ')[1].split(',')[0])

    @classmethod
    def setup(cls):
        cls.dd.generate()
        for cand_key in candidates_keys:
            cls.ad_to_register(cls.can.post(name=cls.dd.get_name(cand_key), position=cls.dd.get_position(cand_key)))

    @classmethod
    def teardown(cls):
        cls.db.clear_all_data()
        for url_id in cls.candidate_register:
            cls.can.delete_by_id(url_id)
        cls.candidate_register = []

    def test_get_list(self):
        assert self.can.get_list.status_code == 200

    def test_post_all_data_valid(self):
        cand_key = 'valid_name_and_position'
        post_response = self.can.post(name=self.dd.get_name(cand_key), position=self.dd.get_position(cand_key))
        self.ad_to_register(post_response)
        assert post_response.status_code == 201
        assert post_response.reason == 'CREATED'

    def test_post_name_absent(self):
        cand_key = 'absent_name'
        post_response = self.can.post(name=self.dd.get_name(cand_key), position=self.dd.get_position(cand_key))
        self.ad_to_register(post_response)
        assert post_response.status_code == 400
        for cand_data in self.dd.get_list_data:
            assert self.dd.get_name(cand_key) != cand_data['name']
            assert self.dd.get_position(cand_key) != cand_data['position']

    def test_post_position_absent(self):
        cand_key = 'absent_position'
        post_response = self.can.post(name=self.dd.get_name(cand_key), position=self.dd.get_position(cand_key))
        self.ad_to_register(post_response)
        assert post_response.status_code == 201
        assert post_response.reason == 'CREATED'

    def test_post_name_position_absent(self):
        cand_key = 'absent_name_and_position'
        post_response = self.can.post(name=self.dd.get_name(cand_key), position=self.dd.get_position(cand_key))
        self.ad_to_register(post_response)
        assert post_response.status_code == 400
        for cand_data in self.dd.get_list_data:
            assert self.dd.get_name(cand_key) != cand_data['name']
            assert self.dd.get_position(cand_key) != cand_data['position']

    @pytest.mark.parametrize('symbol', symbols_for_candidates_name_or_position)
    def test_post_symbols_in_name(self, symbol):
        cand_key = 'absent_name'
        post_response = self.can.post(name=symbol, position=self.dd.get_position(cand_key))
        self.ad_to_register(post_response)
        assert post_response.status_code == 400
        for cand_data in self.dd.get_list_data:
            assert self.dd.get_name(cand_key) != cand_data['name']
            assert symbol != cand_data['position']

    @pytest.mark.parametrize('symbol', symbols_for_candidates_name_or_position)
    def test_post_symbols_in_position(self, symbol):
        cand_key = 'absent_position'
        post_response = self.can.post(name=self.dd.get_name(cand_key), position=symbol)
        self.ad_to_register(post_response)
        assert post_response.status_code == 400
        for cand_data in self.dd.get_list_data:
            assert self.dd.get_name(cand_key) != cand_data['name']
            assert symbol != cand_data['position']

    @pytest.mark.parametrize('header_key', invalid_headers)
    def test_post_invalid_data_in_header(self, header_key):
        content_type = invalid_headers[header_key][0]
        content_format = invalid_headers[header_key][1]
        cand_key = 'valid_name_and_position'
        name = self.dd.get_name(cand_key)
        position = self.dd.get_position(cand_key)
        post_response = self.can.post(name=name, position=position, headers={content_type: content_format})
        assert post_response.status_code == 400

    @pytest.mark.parametrize('cand_key', candidates_keys)
    def test_get_by_id(self, cand_key):
        name = self.dd.get_name(cand_key)
        position = self.dd.get_position(cand_key)
        for url_id in self.candidate_register:
            assert self.can.get_by_id(url_id).status_code == 200
            for cand in self.dd.get_list_data:
                assert int(url_id) == cand['id']
                assert name == cand['name']
                assert position == cand['position']

    @pytest.mark.parametrize('inv_id', invalid_ides)
    def test_get_by_wrong_id(self, inv_id):
        assert self.can.get_by_id(inv_id).status_code != 200

    def test_delete_by_id(self):
        for url_id in self.candidate_register:
            response_delete = self.can.delete_by_id(url_id)
            assert response_delete.status_code == 200
            assert response_delete.text.split(': ')[1].split('\n')[0] == 'true'
            assert response_delete.reason == 'OK'

    @pytest.mark.parametrize('cand_key', candidates_keys)
    def test_data_by_id_deleted(self, cand_key):
        for url_id in self.candidate_register:
            self.can.delete_by_id(url_id)
        name = self.dd.get_name(cand_key)
        position = self.dd.get_position(cand_key)
        for cand_data in self.dd.get_list_data:
            for url_id in self.candidate_register:
                assert cand_data['id'] != int(url_id)
            assert name != cand_data['name']
            assert position != cand_data['position']
