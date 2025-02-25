from odoo import models, fields

class FatturapaRelatedDocumentTypeInherit(models.Model):
    _inherit = "fatturapa.related_document_type"

  # Sovrascrittura completa del campo type con tutte le opzioni
    type = fields.Selection([
        ('order', 'Determina'),  # Modificata solo l'etichetta di 'order'
        ("contract", "Contract"),
        ("agreement", "Agreement"),
        ("reception", "Reception"),
        ("invoice", "Related Invoice"),
    ], string='Document Type', required=True)
