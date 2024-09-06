#! /bin/sh

model_file=./api/models/item.py
add_code_to_model=$(cat <<EOF
shipping_fee = Column(Integer, default=0, nullable=False, comment="送料")
EOF
)
sed -i -e "s/# ここに送料を追加/${add_code_to_model}/g" ${model_file}

schema_file=./api/schemas/item.py
add_code_to_schema=$(cat <<EOF
shipping_fee: int = Field(0, example=500, description="送料")
EOF
)
sed -i -e "s/# ここに送料を追加/${add_code_to_schema}/g" ${schema_file}

crud_file=./api/cruds/item.py
add_code_to_crud=$(cat <<EOF
original.shipping_fee = item.shipping_fee
EOF
)
sed -i -e "s/# ここに送料を追加/${add_code_to_crud}/g" ${crud_file}

make dev-migrate