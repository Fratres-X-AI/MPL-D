# Security Policy — MPL-D

**Maturity:** Stub. No production deployment exists.

## Reporting

If you discover sensitive prototype data exposed outside authorized channels,
contact Fratres X AI project leadership directly. Do not post exploit details
in public forums.

## Repository hygiene

- Never commit `.env`, API keys, LSO credentials, or procurement account data.
- Large binary captures (bench imagery with geolocation, raw sensor IDs) belong
  outside the repo unless redacted and approved.
- Laser bench logs may contain facility identifiers — treat as sensitive.

## Laser safety (operational)

This is not a software CVE process. Energizing laser hardware without an
assigned LSO and approved SOP is a safety incident, not a GitHub security issue.

## Export control

Hardware specifications, measured dazzle thresholds, and integration data with
foreign platforms may require compliance review before sharing.
