# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network manager list-deploy-status",
)
class ListDeployStatus(AAZCommand):
    """Post List of Network Manager Deployment Status.

    :example: List Azure Virtual Network Manager Deployment Status
        az network manager list-deploy-status --network-manager-name "testNetworkManager" --deployment-types "Connectivity" "SecurityAdmin" --regions "eastus" "westus" --resource-group "resoureGroupSample"
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkmanagers/{}/listdeploymentstatus", "2022-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.network_manager_name = AAZStrArg(
            options=["-n", "--name", "--network-manager-name"],
            help="The name of the network manager.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.deployment_types = AAZListArg(
            options=["--deployment-types"],
            arg_group="Parameters",
            help="List of deployment types.",
        )
        _args_schema.regions = AAZListArg(
            options=["--regions"],
            arg_group="Parameters",
            help="List of locations.",
        )
        _args_schema.skip_token = AAZStrArg(
            options=["--skip-token"],
            arg_group="Parameters",
            help="Continuation token for pagination, capturing the next page size and offset, as well as the context of the query.",
        )

        deployment_types = cls._args_schema.deployment_types
        deployment_types.Element = AAZStrArg(
            enum={"Connectivity": "Connectivity", "SecurityAdmin": "SecurityAdmin"},
        )

        regions = cls._args_schema.regions
        regions.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NetworkManagerDeploymentStatusList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetworkManagerDeploymentStatusList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/listDeploymentStatus",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkManagerName", self.ctx.args.network_manager_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("deploymentTypes", AAZListType, ".deployment_types")
            _builder.set_prop("regions", AAZListType, ".regions")
            _builder.set_prop("skipToken", AAZStrType, ".skip_token")

            deployment_types = _builder.get(".deploymentTypes")
            if deployment_types is not None:
                deployment_types.set_elements(AAZStrType, ".")

            regions = _builder.get(".regions")
            if regions is not None:
                regions.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.skip_token = AAZStrType(
                serialized_name="skipToken",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.commit_time = AAZStrType(
                serialized_name="commitTime",
            )
            _element.configuration_ids = AAZListType(
                serialized_name="configurationIds",
            )
            _element.deployment_status = AAZStrType(
                serialized_name="deploymentStatus",
            )
            _element.deployment_type = AAZStrType(
                serialized_name="deploymentType",
            )
            _element.error_message = AAZStrType(
                serialized_name="errorMessage",
            )
            _element.region = AAZStrType()

            configuration_ids = cls._schema_on_200.value.Element.configuration_ids
            configuration_ids.Element = AAZStrType()

            return cls._schema_on_200


class _ListDeployStatusHelper:
    """Helper class for ListDeployStatus"""


__all__ = ["ListDeployStatus"]