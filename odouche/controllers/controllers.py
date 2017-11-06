# -*- coding: utf-8 -*-
from odoo import http

class Odouche(http.Controller):
    @http.route('/test', auth='public')
    def index(self, **kw):
        return "Tu peux pas test"

    @http.route('/odouche/odouche/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/odouche/odouche/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('odouche.listing', {
            'root': '/odouche/odouche',
            'objects': http.request.env['odouche.odouche'].search([]),
        })

    @http.route('/odouche/odouche/objects/<model("odouche.odouche"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('odouche.object', {
            'object': obj
        })
