# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Index, String, Table
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT, VARCHAR,DATETIME
from sqlalchemy.ext.declarative import declarative_base
from .ext import db
Base = declarative_base()
metadata = Base.metadata


