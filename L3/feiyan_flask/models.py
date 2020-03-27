# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Index, String
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PlayerBasic(Base):
    __tablename__ = 'player_basic'

    playerId = Column(BIGINT(255), primary_key=True)
    code = Column(VARCHAR(255))
    country = Column(VARCHAR(255))
    countryEn = Column(VARCHAR(255))
    displayAffiliation = Column(VARCHAR(255))
    displayName = Column(VARCHAR(255))
    displayNameEn = Column(VARCHAR(255))
    dob = Column(VARCHAR(255))
    draftYear = Column(INTEGER(10))
    experience = Column(TINYINT(4))
    firstInitial = Column(VARCHAR(255))
    firstName = Column(VARCHAR(255))
    firstNameEn = Column(VARCHAR(255))
    height = Column(Float(4))
    jerseyNo = Column(TINYINT(4))
    lastName = Column(VARCHAR(255))
    lastNameEn = Column(VARCHAR(255))
    leagueId = Column(VARCHAR(255))
    position = Column(VARCHAR(255))
    schoolType = Column(VARCHAR(255))
    teamId = Column(VARCHAR(255))
    weight = Column(VARCHAR(255))


class PlayerNew(Base):
    __tablename__ = 'player_news'

    id = Column(INTEGER(11), primary_key=True)
    playerId = Column(BIGINT(20))
    publishDate = Column(DateTime)
    title = Column(String(255))
    sentimentDistTitle = Column(String(255))
    publisher = Column(String(255))
    url = Column(String(255), index=True)


class PlayerWeibo(Base):
    __tablename__ = 'player_weibo'

    id = Column(INTEGER(11), primary_key=True)
    playerId = Column(BIGINT(20), nullable=False)
    publishDate = Column(DateTime)
    publisher = Column(VARCHAR(255))
    text = Column(VARCHAR(255))
    shareCount = Column(INTEGER(10))
    commentCount = Column(INTEGER(10))
    likeCount = Column(INTEGER(10))
    url = Column(VARCHAR(255), unique=True)


class PlayerWeiboIndex(Base):
    __tablename__ = 'player_weibo_index'
    __table_args__ = (
        Index('weibo_index', 'playerId', 'currentDate', 'queryWord', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    playerId = Column(BIGINT(20), nullable=False)
    value = Column(INTEGER(10))
    currentDate = Column(DateTime)
    queryWord = Column(String(255))


class TeamBasic(Base):
    __tablename__ = 'team_basic'

    id = Column(VARCHAR(255), primary_key=True)
    abbr = Column(VARCHAR(255))
    city = Column(VARCHAR(255))
    cityEn = Column(VARCHAR(255))
    code = Column(VARCHAR(255))
    conference = Column(VARCHAR(255))
    displayAbbr = Column(VARCHAR(255))
    displayConference = Column(VARCHAR(255))
    division = Column(VARCHAR(255))
    isAllStarTeam = Column(VARCHAR(255))
    isLeagueTeam = Column(VARCHAR(255))
    leagueId = Column(VARCHAR(255))
    name = Column(VARCHAR(255))
    nameEn = Column(VARCHAR(255))
