



# class MovieServices:
#     @classmethod
#     def get_movie(cls,form_data,user_info):
#         id=get(form_data,"id")
#         name=get(form_data,"id")

#         _movie=MovieModel.findone({
#             "_id":id,
#             "name":name
#         })
#         if _movie is None:
#             # throw error exception
        
#         return _movie
#     @classmethod
#     def update_movie(cls,form_data,user_info):
#         ##impllement