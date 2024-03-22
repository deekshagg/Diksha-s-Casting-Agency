import unittest
from api import create_app
from database.models import setup_db
from settings import DB_PASSWORD, DB_URI, DB_USER


class AgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(active=False)
        self.client = self.app.test_client
        self.database_name = 'postgres'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(
            DB_USER, DB_PASSWORD, DB_URI, self.database_name)
        setup_db(self.app, self.database_path)
        self.token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtlQUFSRHFySWhWVzg1UDNvYTNIaCJ9.eyJpc3MiOiJodHRwczovL2RlZWtzaGFnZy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjVmODgxYWM4OTIzMGQ4MzkwN2I5N2UxIiwiYXVkIjoiY2FzdGluZy1hZ2VuY3ktc2VydmljZSIsImlhdCI6MTcxMTEzOTQ1MCwiZXhwIjoxNzExMjI1ODUwLCJzY29wZSI6IiIsImF6cCI6IktxaFNQVmlqSzFxUHRJdlZBYVJaZ2s3SnlRQmVyM3ZqIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.ph5TiHlAQ2nVS_6KLmaESXeeWmS2sENnbApUoo7KS7RZ5wZGaSQaMXEh3AAST3At0SDo3G6av9ppNLrccV_pezMP0jy6hR4D9HVPL7fUJgHDAXUyLD8bEFhAp-b9OWGAdZtSB-x9N51maIYSmq_AYVDjM_83LrrcY-5OohgkGM_gwuy8v5q_Zg4YKPgnk0iWoB6Nmh3FFcv4l52PB4M-meQfbB9CC2cPBuUXKDAVxYkH2FsdeFqT420NjJQgrYNfTKSV3HuJn-Ck4oMRUMbZg4pZEw9dBVuaSNnDRRqlj6l_q2kWkwQsl5mA1XtCs6uYbeFpjkGWAVRfBb2QtZSStg'

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

        self.new_movie = {
            "title": "Udacity",
            "release_date": "2024-03-23"
        }

        self.new_actor = {
            "name": "Diksha Aggarwal",
            "age": 26,
            "gender": "Female"
        }

        
        self.movie_id_del = 1
        
        self.actor_id_del = 1

        self.updated_movie_data = {
            "title": "Updated Movie Title",
            "release_date": "2022-01-01"
        }

        self.updated_actor_data = {
            "name": "Updated Actor Name",
            "age": 40,
            "gender": "Female"
        }

    def tearDown(self):
        # with self.app.app_context():
        #     db.drop_all()
        pass

    def test_get_movies_without_authentication(self):
        response = self.client().get('/movies')
        print(response)

        self.assertEqual(response.status_code, 401)

    def test_get_movies_with_authentication(self):
        response = self.client().get('/movies', headers=self.headers)
        print(response)

        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_post_movies_with_authentication(self):
        response = self.client().post(
            '/movies', json=self.new_movie, headers=self.headers)
        print(response)

        self.assertEqual(response.status_code, 201)

    def test_update_movie(self):
        movie_id = 3
        response = self.client().patch(
            f'/movies/{movie_id}', json=self.updated_movie_data, headers=self.headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])

    def test_delete_movie(self):

        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        response = self.client().delete(
            f'/movies/{self.movie_id_del}', headers=headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])

    # ----------------actors-------------------#

    def test_get_actors_without_authentication(self):
        response = self.client().get('/actors')
        print(response)

        self.assertEqual(response.status_code, 401)

    def test_get_actors_with_authentication(self):
        response = self.client().get('/actors', headers=self.headers)
        print(response)

        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_post_actors_with_authentication(self):

        response = self.client().post(
            '/actors', json=self.new_actor, headers=self.headers)
        print(response)

        self.assertEqual(response.status_code, 201)

    def test_update_actor(self):
        actor_id = 2
        response = self.client().patch(
            f'/actors/{actor_id}', json=self.updated_actor_data, headers=self.headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])

    def test_delete_actor(self):

        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        response = self.client().delete(
            f'/actors/{self.actor_id_del}', headers=headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])


if __name__ == "__main__":
    unittest.main(exit=False)
