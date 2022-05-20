# from flask_app.config.mysqlconnection import connectToMySQL
# from flask import flash


# class Car:
#     db_name = "week_seven_schema_model" #! update this to connect to the correct database 
#     def __init__(self,dealz_data):   #! make your you variable is correct in all your class/static methods 
#         self.id = dealz_data['id']
#         self.price = dealz_data['price']
#         self.model = dealz_data['model']                #! make sure all of the keys are spelled and puncutiaon is the same
#         self.make = dealz_data['make']                    #! as whats in the db, on the htmls templates 
#         self.year = dealz_data['year']
#         self.seller = dealz_data['seller']
#         self.description = dealz_data['description']
#         self.user_id = dealz_data['user_id']  


#! update all queries with correct DB values 

#     @classmethod 
#     def save(cls,data):
#         query = "INSERT INTO cars(price,model,make,year,description,user_id) VALUES (%(price)s,%(model)s,%(make)s,%(year)s,%(description)s,%(user_id)s);"
#         return connectToMySQL(cls.db_name).query_db(query,data)



#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM cars;"
#         results =  connectToMySQL(cls.db_name).query_db(query)
#         all_cars = []
#         for row in results:
#             print(row['model'])
#             all_cars.append(cls(row) )
#         return all_cars


#     @classmethod
#     def get_one(cls,data):
#         query = "SELECT * FROM cars WHERE id = %(id)s;"
#         results = connectToMySQL(cls.db_name).query_db(query,data)
#         return cls( results[0] )

#     @classmethod
#     def update(cls, data):
#         query = "UPDATE cars SET price=%(price)s,name=%(model)s,make=%(make)s, year=%(year)s, description=%(description)s,updated_at=NOW() WHERE id = %(id)s;"
#         return connectToMySQL(cls.db_name).query_db(query,data)
    
#     @classmethod
#     def destroy(cls,data):
#         query = "DELETE FROM cars WHERE id = %(id)s;"
#         return connectToMySQL(cls.db_name).query_db(query,data)

#! ensure your validation is what you want

#     @staticmethod
#     def validate_car(car):
#         is_valid = True
#         if len(car['price']) < 3:
#             is_valid = False
#             flash("Price must be at least 3 characters","car")
#         if len(car['model']) < 3:
#             is_valid = False
#             flash("Model must be at least 3 characters","car")
#         if len(car['make']) < 3:
#             is_valid = False
#             flash("Make must be at least 3 characters","car")
#         if len(car['year']) < 4:                  #! 
#             is_valid = False
#             flash("Year must be at least 4 characters","car")
#         if len(car['description']) < 3:
#             is_valid = False
#             flash("Description must be at least 3 characters","car")
#         return is_valid 