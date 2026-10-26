# Security fix — privilege escalation via the profile form

**Severity:** Critical (broken access control / privilege escalation — CWE-269, CWE-915)

## The defect
`ProfileForm` (in `market/forms.py`) exposed Django's `is_staff` flag as an editable field,
labeled "Show my name on the department board." Any logged-in user could submit the profile form
with that checkbox ticked and promote their own account to staff. `is_staff` gates the confidential
`/desk/` page and the Django admin, so this let an ordinary user read internal department info and
reach `/admin/` with one request.

## Trigger
Logged in as any user → `/profile/` → tick "Show my name on the department board" → Save.
The account's `is_staff` becomes `True`; `/desk/` and `/admin/` open up. (One `POST /profile/`
with `is_staff=on` is sufficient.)

## The fix
Removed `is_staff` from `ProfileForm.Meta.fields` so it can no longer be set from a user-controlled
form. The form now writes only `first_name`, `last_name`, `email`. Staff status is granted only by
an administrator (Django admin, or `createsuperuser`). The stale caption in `profile.html` was also
removed. No model change, no migration.

Verified: the escalation POST is now ignored, `/desk/` stays locked for ordinary users, and normal
posting, profile editing, and admin-granted staff access are all unaffected.

## Related (not changed here, flagged for follow-up)
- `listing_edit` / `listing_sold` / `listing_delete` don't verify ownership (any logged-in user can
  edit/sell/delete any listing by pk).
- `thread_detail` doesn't verify the viewer is a thread participant (private messages readable by pk).
