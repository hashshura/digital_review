# Digital Review & Reward (`digital_review`)

**Digital Review & Reward** is an IF3141 Information System solution approach utilizing Odoo as a service.

Author: **Lelah Tubes**

## Installation

Assuming you are using Windows 10 as your primary operating system,

1. Install [Odoo](https://www.odoo.com/id_ID/page/download).

2. Go to your Odoo addons folder, for example using a Run-As-Administrator terminal:

```bash
cd/d C:\Program Files (x86)\Odoo 13.0\server\odoo\addons
```

3. Clone this repository.

```bash
git clone git@github.com:hashshura/digital_review.git
```

4. Update and install your Odoo apps list via debug: http://localhost:8069/web?debug=1.

## Updating the Module

After each update of the module,

1. Go to **Updates - Odoo** and update all of the modules.

2. Restart the server via **Windows > Services > odoo-server-13.0**.

## CRUD API Endpoints

Every URL endpoint is formatted as `/api/<model>s`.

For example, Voucher model API endpoint will be http://localhost:8069/api/vouchers.

To show response body, please call below requests.

### `POST` `/api/<model>s` - creates new object

Use header as `Content-Type: application/json`.

Request body should be in `{"params": fields}` format. For example, Voucher endpoint body:

```json
{
  "params":
    {
      "title": "Gudshit",
      "point": 100,
      "description": "This shit is gud"
    }
}
```

### `PATCH` `/api/<model>s/<id>` - patches object data with specific object id

Use header as `Content-Type: application/json`.

Request body should be in `{"params": fields}` format. For example, Voucher endpoint body:

```json
{
  "params":
    {
      "description": "Update this shit"
    }
}
```

### `GET` `/api/<model>s` - returns all defined objects

### `GET` `/api/<model>s/<id>` - returns object with specific id

### `DELETE` `/api/<model>s/<id>` - deletes object with specific id

