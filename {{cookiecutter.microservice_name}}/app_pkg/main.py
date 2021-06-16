#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (c) 2021 janine <janine@MacBook-Pro.local>
#
# Distributed under terms of the GNU GPLv3 license.

"""

"""

from __version__ import version
import uvicorn
import os
from fastapi import FastAPI, status
# from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.utils import get_openapi
import logging

from pydantic_models.models import (
    User, UserList
)

from src import proc


app = FastAPI(
    title="{{cookiecutter.microservice_name}}",
    description="{{cookiecutter.microservice_name}}",
    version=version,
    openapi_url="/api/v1/openapi.json",
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"version": version}


@app.post("/add_user", response_model=UserList)
async def add_user(input_: User):
    logging.info(input_)
    ret = proc.add_user(input_.user_id, input_.first_name)
    return {'users': ret}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8081)),
        reload=True,
    )
