"""Pulumi entry point: creates Azure resource group + storage accounts dynamically."""

import pulumi
from pulumi_azure_native import resources
from config import (
    get_resource_groups,
    get_primary_resource_group_name,
    get_storage_accounts,
)
from modules.resource_group.azure_resource_group import create_resource_groups
from modules.storage.azure_storage import create_storage_accounts

# 1. Create RGs
resource_groups = create_resource_groups(get_resource_groups())

# 2. Get config values
primary_rg_name = get_primary_resource_group_name()
storage_accounts_cfg = get_storage_accounts()

# 3. Create storage accounts 
storage_accounts = create_storage_accounts(resource_groups, storage_accounts_cfg, primary_rg_name)

# export the output

pulumi.export("resourceGroups", [rg.name for rg in resource_groups.values()])
pulumi.export("primaryResourceGroup", primary_rg_name)
pulumi.export("storageAccounts", [sa.name for sa in storage_accounts])
