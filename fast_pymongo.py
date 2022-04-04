### Create MongoDB database with FastAPI

from pydantic import BaseModel
from fastapi import FastAPI, Request, Response, status
from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient() # MongoDB connection
pets_db = client['mydb'] # Create 'pets_db' Database
fish_col = pets_db['people'] # Create 'fish_col' Collection

# Pydantic BaseModel
class Pet(BaseModel):
    id: int
    name: str
    description: str
    price: float

app = FastAPI()

#test
@app.get('/hi/{name}',
         tags = ['test_blog']) # add tags 'test_blog'
def hello_world(name:str):
    return {'message': f'hello {name}'}

# Adding data to 'fish_col' collection
@app.post("/create",
          tags = ['Post'])
def create_pet(pet:Pet): # using BaseModel class
    print(f'method called : {str(pet)}')
    id = fish_col.insert_one(pet.dict()).inserted_id
    print(f'pet added : now db size = {str(id)}')
    return {'id': fish_col.count()}

# Query data from MongoDB by using pet_id
@app.get('/pet/{id}',
         tags = ['Get'])
def read_pet(id:int,
             response:Response): # for response status code
    try:
        print(f'method called: {str(id)}')
        result = fish_col.find_one({'id':id})
        print(result)
        if(result == None):
            response.status_code = status.HTTP_404_NOT_FOUND
            return 'Pet Not Found'
        return str(result)

    except Exception as e:
        print(_e)
        response.status_code = status.HTTP_404_NOT_FOUND
        return 'Pet Not Found'

@app.get('/pet/',status_code = 200)
def read_all_pet(response:Response):
    try:
        print(f'method called: {str(id)}')
        results = fish.collection.find({})
        result_list = []
        for result in results:
            result_list.append(str(result))
        if(results == None):
            response.status_code = status.HTTP_404_NOT_FOUND
            return 'Pets Not Found'

        return str(result_list)

    except Exception as e: # if not found any results
        print(_e)
        response.status_code = status.HTTP_404_NOT_FOUND
        return 'Error Occured'

# @app.put('/update', status_code = 200)
# def update_put(pet:Pet):
#     print(f'method called : {str(pet)}')
#     result = fish_col.update_one({'id':pet.id},{'$set'})
