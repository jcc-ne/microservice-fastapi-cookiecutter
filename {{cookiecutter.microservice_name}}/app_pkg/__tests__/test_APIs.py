#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (c) 2021 janine <janine@MacBook-Pro.local>
#
# Distributed under terms of the GNU GPLv3 license.

"""

"""

from fastapi.testclient import TestClient

from main import app
from __version__ import version


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"version": version}
