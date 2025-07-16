from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    tracking_url_clickable = fields.Html(
        string="Tracking URL", compute="_compute_tracking_url_clickable", sanitize=False
    )

    @api.depends("carrier_id.default_tracking_url", "carrier_tracking_ref")
    def _compute_tracking_url_clickable(self):
        for picking in self:
            base_url = picking.carrier_id.default_tracking_url
            if not base_url or not picking.carrier_tracking_ref:
                picking.tracking_url_clickable = False
                continue

            links = []
            tracking_refs = picking.carrier_tracking_ref.split("+")
            for ref in tracking_refs:
                tracking_number = ref.strip()
                full_url = f"{base_url}{tracking_number}"
                links.append(f'<a href="{full_url}" target="_blank">{tracking_number}</a>')
            picking.tracking_url_clickable = "<br/>".join(links)
