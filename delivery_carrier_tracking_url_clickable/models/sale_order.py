from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    tracking_url_clickable = fields.Html(
        string="Tracking URL", compute="_compute_tracking_url_clickable", sanitize=False
    )

    @api.depends(
        "picking_ids.carrier_tracking_ref", "picking_ids.carrier_id.default_tracking_url"
    )
    def _compute_tracking_url_clickable(self):
        # TODO: This can be simplified
        for order in self:
            links = []
            for picking in order.picking_ids:
                base_url = picking.carrier_id.default_tracking_url
                if base_url and picking.carrier_tracking_ref:
                    refs = picking.carrier_tracking_ref.split("+")
                    for ref in refs:
                        tracking_number = ref.strip()
                        full_url = f"{base_url}{tracking_number}"
                        links.append(
                            f'<a href="{full_url}" target="_blank">{ref.strip()}</a>'
                        )
            order.tracking_url_clickable = "<br/>".join(links) if links else False
