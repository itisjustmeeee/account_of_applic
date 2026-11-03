from django.db.models import Field, Lookup
from django.db.utils import NotSupportedError


class UnicodeIContains(Lookup):
    lookup_name = 'unicode_icontains'

    def as_sql(self, compiler, connection):
        if connection.vendor != 'sqlite':
            raise NotSupportedError(
                'Этот lookup предназначен для SQLite'
            )

        lhs, lhs_params = self.process_lhs(
            compiler,
            connection,
        )

        rhs, rhs_params = self.process_rhs(
            compiler,
            connection,
        )

        return (
            f'unicode_contains({lhs}, {rhs}) = 1',
            lhs_params + rhs_params,
        )


Field.register_lookup(UnicodeIContains)
