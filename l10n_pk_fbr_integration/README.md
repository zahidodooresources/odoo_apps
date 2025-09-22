# l10n_pk_fbr_integration

Integrates Odoo 18 invoices with FBR Digital Invoicing (DI) APIs.

## Install
1. Place folder in Odoo addons path.
2. Restart Odoo server.
3. Update Apps list and install `Pakistan FBR Digital Invoicing`.

## Configure
- Go to Settings → FBR Digital Invoicing (Settings) and set:
  - FBR DI API URL (sandbox or production)
  - API Key and Secret
  - Sandbox mode
  - FBR Cookie String : if applicable
  - New addition of fields in product (HS Code, HS Unit of Measure)

## Usage
- Edit an invoice (Draft): you can call it by auto with invoice onchange. a light-weight tax estimate attempt will run when lines change (non-blocking).
- Use the **Sync with FBR** button to send full invoice to FBR; the response will populate FBR Invoice No and status.

## Important
- This module demonstrates the integration pattern. Adapt endpoints, signing, and JSON payload exactly as required by FBR technical documentation. See FBR DI technical spec. :contentReference[oaicite:2]{index=2}
