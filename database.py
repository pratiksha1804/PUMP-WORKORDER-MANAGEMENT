from config import app
from config import mongo
import datetime

def addWorkorder(company_name, pump_details, refered_by, start_date, end_date, workorder_photo_url):
    date=datetime.datetime.now()
    workorder_name=company_name + "_" + str(date)

    workorder_info={
    "workorder_name":workorder_name,
     "company_name":company_name,
     "pump_details":pump_details,
     "refered_by":refered_by,
     "start_date":start_date,
     "end_date":end_date,
     "workorder_photo_url":workorder_photo_url
    }
    return mongo.db.PUMP_WORKORDER_INVENTORY.insert_one(workorder_info)

def deleteWorkorder(workorder_name):
    workorder_info={
        "workorder_name":workorder_name
    }
    return mongo.db.PUMP_WORKORDER_INVENTORY.delete_one(workorder_info)

def getWorkorders():
    workorders = mongo.db.PUMP_WORKORDER_INVENTORY.find({}, {'_id': False})
    wo_list = []
    if workorders:
        for wo in workorders:
            wo_list.append(wo)
        return wo_list
    return None

def getParticularWorkorder(workorder_name):
    workorders = mongo.db.PUMP_WORKORDER_INVENTORY.find_one({"workorder_name":workorder_name}, {'_id': False})
    if workorders:
        return workorders
    return None

def updateWorkorder(workorder_name,company_name, pump_details, refered_by, start_date, end_date, workorder_photo_url):
        my_query = {"workorder_name": workorder_name}
        new_values = {"$set": {"company_name":company_name,"pump_details":pump_details,"refered_by":refered_by
                               ,"start_date":start_date,"end_date":end_date,"workorder_photo_url":workorder_photo_url}}
        return mongo.db.PUMP_WORKORDER_INVENTORY.update(my_query, new_values)