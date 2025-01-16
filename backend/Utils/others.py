# First approach

# pipeline = [
#     {"$match": {"_id": business_id}},
#     {
#         "$lookup": {
#             "from": "TeamPresence",  # Join with team_presence collection
#             "localField": "_id",
#             "foreignField": "BussinessId",
#             "as": "staff_details",
#         }
#     },
#     {
#         "$lookup": {
#             "from": "ServiceInfo",  # Join with service_info collection
#             "localField": "_id",
#             "foreignField": "BussinessId",
#             "as": "services",
#         }
#     },
#     {
#         "$project": {
#             "BussinessId": 1,
#             "business_name": 1,
#             "staff_details": 1,
#             "services": 1,
#         }
#     },
# ]

# cursor = mongodb.db["BusinessDetails"].aggregate(pipeline)

# # Convert the cursor to a list
# result = list(cursor)

# # Ensure the result is JSON serializable
# for doc in result:
#     doc["_id"] = str(doc["_id"])  # Convert ObjectId to string if needed

# return result

