# -*- coding: utf-8 -*-
from odoo import http


class DigitalReview(http.Controller):
    @http.route('/digital_review/digital_review/', auth='public')
    def index(self, **kw):
        return "Hello, za warudo!"

    @http.route('/digital_review/digital_review/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('digital_review.listing', {
            'root': '/digital_review/digital_review',
            'objects': http.request.env['digital_review.digital_review'].search([]),
        })

    @http.route('/digital_review/digital_review/objects/<model("digital_review.digital_review"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('digital_review.object', {
            'object': obj
        })
