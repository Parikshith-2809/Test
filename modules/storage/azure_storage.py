"""Module for creating Azure Storage Accounts dynamically."""

from pulumi_azure_native import storage, resources

def create_storage_accounts(resource_groups_dict, accounts, primary_rg_name):
    """
    Creates multiple storage accounts.

    Args:
        resource_groups: list of ResourceGroup objects.
        accounts: list of dicts (name, sku, optional resourceGroup).
        primary_rg_name: str, name of the primary resource group.

    Returns:
        list of created storage.StorageAccount resources.
    """
    storages = []

    if primary_rg_name not in resource_groups_dict:
        raise ValueError(f"Primary RG '{primary_rg_name}' not found among created RGs.")

    for acct in accounts:
        target_rg_name = acct.get("resourceGroup", primary_rg_name)

        if target_rg_name not in resource_groups_dict:
            raise ValueError(f"ResourceGroup '{target_rg_name}' for storage account '{acct['name']}' not found.")

        rg_obj = resource_groups_dict[target_rg_name]

        storages.append(
            storage.StorageAccount(
                f"storage-{acct['name']}",
                resource_group_name=rg_obj.name,  # Azure RG name
                account_name=acct["name"],
                sku=storage.SkuArgs(name=acct["sku"]),
                kind=storage.Kind.STORAGE_V2,
            )
        )

    return storages
