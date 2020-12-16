from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json

# {
#  "company_name":"company_name",
#      "pump_details":{
# "pump type":"xyz type",
# "power":"5mb",
# "cabel":"cabel",
# "used_flag":"false",
# "rate":500,
# "start_date":"12/15/2020",
# "end_date":"12/31/2020"
# },
#      "refered_by":"refered_by",
#    "workorder_photo_url":"workorder_photo_url"
# }

@swagger.model
class workorderCreation(Resource):
    @swagger.operation(
        description="workorder creation",
        nickname="workorder creation",
        parameters=[
            {
                "name": "body",
                "dataType": "string",

                "required": True,
                "allowMultiple": False,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Workorder Created succesfully"},
            {"code": 400, "message": "Bad Request: Error on creating workorder"}
        ],
    )
    def post(self):
        try:
            payload = json.loads(request.data.decode())
            company_name=payload["company_name"]
            pump_details=payload["pump_details"]
            refered_by=payload["refered_by"]
            start_date=pump_details["start_date"]
            end_date=pump_details["end_date"]
            workorder_photo_url=payload["workorder_photo_url"]

            database.addWorkorder(company_name,pump_details,refered_by,start_date,end_date,workorder_photo_url)
            return make_response(jsonify(
                {
                    'title': "Workorder Created Successfully",
                    "status": HTTPStatus.CREATED
                }
            ),
                HTTPStatus.CREATED,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from workorder creation",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )