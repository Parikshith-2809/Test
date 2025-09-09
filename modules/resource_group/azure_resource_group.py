"""Module for creating Azure Resource Group."""

from pulumi_azure_native import resources

def create_resource_groups(rg_configs):
    """
    Create Resource Groups based on config.
    Returns a dict keyed by Azure resource group name.
    """
    rg_dict = {}

    for rg in rg_configs:
        rg_obj = resources.ResourceGroup(
            f"rg-{rg['name']}",
            resource_group_name=rg["name"],
            location=rg.get("location", "WestUS2")
        )
        rg_dict[rg["name"]] = rg_obj

    return rg_dict
