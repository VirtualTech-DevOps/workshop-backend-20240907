#!/bin/bash

# ==========================================
# Install Python dependencies
# ==========================================
make install && make migrate

# ==========================================
#  Add shipping_fee
# ==========================================
./.devcontainer/add_shipping_fee.sh