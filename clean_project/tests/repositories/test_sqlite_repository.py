import pytest
from clean_project.database import base, models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def db():
    engine = create_engine(
        "sqlite:///:memory:", connect_args={"check_same_thread": False}
    )
    TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    base.Base.metadata.create_all(bind=engine)
    yield TestSession()


@pytest.mark.usefixtures("db")
def test_orm_repository_creating_item(db):
    item = {"title": "title", "description": "description", "priority": "prioridade"}
    db_item = models.Item(**item)
    db.add(instance=db_item)
    db.commit()
    db.refresh(db_item)

    users = db.query(models.Item).filter(models.Item.title == item["title"])

    assert users.all() == [db_item]
