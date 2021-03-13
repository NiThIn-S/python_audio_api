#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from flask import jsonify
from flask import request
from flask_restful import Api, Resource
import datetime
import validater


# In[2]:


app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

def success():
    """ Displaying Success message."""
    return "200 OK"

@app.errorhandler(404)
def not_found(e): 
    """Changing 404 not found to 400 Bad request"""
    return "400 Bad request"

@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return "400 Bad request"

@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return "500 Internel Server error"


# In[3]:


@app.route('/<string:audiofiletype>/<int:_id>/get',methods=['GET'])
def get_a_file(audiofiletype,_id):
    """
    Get a single file using the id given.
    """
    aud = mongo.db[audiofiletype]
    output = aud.find_one(_id)
    return jsonify(output)

@app.route('/<string:audiofiletype>',methods=['GET']) 
def get_all_files(audiofiletype):
    """
    Get all audio files of the mentioned type.
    This function uses dictionary to retrieve the common data
    irrespective of the Audiofiletype. Then updates the dictionary 
    with the data specific to it's type.
    
    """
    aud = mongo.db[audiofiletype]
    output = []
    for c in aud.find():
        dict1 = dict()
        dict1.update({'id':c['_id'],
                      'Duration_in_seconds':c['Duration_in_seconds'],
                      'uploaded_time':c['uploaded_time']})
        
        if(audiofiletype.lower()=='song'):
            dict1.update({"name_of_the_song":c['name_of_the_song']})

        elif(audiofiletype.lower()=='podcast'):
            dict1.update({'name_of_the_podcast':c['name_of_the_podcast'],
                           'host':c['host'],
                           'participants':c['participants']
                           })
        elif(audiofiletype.lower()=='audiobook'):
            dict1.update({'title_of_the_audiobook':c['title_of_the_audiobook'],
                           'author_of_title':c['author_of_title'],
                           'narrator':c['narrator']
                           })
        else:
            return bad_request()
        
        output.append(dict1)
        
    return jsonify({'result' : output})


# In[4]:


@app.route('/<string:audiofiletype>/<int:_id>/delete',methods=['GET','POST'])
def delete_a_file(audiofiletype,_id):
    """
    Deleting a file using the id.
    """
    if(type(mongo.db[audiofiletype].find_one(_id)) != dict):
        return bad_request()
    else:
        try:
            mongo.db[audiofiletype].delete_one({"_id":_id})
            return success()
        except:
            return server_error()


# In[5]:


@app.route('/<string:audiofiletype>/create', methods = ['GET','POST'])
def insert_a_file(audiofiletype):
    """
    Creating a new file based on the information given.
    """
    meta = validater.get_meta(request,audiofiletype)
    if(-1 in meta.values()):
        return bad_request()
    else:
        try:
            mongo.db[audiofiletype].insert_one(meta)
            return success()
        except:
            return bad_request()


# In[6]:


@app.route('/<string:audiofiletype>/<int:_id>/update', methods = ['GET','POST'])
def update_a_file(audiofiletype,_id):
    """
    Updating an existing file using its id.
    """
    if(type(mongo.db[audiofiletype].find_one(_id)) != dict):
        return bad_request()
    else:
        myquery = { "_id": int(_id) }
        meta = validater.get_meta(request,audiofiletype,id1=True)
        newvalues = { "$set": meta }
        if(-1 in meta.values()):
            return bad_request()
        else:
            try:
                mongo.db[audiofiletype].update_one(myquery,newvalues)
                return success()
            except:
                return server_error()


# #### Running the application

# In[7]:


if __name__ == "__main__":
    
    # Initializing MongoDB if its not already present in the server.
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mydb["song"]
    mydb["podcast"]
    mydb["audiobook"]
    
    # Running the application
    app.run(debug=False,port=9000)


# In[ ]:




