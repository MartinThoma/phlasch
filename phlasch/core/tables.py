import sqlalchemy as sa
from phlasch.db.meta import metadata


# link table
link = sa.Table(
    'phlasch_link',
    metadata,
    sa.Column(
        'id',
        sa.Integer,
        sa.Sequence('phlasch_link_id_seq'),
        primary_key=True,
    ),
    sa.Column(
        'address',
        sa.Text,
        sa.CheckConstraint("address>''"),
        nullable=False,
    ),
    sa.Column(
        'shortcut',
        sa.String(256),
        nullable=True,
        unique=True,
        index=True,
    ),
    sa.Column(
        'visits',
        sa.Integer,
        nullable=False,
        server_default="0",
    ),
)
