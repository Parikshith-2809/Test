"""Centralized config parsing for Pulumi project."""

import pulumi

config = pulumi.Config()

def get_resource_groups():
    return config.require_object("resourceGroups")

def get_primary_resource_group_name():
    return config.require("primaryResourceGroupName")

def get_storage_accounts():
    return config.require_object("storageAccounts")

def get_location():
    return config.get("location") or "WestUS2"

