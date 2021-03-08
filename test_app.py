import  os
import unittest
import  json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

Assistant = {
    'Content-Type': 'application/json',
    'Authorization': os.environ['Assistant_jwt']
    }

Director = {
    'Content-Type': 'application/json',
    'Authorization': os.environ['Director_jwt']
    }

Producer = {
    'Content-Type': 'application/json',
    'Authorization': os.environ['Producer_jwt']
    }
    
class capstontest(unittest.TestCase):
    """This class represents the trivia test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass    

        # successful Get
    def test_get_actors(self):
        res = self.client().get('/actors', headers=Director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_movies(self):
        res = self.client().get('/movies',headers=Assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Unsuccessful Get
    def invaild_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "method not allowed")

    def invaild_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "method not allowed")    

    # successful Post
    def test_create_new_actors(self):
        res = self.client().post('/actors',headers=Producer,json={"name": "Rasha","age": "20","gender": "Fmale"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['created_id'], 27)  

    def test_create_new_movies(self):
        res = self.client().post('/movies',headers=Producer,json={ "release_date": "Mon, 26 Oct 2020 00:00:00 GMT","title": "BoyzBeforFlower1"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['created_id'], 20) 

    # Unsuccessful Post
    def invaild_post_actors(self):
        res = self.client().post('/actors', json={ "title": "Sara", "age": "22","gender":"fmale"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable') 

    def invaild_post_movies(self):
        res = self.client().post('/movies', json={"release_date": "Mon, 26 Oct 2020 00:00:00 GMT","title": "BoyzBeforFlower"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')        

    # successful Patch

    def test_patch_actors(self):
        res = self.client().patch('/actors/1',headers=Producer,json={"gender": "male"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_patch_movies(self):
        res = self.client().patch('/movies/3',headers=Producer, json={"title": "IntoStorm"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # Unsuccessful Patch 

    def invaild_patch_actors(self):
        res = self.client().patch('/actors/1', json={"name": "Sara","age": "22","gender": "Fmale"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 402)

    def invaild_patch_movies(self):
        res = self.client().patch('/movies/1', json={"title": "The Dark"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 402)
    
           
    # successful Delete
    def test_delete_actors(self):
        res = self.client().delete('/actors/25',headers=Producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_id'],25)

    def test_delete_movies(self):
        res = self.client().delete('/movies/18',headers=Producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted_id'],18)

    # Unsuccessful Delete     

    def invaild_delete_actors(self):
        res = self.client().delete('/actors/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "unauthorized")

    def invaild_delete_movies(self):
        res = self.client().delete('/movies/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "unauthorized")
           
    # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()