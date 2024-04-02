"""
The Tenant module

Exposes the tenant administration, for administrators to add, change and remove SPOTinfo tenants or subtenants
"""
from collections.abc import Iterable
from typing import override

from django.db import models


class SomeModel(models.Model):
    @override
    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: Iterable[str] | None = None,
    ) -> None:
        pass
