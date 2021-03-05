# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class Resource(Model):
    """Resource.

    Common fields that are returned in the response for all Azure Resource
    Manager resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AzureEntityResource(Resource):
    """Entity Resource.

    The resource model definition for an Azure Resource Manager resource with
    an etag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureEntityResource, self).__init__(**kwargs)
        self.etag = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Display(Model):
    """Detailed HANA operation information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: The localized friendly form of the resource provider name.
     This form is also expected to include the publisher/company responsible.
     Use Title Casing. Begin with "Microsoft" for 1st party services.
    :vartype provider: str
    :ivar resource: The localized friendly form of the resource type related
     to this action/operation. This form should match the public documentation
     for the resource provider. Use Title Casing. For examples, refer to the
     “name” section.
    :vartype resource: str
    :ivar operation: The localized friendly name for the operation as shown to
     the user. This name should be concise (to fit in drop downs), but clear
     (self-documenting). Use Title Casing and include the entity/resource to
     which it applies.
    :vartype operation: str
    :ivar description: The localized friendly description for the operation as
     shown to the user. This description should be thorough, yet concise. It
     will be used in tool-tips and detailed views.
    :vartype description: str
    :ivar origin: The intended executor of the operation; governs the display
     of the operation in the RBAC UX and the audit logs UX. Default value is
     'user,system'
    :vartype origin: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Display, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None
        self.origin = None


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param error: Describes the error object.
    :type error: ~azure.mgmt.hanaonazure.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ErrorResponseError(Model):
    """Describes the error object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Error code
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorResponseError, self).__init__(**kwargs)
        self.code = None
        self.message = None


class Operation(Model):
    """HANA operation information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the operation being performed on this particular
     object. This name should match the action name that appears in RBAC / the
     event service.
    :vartype name: str
    :param display: Displayed HANA operation information
    :type display: ~azure.mgmt.hanaonazure.models.Display
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'Display'},
    }

    def __init__(self, *, display=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = display


class ProxyResource(Resource):
    """Proxy Resource.

    The resource model definition for a Azure Resource Manager proxy resource.
    It will not have tags and a location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ProxyResource, self).__init__(**kwargs)


class ProviderInstance(ProxyResource):
    """A provider instance associated with a SAP monitor.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param provider_instance_type: The type of provider instance.
    :type provider_instance_type: str
    :param properties: A JSON string containing the properties of the provider
     instance.
    :type properties: str
    :param metadata: A JSON string containing metadata of the provider
     instance.
    :type metadata: str
    :ivar provisioning_state: State of provisioning of the provider instance.
     Possible values include: 'Accepted', 'Creating', 'Updating', 'Failed',
     'Succeeded', 'Deleting', 'Migrating'
    :vartype provisioning_state: str or
     ~azure.mgmt.hanaonazure.models.HanaProvisioningStatesEnum
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provider_instance_type': {'key': 'properties.type', 'type': 'str'},
        'properties': {'key': 'properties.properties', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, provider_instance_type: str=None, properties: str=None, metadata: str=None, **kwargs) -> None:
        super(ProviderInstance, self).__init__(**kwargs)
        self.provider_instance_type = provider_instance_type
        self.properties = properties
        self.metadata = metadata
        self.provisioning_state = None


class TrackedResource(Resource):
    """Tracked Resource.

    The resource model definition for an Azure Resource Manager tracked top
    level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class SapMonitor(TrackedResource):
    """SAP monitor info on Azure (ARM properties and SAP monitor properties).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :ivar provisioning_state: State of provisioning of the HanaInstance.
     Possible values include: 'Accepted', 'Creating', 'Updating', 'Failed',
     'Succeeded', 'Deleting', 'Migrating'
    :vartype provisioning_state: str or
     ~azure.mgmt.hanaonazure.models.HanaProvisioningStatesEnum
    :ivar managed_resource_group_name: The name of the resource group the SAP
     Monitor resources get deployed into.
    :vartype managed_resource_group_name: str
    :param log_analytics_workspace_arm_id: The ARM ID of the Log Analytics
     Workspace that is used for monitoring
    :type log_analytics_workspace_arm_id: str
    :param enable_customer_analytics: The value indicating whether to send
     analytics to Microsoft
    :type enable_customer_analytics: bool
    :param log_analytics_workspace_id: The workspace ID of the log analytics
     workspace to be used for monitoring
    :type log_analytics_workspace_id: str
    :param log_analytics_workspace_shared_key: The shared key of the log
     analytics workspace that is used for monitoring
    :type log_analytics_workspace_shared_key: str
    :ivar sap_monitor_collector_version: The version of the payload running in
     the Collector VM
    :vartype sap_monitor_collector_version: str
    :param monitor_subnet: The subnet which the SAP monitor will be deployed
     in
    :type monitor_subnet: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'managed_resource_group_name': {'readonly': True},
        'sap_monitor_collector_version': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'managed_resource_group_name': {'key': 'properties.managedResourceGroupName', 'type': 'str'},
        'log_analytics_workspace_arm_id': {'key': 'properties.logAnalyticsWorkspaceArmId', 'type': 'str'},
        'enable_customer_analytics': {'key': 'properties.enableCustomerAnalytics', 'type': 'bool'},
        'log_analytics_workspace_id': {'key': 'properties.logAnalyticsWorkspaceId', 'type': 'str'},
        'log_analytics_workspace_shared_key': {'key': 'properties.logAnalyticsWorkspaceSharedKey', 'type': 'str'},
        'sap_monitor_collector_version': {'key': 'properties.sapMonitorCollectorVersion', 'type': 'str'},
        'monitor_subnet': {'key': 'properties.monitorSubnet', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, log_analytics_workspace_arm_id: str=None, enable_customer_analytics: bool=None, log_analytics_workspace_id: str=None, log_analytics_workspace_shared_key: str=None, monitor_subnet: str=None, **kwargs) -> None:
        super(SapMonitor, self).__init__(tags=tags, location=location, **kwargs)
        self.provisioning_state = None
        self.managed_resource_group_name = None
        self.log_analytics_workspace_arm_id = log_analytics_workspace_arm_id
        self.enable_customer_analytics = enable_customer_analytics
        self.log_analytics_workspace_id = log_analytics_workspace_id
        self.log_analytics_workspace_shared_key = log_analytics_workspace_shared_key
        self.sap_monitor_collector_version = None
        self.monitor_subnet = monitor_subnet


class Tags(Model):
    """Tags field of the resource.

    :param tags: Tags field of the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, tags=None, **kwargs) -> None:
        super(Tags, self).__init__(**kwargs)
        self.tags = tags
