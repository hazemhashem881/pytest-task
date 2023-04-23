import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from model import Base, engine, Session, Author, Article


class TestBlog:
    def setup_class(self):
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.Session = Session()
        self.valid_author = Author(
            firstname="Ezzeddin",
            lastname="Aybak",
            email="aybak_email@gmail.com"
        )
        self.valid_author2 = Author(
            firstname="hazem",
            lastname="mohamed",
            email="mohamed_email@gmail.com"
        )



    def teardown_class(self):
        self.Session.rollback()
        self.Session.close()

    def test_author_valid(self):
        self.Session.add(self.valid_author)
        self.Session.commit()
        aybak = self.Session.query(Author).filter_by(lastname="Aybak").first()
        assert aybak.firstname == "Ezzeddin"
        assert aybak.lastname != "Abdullah"
        assert aybak.email == "aybak_email@gmail.com"

#test Auther2
    def test_author_valid2(self):
        self.Session.add(self.valid_author2)
        self.Session.commit()
        hazem = self.Session.query(Author).filter_by(lastname="hashem").first()
        assert hazem.firstname == "hazem"
        assert hazem.lastname != "mohamed"
        assert hazem.email == "hazem_email@gmail.com"
    @pytest.mark.xfail(raises=IntegrityError)
    def test_author_no_email(self):
        author = Author(
            firstname="James",
            lastname="Clear"
        )
        self.Session.add(author)
        try:
            self.Session.commit()
        except IntegrityError:
            self.Session.rollback()

    def test_article_valid(self):
        valid_article = Article(
            slug="sample-slug",
            title="Title of the Valid Article",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            author=self.valid_author
            )
        self.Session.add(valid_article)
        self.Session.commit()
        sample_article = self.Session.query(Article).filter_by(slug="sample-slug").first()
        assert sample_article.title == "Title of the Valid Article"
        assert len(sample_article.content.split(" ")) > 50
#------------- test article 4------------------------
    def test_article_valid2(self):
        valid_article = Article(
        slug="DevOps-postgrs",
        title="using tool is called docker to Interacting with Databases using SQLAlchemy with PostgreSQL",
        content="Create docker and docker-compose then create docker-compose pull image latest form postgres and pgadmin then create venv to run pythem",
        author=self.valid_author2
            )
        self.Session.add(valid_article)
        self.Session.commit()
        sample_article = self.Session.query(Article).filter_by(slug="sample-slug").first()
        assert sample_article.title == "Title of the Valid Article"
        assert len(sample_article.content.split(" ")) > 50