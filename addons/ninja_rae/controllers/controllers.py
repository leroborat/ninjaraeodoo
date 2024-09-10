# -*- coding: utf-8 -*-
# from odoo import http


# class NinjaRae(http.Controller):
#     @http.route('/ninja_rae/ninja_rae', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ninja_rae/ninja_rae/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ninja_rae.listing', {
#             'root': '/ninja_rae/ninja_rae',
#             'objects': http.request.env['ninja_rae.ninja_rae'].search([]),
#         })

#     @http.route('/ninja_rae/ninja_rae/objects/<model("ninja_rae.ninja_rae"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ninja_rae.object', {
#             'object': obj
#         })

