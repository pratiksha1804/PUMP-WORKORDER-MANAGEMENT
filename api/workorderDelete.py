from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
@swagger.model
class workorderDeletion(Resource):
    @swagger.operation(
        description="workorder deletion",
        nickname="workorder deletion",
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
            {"code": 200, "message": "Workorder deleted succesfully"},
            {"code": 400, "message": "Bad Request: Error on deleting workorder"}
        ],
    )
    def delete(self):
        try:
            payload = json.loads(request.data.decode())
            workorder_name=payload["workorder_name"]

            database.deleteWorkorder(workorder_name)
            return make_response(jsonify(
                {
                    'title': "Workorder Deleted Successfully",
                    "status": HTTPStatus.OK
                }
            ),
                HTTPStatus.OK,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from workorder deletion",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )