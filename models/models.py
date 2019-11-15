# -*- coding: utf-8 -*-

from odoo import models, fields, api


class User(models.Model):
    _name = 'digital_review.user'

    name = fields.Char()
    profile_url = fields.Char()
    email = fields.Char()
    password = fields.Char()
    phone_number = fields.Char()
    point = fields.Integer()

    vouchers = fields.Many2many('digital_review.voucher',
                                string="Owned Vouchers", index=True)


class Voucher(models.Model):
    _name = 'digital_review.voucher'

    title = fields.Char()
    point = fields.Integer()
    description = fields.Char()


class Menu(models.Model):
    _name = 'digital_review.menu'

    name = fields.Char()
    picture_url = fields.Char()
    description = fields.Char()

    reviews = fields.One2many('digital_review.review', 'menu',
                              string="Reviews", index=True)


class Transaction(models.Model):
    _name = 'digital_review.transaction'

    name = fields.Char()
    picture_url = fields.Char()
    description = fields.Char()

    menus = fields.Many2many('digital_review.menu',
                             string="Purchased Items", index=True)


class Question(models.Model):
    _name = 'digital_review.question'

    title = fields.Char()
    answers = fields.One2many('digital_review.answer', 'question',
                              string="Answers", index=True)


class Answer(models.Model):
    _name = 'digital_review.answer'

    rating = fields.Integer()
    comment = fields.Char()

    transaction = fields.Many2one('digital_review.transaction',
                                  string="Transaction", index=True)
    question = fields.Many2one('digital_review.question',
                               string="Question", index=True)
    user = fields.Many2one('digital_review.user',
                           string="User", index=True)


class Review(models.Model):
    _name = 'digital_review.review'

    rating = fields.Integer()
    comment = fields.Char()

    transaction = fields.Many2one('digital_review.transaction',
                                  string="Transaction", index=True)
    menu = fields.Many2one('digital_review.menu',
                           string="Menu", index=True)
    user = fields.Many2one('digital_review.user',
                           string="User", index=True)
