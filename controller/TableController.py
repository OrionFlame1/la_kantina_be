from flask import jsonify, Response

from controller.service.TableService import TableService


class TableController:

    def getTables(date, appSession):
        if 'user_id' in appSession:
            return jsonify(TableService.getTables(date))
        else:
            return Response(status=401)