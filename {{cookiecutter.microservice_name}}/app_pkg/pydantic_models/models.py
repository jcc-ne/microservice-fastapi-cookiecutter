#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the GNU GPLv3 license.

"""

"""

# from enum import Enum
from pydantic import BaseModel, Field, validator
from typing import Optional, List


class User(BaseModel):
    user_id: int
    first_name: Optional[str] = Field(None, example='Foo')

    @validator('first_name')
    def check_first_name_len(cls, v):
        if not v:
            return v
        assert len(v) > 2, "name length must >= 3 characters"
        return v


class UserList(BaseModel):
    users: List[User]
