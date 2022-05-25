from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user #! added this after talking to aaron 


class Show:
    db_name = "users_belt_schema_three" #! update this to connect to the correct database 
    def __init__(self,show_data):   #! release_date your you variable is correct in all your class/static methods 
        self.id = show_data['id']
        self.title = show_data['title']
        self.network = show_data['network']                #! release_date sure all of the keys are spelled and puncutiaon is the same
        self.release_date = show_data['release_date']                    #! as whats in the db, on the htmls templates 
        self.description = show_data['description']
        self.user_id = show_data['user_id']  
        # self.user = []  #* placeholder holder holding many movies   the [] would be replaced with none if you are linking only one user to one show 
        self.user = None   #* can be overridden if their is an instance of a name??



    @classmethod 
    def save(cls,data):
        query = "INSERT INTO shows(title,network,release_date,description,user_id) VALUES (%(title)s,%(network)s,%(release_date)s,%(description)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_shows = []
        for row in results:
            print(row['title'])
            all_shows.append(cls(row) )
        return all_shows


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )


    @classmethod  #*says with user but its really getting the person who created it, not the user
    def get_one_show_with_user(cls,data):
        query = "SELECT * FROM shows LEFT JOIN users ON shows.user_id = users.id WHERE shows.id =%(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print('printing results',results[0])
        print('*************************')
        this_show = cls(results[0]) 
        user_data=results[0] 
        user_created= {
            'id': user_data['users.id'],  
            'first_name': user_data['first_name'],    
            'last_name': user_data['last_name'],
            'email' :user_data['email'],
            'password' : user_data['password'],
            'confirm_password': user_data['confirm_password'],
            'created_at': user_data['users.created_at'],
            'updated_at': user_data['users.updated_at']

        }
        this_show.user = user.User(user_created)
        # return cls(results[0]) #* this is what I originally had to return out of my code 
        return this_show


    @classmethod
    def update(cls, data):
        query = "UPDATE shows SET title=%(title)s,network=%(network)s,release_date=%(release_date)s, description=%(description)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)


    @staticmethod
    def validate_show(show):
        is_valid = True
        if len(show['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters","show")
        if len(show['network']) < 3:
            is_valid = False
            flash("Network must be at least 3 characters","show")
        if len(show['release_date']) < 3:
            is_valid = False
            flash("Release date must be at least 3 characters","show")
        if len(show['description']) < 4:                   
            is_valid = False
            flash("Description must be at least 4 characters","show")
        return is_valid 



#! this is from a print statement that printed results for me to understnad what was happening 
# {
# 'id': 4, 'title': 'Lost', 
# 'network': 'ABC ', 
# 'release_date': datetime.date(2000, 1, 1),
# 'description': 'tttdfafdfad',
# 'created_at': datetime.datetime(2022, 5, 20, 15, 26, 44),
# 'updated_at': datetime.datetime(2022, 5, 24, 9, 12), 
# 'user_id': 3, 
# 'users.id': 3,
# 'first_name': 'Hagen ', 
# 'last_name': 'Fulford',
# 'email': 'h@gmail.com', 
# 'password': '$2b$12$7EvEK/DyS3bRxlh82jVzvu6Kuz5Q6hDpvSCQuqfWroe.X4NjhipQa',
# 'confirm_password': None, 
# 'users.created_at': datetime.datetime(2022, 5, 20, 15, 1, 15),
# 'users.updated_at': datetime.datetime(2022, 5, 20, 15, 1, 15)
# }