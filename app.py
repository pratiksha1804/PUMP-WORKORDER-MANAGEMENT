import os
from config import app
from api import api
from api.workorderCreate import workorderCreation
from api.workorderDelete import workorderDeletion
from api.workorderList import workorderList
from api.updateWorkorder import workorderUpdate

api.add_resource(workorderCreation,"/api/workorderCreate")
api.add_resource(workorderDeletion,"/api/workorderDelete")
api.add_resource(workorderList,"/api/get_all_workorders")
api.add_resource(workorderUpdate,"/api/update_workorder")

if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5003, debug=True)