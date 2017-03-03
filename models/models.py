# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class sale_order(models.Model):
    _inherit = "sale.order"

    #x_so_note = fields.Char(string = "new note")

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(sale_order, self)._prepare_invoice()
        invoice_vals['x_inv_note'] = self.x_so_note
        return invoice_vals

class account_invoice(models.Model):
    _inherit = "account.invoice"

    #x_inv_note = fields.Char(string="new note")

class sale_advance_payment_inv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        invoice = super(sale_advance_payment_inv, self)._create_invoice(order, so_line, amount)
        invoice.x_inv_note = order.x_so_note

