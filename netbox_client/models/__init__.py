# coding: utf-8

# flake8: noqa
"""
    NetBox API

    API to access NetBox  # noqa: E501

    OpenAPI spec version: 2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from netbox_client.models.action import Action
from netbox_client.models.aggregate import Aggregate
from netbox_client.models.available_ip import AvailableIP
from netbox_client.models.available_prefix import AvailablePrefix
from netbox_client.models.cable import Cable
from netbox_client.models.circuit import Circuit
from netbox_client.models.circuit_circuit_termination import CircuitCircuitTermination
from netbox_client.models.circuit_termination import CircuitTermination
from netbox_client.models.circuit_type import CircuitType
from netbox_client.models.cluster import Cluster
from netbox_client.models.cluster_group import ClusterGroup
from netbox_client.models.cluster_type import ClusterType
from netbox_client.models.config_context import ConfigContext
from netbox_client.models.connection_status import ConnectionStatus
from netbox_client.models.console_port import ConsolePort
from netbox_client.models.console_port_template import ConsolePortTemplate
from netbox_client.models.console_server_port import ConsoleServerPort
from netbox_client.models.console_server_port_template import ConsoleServerPortTemplate
from netbox_client.models.device import Device
from netbox_client.models.device_bay import DeviceBay
from netbox_client.models.device_bay_template import DeviceBayTemplate
from netbox_client.models.device_interface import DeviceInterface
from netbox_client.models.device_napalm import DeviceNAPALM
from netbox_client.models.device_role import DeviceRole
from netbox_client.models.device_type import DeviceType
from netbox_client.models.device_with_config_context import DeviceWithConfigContext
from netbox_client.models.export_template import ExportTemplate
from netbox_client.models.face import Face
from netbox_client.models.family import Family
from netbox_client.models.feed_leg import FeedLeg
from netbox_client.models.front_port import FrontPort
from netbox_client.models.front_port_rear_port import FrontPortRearPort
from netbox_client.models.front_port_template import FrontPortTemplate
from netbox_client.models.graph import Graph
from netbox_client.models.ip_address import IPAddress
from netbox_client.models.ip_address_interface import IPAddressInterface
from netbox_client.models.image_attachment import ImageAttachment
from netbox_client.models.inline_response200 import InlineResponse200
from netbox_client.models.inline_response2001 import InlineResponse2001
from netbox_client.models.inline_response20010 import InlineResponse20010
from netbox_client.models.inline_response20011 import InlineResponse20011
from netbox_client.models.inline_response20012 import InlineResponse20012
from netbox_client.models.inline_response20013 import InlineResponse20013
from netbox_client.models.inline_response20014 import InlineResponse20014
from netbox_client.models.inline_response20015 import InlineResponse20015
from netbox_client.models.inline_response20016 import InlineResponse20016
from netbox_client.models.inline_response20017 import InlineResponse20017
from netbox_client.models.inline_response20018 import InlineResponse20018
from netbox_client.models.inline_response20019 import InlineResponse20019
from netbox_client.models.inline_response2002 import InlineResponse2002
from netbox_client.models.inline_response20020 import InlineResponse20020
from netbox_client.models.inline_response20021 import InlineResponse20021
from netbox_client.models.inline_response20022 import InlineResponse20022
from netbox_client.models.inline_response20023 import InlineResponse20023
from netbox_client.models.inline_response20024 import InlineResponse20024
from netbox_client.models.inline_response20025 import InlineResponse20025
from netbox_client.models.inline_response20026 import InlineResponse20026
from netbox_client.models.inline_response20027 import InlineResponse20027
from netbox_client.models.inline_response20028 import InlineResponse20028
from netbox_client.models.inline_response20029 import InlineResponse20029
from netbox_client.models.inline_response2003 import InlineResponse2003
from netbox_client.models.inline_response20030 import InlineResponse20030
from netbox_client.models.inline_response20031 import InlineResponse20031
from netbox_client.models.inline_response20032 import InlineResponse20032
from netbox_client.models.inline_response20033 import InlineResponse20033
from netbox_client.models.inline_response20034 import InlineResponse20034
from netbox_client.models.inline_response20035 import InlineResponse20035
from netbox_client.models.inline_response20036 import InlineResponse20036
from netbox_client.models.inline_response20037 import InlineResponse20037
from netbox_client.models.inline_response20038 import InlineResponse20038
from netbox_client.models.inline_response20039 import InlineResponse20039
from netbox_client.models.inline_response2004 import InlineResponse2004
from netbox_client.models.inline_response20040 import InlineResponse20040
from netbox_client.models.inline_response20041 import InlineResponse20041
from netbox_client.models.inline_response20042 import InlineResponse20042
from netbox_client.models.inline_response20043 import InlineResponse20043
from netbox_client.models.inline_response20044 import InlineResponse20044
from netbox_client.models.inline_response20045 import InlineResponse20045
from netbox_client.models.inline_response20046 import InlineResponse20046
from netbox_client.models.inline_response20047 import InlineResponse20047
from netbox_client.models.inline_response20048 import InlineResponse20048
from netbox_client.models.inline_response20049 import InlineResponse20049
from netbox_client.models.inline_response2005 import InlineResponse2005
from netbox_client.models.inline_response20050 import InlineResponse20050
from netbox_client.models.inline_response20051 import InlineResponse20051
from netbox_client.models.inline_response20052 import InlineResponse20052
from netbox_client.models.inline_response20053 import InlineResponse20053
from netbox_client.models.inline_response20054 import InlineResponse20054
from netbox_client.models.inline_response20055 import InlineResponse20055
from netbox_client.models.inline_response20056 import InlineResponse20056
from netbox_client.models.inline_response20057 import InlineResponse20057
from netbox_client.models.inline_response20058 import InlineResponse20058
from netbox_client.models.inline_response20059 import InlineResponse20059
from netbox_client.models.inline_response2006 import InlineResponse2006
from netbox_client.models.inline_response20060 import InlineResponse20060
from netbox_client.models.inline_response2007 import InlineResponse2007
from netbox_client.models.inline_response2008 import InlineResponse2008
from netbox_client.models.inline_response2009 import InlineResponse2009
from netbox_client.models.interface_connection import InterfaceConnection
from netbox_client.models.interface_template import InterfaceTemplate
from netbox_client.models.inventory_item import InventoryItem
from netbox_client.models.length_unit import LengthUnit
from netbox_client.models.manufacturer import Manufacturer
from netbox_client.models.mode import Mode
from netbox_client.models.nested_cable import NestedCable
from netbox_client.models.nested_circuit import NestedCircuit
from netbox_client.models.nested_circuit_type import NestedCircuitType
from netbox_client.models.nested_cluster import NestedCluster
from netbox_client.models.nested_cluster_group import NestedClusterGroup
from netbox_client.models.nested_cluster_type import NestedClusterType
from netbox_client.models.nested_device import NestedDevice
from netbox_client.models.nested_device_role import NestedDeviceRole
from netbox_client.models.nested_device_type import NestedDeviceType
from netbox_client.models.nested_ip_address import NestedIPAddress
from netbox_client.models.nested_interface import NestedInterface
from netbox_client.models.nested_manufacturer import NestedManufacturer
from netbox_client.models.nested_platform import NestedPlatform
from netbox_client.models.nested_power_panel import NestedPowerPanel
from netbox_client.models.nested_power_port import NestedPowerPort
from netbox_client.models.nested_power_port_template import NestedPowerPortTemplate
from netbox_client.models.nested_provider import NestedProvider
from netbox_client.models.nested_rir import NestedRIR
from netbox_client.models.nested_rack import NestedRack
from netbox_client.models.nested_rack_group import NestedRackGroup
from netbox_client.models.nested_rack_role import NestedRackRole
from netbox_client.models.nested_rear_port_template import NestedRearPortTemplate
from netbox_client.models.nested_region import NestedRegion
from netbox_client.models.nested_role import NestedRole
from netbox_client.models.nested_secret_role import NestedSecretRole
from netbox_client.models.nested_site import NestedSite
from netbox_client.models.nested_tenant import NestedTenant
from netbox_client.models.nested_tenant_group import NestedTenantGroup
from netbox_client.models.nested_user import NestedUser
from netbox_client.models.nested_vlan import NestedVLAN
from netbox_client.models.nested_vlan_group import NestedVLANGroup
from netbox_client.models.nested_vrf import NestedVRF
from netbox_client.models.nested_virtual_chassis import NestedVirtualChassis
from netbox_client.models.nested_virtual_machine import NestedVirtualMachine
from netbox_client.models.object_change import ObjectChange
from netbox_client.models.outer_unit import OuterUnit
from netbox_client.models.phase import Phase
from netbox_client.models.platform import Platform
from netbox_client.models.power_feed import PowerFeed
from netbox_client.models.power_outlet import PowerOutlet
from netbox_client.models.power_outlet_template import PowerOutletTemplate
from netbox_client.models.power_panel import PowerPanel
from netbox_client.models.power_port import PowerPort
from netbox_client.models.power_port_template import PowerPortTemplate
from netbox_client.models.prefix import Prefix
from netbox_client.models.protocol import Protocol
from netbox_client.models.provider import Provider
from netbox_client.models.rir import RIR
from netbox_client.models.rack import Rack
from netbox_client.models.rack_group import RackGroup
from netbox_client.models.rack_reservation import RackReservation
from netbox_client.models.rack_role import RackRole
from netbox_client.models.rack_unit import RackUnit
from netbox_client.models.rear_port import RearPort
from netbox_client.models.rear_port_template import RearPortTemplate
from netbox_client.models.region import Region
from netbox_client.models.role import Role
from netbox_client.models.role1 import Role1
from netbox_client.models.secret import Secret
from netbox_client.models.secret_role import SecretRole
from netbox_client.models.service import Service
from netbox_client.models.site import Site
from netbox_client.models.status import Status
from netbox_client.models.status1 import Status1
from netbox_client.models.status2 import Status2
from netbox_client.models.status3 import Status3
from netbox_client.models.status4 import Status4
from netbox_client.models.status5 import Status5
from netbox_client.models.status6 import Status6
from netbox_client.models.status7 import Status7
from netbox_client.models.status8 import Status8
from netbox_client.models.status9 import Status9
from netbox_client.models.subdevice_role import SubdeviceRole
from netbox_client.models.supply import Supply
from netbox_client.models.tag import Tag
from netbox_client.models.template_language import TemplateLanguage
from netbox_client.models.tenant import Tenant
from netbox_client.models.tenant_group import TenantGroup
from netbox_client.models.type import Type
from netbox_client.models.type1 import Type1
from netbox_client.models.type2 import Type2
from netbox_client.models.type3 import Type3
from netbox_client.models.type4 import Type4
from netbox_client.models.type5 import Type5
from netbox_client.models.type6 import Type6
from netbox_client.models.type7 import Type7
from netbox_client.models.vlan import VLAN
from netbox_client.models.vlan_group import VLANGroup
from netbox_client.models.vrf import VRF
from netbox_client.models.virtual_chassis import VirtualChassis
from netbox_client.models.virtual_machine_interface import VirtualMachineInterface
from netbox_client.models.virtual_machine_with_config_context import VirtualMachineWithConfigContext
from netbox_client.models.width import Width
from netbox_client.models.writable_aggregate import WritableAggregate
from netbox_client.models.writable_cable import WritableCable
from netbox_client.models.writable_circuit import WritableCircuit
from netbox_client.models.writable_circuit_termination import WritableCircuitTermination
from netbox_client.models.writable_cluster import WritableCluster
from netbox_client.models.writable_config_context import WritableConfigContext
from netbox_client.models.writable_console_port import WritableConsolePort
from netbox_client.models.writable_console_port_template import WritableConsolePortTemplate
from netbox_client.models.writable_console_server_port import WritableConsoleServerPort
from netbox_client.models.writable_console_server_port_template import WritableConsoleServerPortTemplate
from netbox_client.models.writable_device_bay import WritableDeviceBay
from netbox_client.models.writable_device_bay_template import WritableDeviceBayTemplate
from netbox_client.models.writable_device_interface import WritableDeviceInterface
from netbox_client.models.writable_device_type import WritableDeviceType
from netbox_client.models.writable_device_with_config_context import WritableDeviceWithConfigContext
from netbox_client.models.writable_export_template import WritableExportTemplate
from netbox_client.models.writable_front_port import WritableFrontPort
from netbox_client.models.writable_front_port_template import WritableFrontPortTemplate
from netbox_client.models.writable_ip_address import WritableIPAddress
from netbox_client.models.writable_interface_template import WritableInterfaceTemplate
from netbox_client.models.writable_inventory_item import WritableInventoryItem
from netbox_client.models.writable_platform import WritablePlatform
from netbox_client.models.writable_power_feed import WritablePowerFeed
from netbox_client.models.writable_power_outlet import WritablePowerOutlet
from netbox_client.models.writable_power_outlet_template import WritablePowerOutletTemplate
from netbox_client.models.writable_power_panel import WritablePowerPanel
from netbox_client.models.writable_power_port import WritablePowerPort
from netbox_client.models.writable_power_port_template import WritablePowerPortTemplate
from netbox_client.models.writable_prefix import WritablePrefix
from netbox_client.models.writable_rack import WritableRack
from netbox_client.models.writable_rack_group import WritableRackGroup
from netbox_client.models.writable_rack_reservation import WritableRackReservation
from netbox_client.models.writable_rear_port import WritableRearPort
from netbox_client.models.writable_rear_port_template import WritableRearPortTemplate
from netbox_client.models.writable_region import WritableRegion
from netbox_client.models.writable_secret import WritableSecret
from netbox_client.models.writable_service import WritableService
from netbox_client.models.writable_site import WritableSite
from netbox_client.models.writable_tenant import WritableTenant
from netbox_client.models.writable_tenant_group import WritableTenantGroup
from netbox_client.models.writable_vlan import WritableVLAN
from netbox_client.models.writable_vlan_group import WritableVLANGroup
from netbox_client.models.writable_vrf import WritableVRF
from netbox_client.models.writable_virtual_chassis import WritableVirtualChassis
from netbox_client.models.writable_virtual_machine_interface import WritableVirtualMachineInterface
from netbox_client.models.writable_virtual_machine_with_config_context import WritableVirtualMachineWithConfigContext