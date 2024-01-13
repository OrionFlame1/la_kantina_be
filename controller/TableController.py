from flask import jsonify, Response

from controller.service.TableService import TableService


class TableController:

    def getTables(date, appSession, isAdmin):
        if 'user_id' in appSession:
            return jsonify(TableService.getTables(date, isAdmin))
        else:
            return Response(status=401)