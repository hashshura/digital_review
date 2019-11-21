import json

from odoo import http
from odoo.http import Response, request


def strip_dict(d):
    d.pop('display_name', None)
    d.pop('create_uid', None)
    d.pop('create_date', None)
    d.pop('write_uid', None)
    d.pop('write_date', None)
    d.pop('__last_update', None)
    return d


def serialize_to_dict(obj):
    d = obj.__dict__
    return strip_dict(d)


class UserController(http.Controller):
    base_url = '/api/users'
    model_name = 'digital_review.user'

    @http.route('/auth', auth='public', csrf=False, cors='*')
    def auth(self, **kw):
        user_id = request.httprequest.cookies.get('user', '-1')
        result = http.request.env[self.model_name].search(
            [['id', '=', user_id]])
        return json.dumps([strip_dict(x.read()[0]) for x in result], indent=4)

    @http.route('/login', auth='public', csrf=False, cors='*')
    def login(self, **kw):
        params = [[k, '=', kw[k]] for k in kw.keys()]
        result = http.request.env[self.model_name].search(params)
        data = {'success': False}
        cookies = {}

        try:
            if len(result):
                data = {'success': True}
                cookies = {'user': str(result[0].id)}
                response = Response(data)
                for k, v in cookies.items():
                    response.set_cookie(k, v)
                return response
        except Exception:
            pass
        return 'failed'

    @http.route('/logout', auth='public', csrf=False, cors='*')
    def logout(self, **kw):
        response = Response({})
        response.set_cookie('user', '')
        return response

    @http.route(base_url, type='json', methods=['POST'], auth='public', csrf=False, cors='*')
    def create(self, **kw):
        result = http.request.env[self.model_name].create(http.request.params)
        return strip_dict(result[0].read()[0])

    @http.route(base_url, auth='public', csrf=False, cors='*')
    def search(self, **kw):
        params = [[k, '=', kw[k]] for k in kw.keys()]
        result = http.request.env[self.model_name].search(params)
        return json.dumps([strip_dict(x.read()[0]) for x in result], indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['DELETE'], auth='public', csrf=False, cors='*')
    def unlink(self, obj, **kw):
        result = obj.unlink()
        return str(result)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['GET'], auth='public', csrf=False, cors='*')
    def read(self, obj, **kw):
        result = obj.read()
        return json.dumps(strip_dict(result[0]), indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), type='json', methods=['PATCH'], auth='public', csrf=False, cors='*')
    def write(self, obj, **kw):
        result = obj.write(http.request.params)
        return str(result)


class VoucherController(http.Controller):
    base_url = '/api/vouchers'
    model_name = 'digital_review.voucher'

    @http.route(base_url, type='json', methods=['POST'], auth='public', csrf=False, cors='*')
    def create(self, **kw):
        result = http.request.env[self.model_name].create(http.request.params)
        return strip_dict(result[0].read()[0])

    @http.route(base_url, auth='public', csrf=False, cors='*')
    def search(self, **kw):
        params = [[k, '=', kw[k]] for k in kw.keys()]
        result = http.request.env[self.model_name].search(params)
        return json.dumps([strip_dict(x.read()[0]) for x in result], indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['DELETE'], auth='public', csrf=False, cors='*')
    def unlink(self, obj, **kw):
        result = obj.unlink()
        return str(result)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['GET'], auth='public', csrf=False, cors='*')
    def read(self, obj, **kw):
        result = obj.read()
        return json.dumps(strip_dict(result[0]), indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), type='json', methods=['PATCH'], auth='public', csrf=False, cors='*')
    def write(self, obj, **kw):
        result = obj.write(http.request.params)
        return str(result)


class MenuController(http.Controller):
    base_url = '/api/menus'
    model_name = 'digital_review.menu'

    @http.route('/entahlah/hehe', auth='public')
    def index(self, **kw):
        return "Hello, world baru lagiii"

    @http.route(base_url, type='json', methods=['POST'], auth='public', csrf=False, cors='*')
    def create(self, **kw):
        result = http.request.env[self.model_name].create(http.request.params)
        return strip_dict(result[0].read()[0])

    @http.route(base_url, auth='public', csrf=False, cors='*')
    def search(self, **kw):
        params = [[k, '=', kw[k]] for k in kw.keys()]
        result = http.request.env[self.model_name].search(params)
        return json.dumps([strip_dict(x.read()[0]) for x in result], indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['DELETE'], auth='public', csrf=False, cors='*')
    def unlink(self, obj, **kw):
        result = obj.unlink()
        return str(result)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['GET'], auth='public', csrf=False, cors='*')
    def read(self, obj, **kw):
        result = obj.read()
        return json.dumps(strip_dict(result[0]), indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), type='json', methods=['PATCH'], auth='public', csrf=False, cors='*')
    def write(self, obj, **kw):
        result = obj.write(http.request.params)
        return str(result)


class TransactionController(http.Controller):
    base_url = '/api/transactions'
    model_name = 'digital_review.transaction'

    @http.route(base_url, type='json', methods=['POST'], auth='public', csrf=False, cors='*')
    def create(self, **kw):
        result = http.request.env[self.model_name].create(http.request.params)
        return strip_dict(result[0].read()[0])

    @http.route(base_url, auth='public', csrf=False, cors='*')
    def search(self, **kw):
        params = [[k, '=', kw[k]] for k in kw.keys()]
        result = http.request.env[self.model_name].search(params)
        return json.dumps([strip_dict(x.read()[0]) for x in result], indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['DELETE'], auth='public', csrf=False, cors='*')
    def unlink(self, obj, **kw):
        result = obj.unlink()
        return str(result)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['GET'], auth='public', csrf=False, cors='*')
    def read(self, obj, **kw):
        result = obj.read()
        return json.dumps(strip_dict(result[0]), indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), type='json', methods=['PATCH'], auth='public', csrf=False, cors='*')
    def write(self, obj, **kw):
        result = obj.write(http.request.params)
        return str(result)


class QuestionController(http.Controller):
    base_url = '/api/questions'
    model_name = 'digital_review.question'

    @http.route(base_url, type='json', methods=['POST'], auth='public', csrf=False, cors='*')
    def create(self, **kw):
        result = http.request.env[self.model_name].create(http.request.params)
        return strip_dict(result[0].read()[0])

    @http.route(base_url, auth='public', csrf=False, cors='*')
    def search(self, **kw):
        params = [[k, '=', kw[k]] for k in kw.keys()]
        result = http.request.env[self.model_name].search(params)
        return json.dumps([strip_dict(x.read()[0]) for x in result], indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['DELETE'], auth='public', csrf=False, cors='*')
    def unlink(self, obj, **kw):
        result = obj.unlink()
        return str(result)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['GET'], auth='public', csrf=False, cors='*')
    def read(self, obj, **kw):
        result = obj.read()
        return json.dumps(strip_dict(result[0]), indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), type='json', methods=['PATCH'], auth='public', csrf=False, cors='*')
    def write(self, obj, **kw):
        result = obj.write(http.request.params)
        return str(result)


class AnswerController(http.Controller):
    base_url = '/api/answers'
    model_name = 'digital_review.answer'

    @http.route(base_url, type='json', methods=['POST'], auth='public', csrf=False, cors='*')
    def create(self, **kw):
        result = http.request.env[self.model_name].create(http.request.params)
        return strip_dict(result[0].read()[0])

    @http.route(base_url, auth='public', csrf=False, cors='*')
    def search(self, **kw):
        params = [[k, '=', kw[k]] for k in kw.keys()]
        result = http.request.env[self.model_name].search(params)
        return json.dumps([strip_dict(x.read()[0]) for x in result], indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['DELETE'], auth='public', csrf=False, cors='*')
    def unlink(self, obj, **kw):
        result = obj.unlink()
        return str(result)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['GET'], auth='public', csrf=False, cors='*')
    def read(self, obj, **kw):
        result = obj.read()
        return json.dumps(strip_dict(result[0]), indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), type='json', methods=['PATCH'], auth='public', csrf=False, cors='*')
    def write(self, obj, **kw):
        result = obj.write(http.request.params)
        return str(result)


class ReviewController(http.Controller):
    base_url = '/api/reviews'
    model_name = 'digital_review.review'

    @http.route(base_url, type='json', methods=['POST'], auth='public', csrf=False, cors='*')
    def create(self, **kw):
        result = http.request.env[self.model_name].create(http.request.params)
        return strip_dict(result[0].read()[0])

    @http.route(base_url, auth='public', csrf=False, cors='*')
    def search(self, **kw):
        params = [[k, '=', kw[k]] for k in kw.keys()]
        result = http.request.env[self.model_name].search(params)
        return json.dumps([strip_dict(x.read()[0]) for x in result], indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['DELETE'], auth='public', csrf=False, cors='*')
    def unlink(self, obj, **kw):
        result = obj.unlink()
        return str(result)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), methods=['GET'], auth='public', csrf=False, cors='*')
    def read(self, obj, **kw):
        result = obj.read()
        return json.dumps(strip_dict(result[0]), indent=4)

    @http.route('{}/<model("{}"):obj>'.format(base_url, model_name), type='json', methods=['PATCH'], auth='public', csrf=False, cors='*')
    def write(self, obj, **kw):
        result = obj.write(http.request.params)
        return str(result)
