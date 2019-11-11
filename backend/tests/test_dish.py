#!/usr/bin/env python
# coding=utf-8

import unittest
import json

import pathmagic

from server import db
from base import BaseTestClass
from server.models.dish import Dish


class TestDish(BaseTestClass):
    dish = {
        'name': 'A test name',
        'description': 'A test description',
        'country': 'A test country',
        'category': 'A test category'
    }

    dish2 = {
        'name': 'A test name 2',
        'description': 'A test description 2',
        'country': 'A test country 2',
        'category': 'A test category 2'
    }

    def test_create_dish(self):
        data = {
            'name': 'A name',
            'description': 'A description',
            'country': 'A country',
            'category': 'A category'
        }

        res = self.tester_app.post(
            '/api/dishes',
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
            )

        self.assertEqual(res.status_code, 201)
        data = json.loads(res.get_data(as_text=True))
        expected_dish = {
            'id': 1,
            'name': 'A name',
            'description': 'A description',
            'country': 'A country',
            'category': 'A category'
            }
        dish = dict(data)
        self.assertDictEqual(dish, expected_dish)

    def test_get_a_dish(self):
        self.create_dish(self.dish)
        res = self.tester_app.get(
            '/api/dishes/1',
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.get_data(as_text=True))
        expected_dish = {
            'id': 1,
            'name': 'A test name',
            'description': 'A test description',
            'country': 'A test country',
            'category': 'A test category'
            }
        dish = dict(data)
        self.assertDictEqual(dish, expected_dish)

    def test_get_all_dishes(self):
        self.create_dish(self.dish)
        self.create_dish(self.dish2)
        res = self.tester_app.get(
            '/api/dishes/',
            headers={'Content-Type': 'application/json'}
        )
        data = json.loads(res.get_data(as_text=True))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_edit_a_dish(self):
        self.create_dish(self.dish)
        data = {
            'description': 'A different description',
        }
        res = self.tester_app.put(
            '/api/dishes/1',
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
            )
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        dish = Dish.query.get(1)
        self.assertEqual(dish.description, 'A different description')

    def test_delete_a_dish(self):
        self.create_dish(self.dish)
        res = self.tester_app.delete(
            '/api/dishes/1',
            headers={'Content-Type': 'application/json'}
            )

        self.assertEqual(res.status_code, 200)
        dish = Dish.query.get(1)
        self.assertIsNone(dish)

    def create_dish(self, data=dish):
        '''
        Function that presists a dish in the database for the test
        '''
        dish = Dish(
            name=data['name'],
            description=data['description'],
            country=data['country'],
            category=data['category'],
        )
        db.session.add(dish)
        db.session.flush()
