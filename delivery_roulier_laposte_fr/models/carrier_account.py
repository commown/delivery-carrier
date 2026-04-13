# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CarrierAccount(models.Model):
    _inherit = "carrier.account"

    laposte_fr_file_format = fields.Selection(
        [("PDF_10x15_300dpi", "PDF 10x15 300dpi"),
         ("PDF_10x12_300dpi", "PDF 10x12 300dpi"),
         ("PDF_A4_300dpi", "PDF A4 300dpi")], 
        default="PDF_10x15_300dpi", string="Label format"
    )
