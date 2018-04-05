# pySwitchLib 

## PySwitchLib API Daemon

The pyswitchlib api daemon is a service that will translate pyswitchlib APIs into a REST request which the device/asset can then issue to the switch.

- The pyswitchlib-api-daemon service can start one or more pyswitchlib api daemons depending on the service configuration file.
- The pyswitchlib daemon(s) will be started or restarted when a pip install is done.
- A default API daemon will be started if the config file does not match any configured prefixes. For example if the pyswitchlib-api-daemon service is installed on to the host's base python.

### Pyswitchlib-api-daemon Service Configuration

The pyswitchlib-api-daemon service is installed with a default configuration file. If a working configuration file does not exist, then the default configuration file will be copied over and setup as the initial working configuration file. If a working configuration file already exits during an upgrade/install, then the working configuration file is preserved and will be used to start/restart the api daemon(s).

- Default config file is installed at /etc/pyswitchlib/pyswitchlib.conf.default
- Working config file is at /etc/pyswitchlib/pyswitchlib.conf.  If a working config file does not exist then the default config file will be copied and used as the working.
- The config file specifies how many api daemons will be launched and which sys.prefixes should be associated to the daemon.  When multiple sys.prefixes or virtualenv prefixes are associated to the api daemon (delimited by a colon), then any pyswitchlib assets created under these virtualenvs will utilize this single api daemon.
- The 'cacert = <Path to trusted CA certificate file>' is optional.  If ca certificate file is populated then it will be used for client side validations when https protocol is specified when assets are constructed.  If the 'cacert' option is not specified and https protocol is used then client side validations are bypassed and https protocol is still used.
- The 'ns_port = <tcp port #>' configuration is optional.  If specified, then a pyswitchlib_ns_daemon will be launched as well as the configured api daemons and pyswitchlib assets will use the name server daemon to lookup which api daemons to use.
- When the ns_port configuration is not specified, then a file is maintained to list which api daemons are running and how to connect to them.  Pyswitchlib assets will look up this file to connect to the proper api daemon.  The file is located at /etc/pyswitchlib/.pswitchlib_ns_daemon.uri.
- Any python virtualenv that is not found in the config file will try to connect to the default API daemon that is started on the host's base python.

#### Pyswitchlib-api-daemon Default Configuration

1. api_daemon_bwc_topology:  The associated sys.prefix is the bwc-topology virtualenv path
2. api_deamon_virtualenv_packs:  The two associated sys.prefixes are the network_essentials and dcfabric virtualenv paths

- When multiple prefixes are specified for a single api daemon, the first listed prefix will the be virtualenv which the api daemon will start up under.  When an api daemon is restarted, the config file is updated and the last restarted api daemon's prefix will be listed first.  The api deamon will be restarted during a pip install of a given virtualenv and which ever virtualenv is updated last we be the preferred virtualenv to service the rest of the configured virtualenvs. 

### Install required packages
```
    Standard PyPI Package Installation:
        sudo -H pip install pyswitchlib

    GitHub Repo Installation:
        sudo -H [<virtualenv prefix>/bin/]pip install -U git+https://github.com/StackStorm/PySwitchLib[@branch_name]
```

### Inside a python program do this
```
    import pyswitch.device
```

# pySwitchLib Version History

## 1.2.0
* Pyswitchlib uses an API daemon to convert pyswitchlib APIs into REST requests.
## 0.1.88
* Changed requirements to be locked to pybind 0.1.29.
## 0.1.87
* Added v17r.2.00 support in pyswitch netconf device.
## 0.1.86
* Added v17r.2.00 support in pyswitch.
## 0.1.85
* Updated v17s.1.02 bindings to include show_management_cluster rpc.
* Fixed v17r.2.00 support for rest rpc requests.
## 0.1.84
* Added back version check and reponse close logic.
## 0.1.83
* Added pybindgs support for slxos17r2.00.
## 0.1.82
* Pyswitch Wrapper for v7.x.x in NOS 
## 0.1.81
* Pyswitch Wrapper to use the same logic firmware version computation
## 0.1.80
* Pyswitch Wrapper uses two tuple version of firmware by default. 
## 0.1.79
* Added pybindings support for slxos17s1.02.
## 0.1.78
* Added pybindings support for nos7.2.0 and slxos17r1.01.
## 0.1.72
* Added support for add_vlan_int() bulk support using Raw XML over Netconf
## 0.1.70
* Fixed rbridge_id_create_vrf() API when 'vrf' is part of the parameter name.
## 0.1.67
* Fixed URI formation for mac_group_mac_create() API.
* Fixed pybind object set for vni parameter in overlay_gateway_map_vlan_vni_mapping_vni_update() API.
## 0.1.66
* Fixed issue with unnumbered interface.
## 0.1.54
* Fixed issue with update APIs where a value of 0 was not properly being updated.
## 0.1.63
* Added support for SLXOS 17r.1.00a
## 0.1.59
* Allow deletion of neighbor
* fix issue with creating neighbor associated to a peer-group
## 0.1.58
* Add support for neighbor peer-group configuration
* Add support for peer groups under l2vpn evpn afi
## 0.1.57
* Add support for trunk allowed vlan all
## 0.1.56
* Add support for NOS 7.0.0
## 0.1.52
* Fix for evpn_instance ignore as both 
## 0.1.51
* Raise Error when Interface is not present on device for admin_state
## 0.1.50
* JSON to XML Porting
## 0.1.49
* Added run_command() to asset class to allow CLI execution through REST API.
* Added _update_max_keep_alive_requests() to dynamically update apache setting to control number of persistent connection rest requests per login.
## 0.1.48
* Fixed fabric_service.trill_links
## 0.1.47
* Added authentication token code back to minimize login sessions.
## 0.1.44
* Add missing firmware_download_rpc.
* Added XML to JSON to Python Dictionary logic for error status REST requests.
## 0.1.43
* Added 6.0.2 in Pyswitch
## 0.1.41
* Reverted json output removal change done in 0.1.39.

## 0.1.40
* Added 16.1.1 and 17.1.1 to SLX
## 0.1.39
* Removed json output from main response object. get_dict_output() now converts xml response to json/dictionary.
* Added get_xml_output() method.

## 0.1.38
* Single entries for lldp 
## 0.1.37
* device was not closing the REST session 
## 0.1.35
* Removed delete APIs where YANG elements contain "cli-incomplete-no" extension.

## 0.1.34
* Fixed missing payload for default values.

## 0.1.33
* Fixed updating with default values.
## 0.1.32
* switchport_list corrected vlan entry for access

## 0.1.31
* interface_exists : checks for the presence of an interface

## 0.1.30
* Vrrpe Changes for ipv6

## 0.1.29
* Fix for show_arp for NOS/SLX
* VCS Nodes Listing is corrected for multiple nodes

## 0.1.28:
* Optimized firmware version fetch
* Fixed changes in Port Channel

## 0.1.26:
* Fixed VLAN issues in pyswitch_wrapper
* Fixed VRRPE issues in NOS
* Fixed key combination delimiter for REST URI formation of object instances.  Now uses '%2C' (comma) as the delimeter.
* Reverted REST session auth token code. REST requests will always authenticate.
* Updated dependency to a minimum version of pyangbind-brcd 0.6.12.
* Updated dependency to a minimum version of pybind 0.1.23.

## 0.1.25:
* Removed logging and logger from asset object.

## 0.1.24:
* Added leaf level delete APIs for containers and lists.
* Fixed leaf level update APIs where all other leaves under same container/list were incorrectly listed as kwargs to be updated.
* Updated requirements dependency on pybind module. Needs a minimum version of pybind 0.1.22.

## 0.1.20:
* Supported NOS Versions:
** nos6.0.2c (ga)
** nos7.0.1b (based on bld13)
* Added presence container create/delete support.  Specifically for rbridge-id router bgp enable/disable
* Added delete API counter parts for corresponding update APIs.
* Fixed xml payload formation for update operations.  Uses rest alt-name instead of yang name.
* Fixed IPv6 deletion issue.  REST URI formation in pyswitchlib was incorrect.  drop-node-names should only apply to containers.

## 0.1.19:
* get_dict_output() method added on asset object to easily access output response from last issued API.  Also YANG list elements will consistently be returned as a python list type regardless of single instance or multiple instances created
* Fixed out of order update for interface channel-groups api
* Added back missing RPCs.  Inadvertently removed when filtering out incorrect "output" input parameters for RPCs

## 0.1.18:
* Fixed source ip collision for ipv4/ipv6 acls
* Exposed update APIs for all interfaces at the list level
* Fixed boolean False issue

## 0.1.17:
* Added sphinx apidocs for pyswitchlib documentation generation.
* Organized API methods in separate files under api directory.
* Fixed missing kwargs for certain update API's.  Including interface_*_channel_group_update().
* Added workaround to detect SLX Fusion OS type. "show-firmware-rpc" in Fusion branch is returning "NOS" os type.
* Added tox framework (WIP)

## 0.1.16:
* Updated README.md with change information

## 0.1.15:
* Added persistent sessions for REST requests. Authentication Token renewed after 160 seconds between REST requests and in case of failed REST responses.
* Timeout kwarg added to asset and API's. Default asset timeout is 1800 seconds. API timeouts override asset timeout.
* Added get_os_type() and get_os_version() methods to asset object. 
* Request from BFO team
* RestInterfaceError expection raised when asset can connect to IP, but web server is not available. Request from BFO team.





