# Retail Field Reports

Archived JSON payloads from DApp store status updates ( `[RETAIL FIELD REPORT EVENT]` ).

## Source

- **DApp pages:** `store_interaction_history.html`, `stores_nearby.html`
- **Edgar endpoint:** `POST https://edgar.truesight.me/dao/submit_contribution`
- **GAS audit sheet:** "Stores Visits Field Reports" tab in the Telegram compilation workbook

## File naming

```
retail_field_reports/<YYYYMMDDTHHMMSSZ>.json
```

## Schema

Each file is a JSON object:

```json
{
  "received_at": "2026-04-24T11:30:00Z",
  "signature_verification": "success",
  "parsed": {
    "shop_name": "Creative Healing Center",
    "store_key": "creative-healing-center--crystal-boutique...",
    "new_status": "Partnered",
    "previous_status": "Manager Follow-up",
    "shop_type": "Metaphysical/Spiritual",
    "owner_name": "Jane Doe",
    "contact_person": "Jane Doe",
    "email": "jane@example.com",
    "phone": "(555) 123-4567",
    "cell_phone": "(555) 123-4567",
    "website": "https://example.com",
    "instagram": "https://instagram.com/handle",
    "visit_date": "2026-04-24",
    "contact_date": "2026-04-24",
    "follow_up_date": "2026-04-30",
    "contact_method": "In Person",
    "remarks": "Sample dropped, owner interested"
  },
  "raw_text": "[RETAIL FIELD REPORT EVENT]\nShop Name: ..."
}
```

## Oracle visibility

The advisory snapshot generator (`market_research/scripts/generate_advisory_snapshot.py`)
reads the newest files here and surfaces recent store state changes to the Oracle.
