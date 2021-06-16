#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GNU GPLv3 license.

"""

"""


fake_db = {}


def add_user(user_id, first_name):
    if fake_db.get(user_id):
        return
    fake_db[user_id] = first_name
    return [{"user_id": k, "first_name": v} for k, v in fake_db.items()]
