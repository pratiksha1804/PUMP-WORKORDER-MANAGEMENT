from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import constant
import json
@swagger.model
class workorderList(Resource):
    @swagger.operation(
        description="workorder list",
        nickname="workorder list",
        parameters=[
            {
                "name": "workorder_name",
                "dataType": "String",
                "description": "workorder details",
                "required": False,
                "allowMultiple": False,
                "paramType": "query"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Wororder details fetched successfully"},
            {"code": 400, "message": "Bad Request: Error on fetching workorder list"}
        ],
    )
    def get(self):
        try:
            workorder_name = request.args.get(constant.WORKORDER_NAME)
            if workorder_name:
                workorders=database.getParticularWorkorder(workorder_name)
            else:
                workorders=database.getWorkorders()
            return make_response(jsonify(
                {
                    "title": "Workorder Details Fetched Successfully",
                    "status": HTTPStatus.OK,
                    "data": workorders,
                }
            ),
                HTTPStatus.OK
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from fetching workorders",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )