"""
-----------------------------------------------------------------------------
Copyright (C) 2024 Jaime M. Villegas I. <jmvillegasi96@gmail.com>
-----------------------------------------------------------------------------
Package name  : snmp-test.py
Description   : Simple SNMP GET operation.
Version       : 01.00
Revision      : 00
Date          : March, 2024.
-----------------------------------------------------------------------------
"""

# Third party-libraries
from pysnmp.hlapi import *

################################################################
#                         TELTONIKA                            #
################################################################

# Target device configuration
teltonika_agent_ip   = "192.168.1.1"   # Device IP address
teltonika_community  = "public"        # Community string

# OIDs
teltonika_oids = [
    # --------------- Device Information ---------------------
    ".1.3.6.1.4.1.48690.1.1.0",       # Device serial number
    ".1.3.6.1.4.1.48690.1.2.0",       # Device name
    ".1.3.6.1.4.1.48690.1.5.0",       # Hardware version
    ".1.3.6.1.4.1.48690.1.6.0",       # RUTOS Firmware version
    ".1.3.6.1.4.1.48690.1.7.0",       # Device uptime
    # ----------------- Mobile status ------------------------
    ".1.3.6.1.4.1.48690.2.2.1.3.1",   # Modem IMEI
    ".1.3.6.1.4.1.48690.2.2.1.6.1",   # Modem firmware version
    ".1.3.6.1.4.1.48690.2.2.1.8.1",   # Modem IMSI number
    ".1.3.6.1.4.1.48690.2.2.1.9.1",   # SIM card status
    ".1.3.6.1.4.1.48690.2.2.1.10.1",  # PIN status
    ".1.3.6.1.4.1.48690.2.2.1.11.1",  # Mobile network registration status
    ".1.3.6.1.4.1.48690.2.2.1.12.1",  # Signal strength level
    ".1.3.6.1.4.1.48690.2.2.1.13.1",  # Current mobile network operator
    ".1.3.6.1.4.1.48690.2.2.1.14.1",  # Mobile operator number
    ".1.3.6.1.4.1.48690.2.2.1.15.1",  # Mobile data connection state
    ".1.3.6.1.4.1.48690.2.2.1.16.1",  # Mobile data connection type
    ".1.3.6.1.4.1.48690.2.2.1.22.1",  # Total bytes sent
    ".1.3.6.1.4.1.48690.2.2.1.23.1",  # Total bytes received
    ".1.3.6.1.4.1.48690.2.2.1.24.1",  # Modem IP address
    ".1.3.6.1.4.1.48690.2.2.1.25.1",  # Bytes sent today
    ".1.3.6.1.4.1.48690.2.2.1.26.1",  # Bytes received today
    ".1.3.6.1.4.1.48690.2.2.1.27.1",  # SIM ICCID
    ".1.3.6.1.4.1.48690.2.2.1.28.1",  # Bytes sent this week
    ".1.3.6.1.4.1.48690.2.2.1.29.1",  # Bytes received this week
    ".1.3.6.1.4.1.48690.2.2.1.30.1",  # Bytes sent this month
    ".1.3.6.1.4.1.48690.2.2.1.31.1",  # Bytes received this month
    ".1.3.6.1.4.1.48690.2.3.0.1"      # Mobile connection uptime
]

################################################################
#                          PEPLINK                             #
################################################################

# Target device configuration
peplink_agent_ip   = "192.168.1.1"   # Device IP address
peplink_community  = "public"        # Community string

# OIDs
peplink_oids = [
    # --------------- Device Information ---------------------
    ".1.3.6.1.4.1.23695.200.1.1.1.1.1.0",   # Device model
    ".1.3.6.1.4.1.23695.200.1.1.1.1.2.0",   # Device serial number
    ".1.3.6.1.4.1.23695.200.1.1.1.1.3.0",   # Device firmware version
    ".1.3.6.1.4.1.23695.200.1.1.1.1.4.0",   # Device name
    ".1.3.6.1.4.1.23695.200.1.1.1.1.6.0",   # Device hardware revision
    ".1.3.6.1.4.1.23695.200.1.1.1.2.2.0",   # Device system uptime
    # ----------------- Mobile status ------------------------
    ".1.3.6.1.4.1.23695.200.1.12.1.1.1.3",  # Signal RSSI
    ".1.3.6.1.4.1.23695.200.1.12.1.1.1.9",  # Cellular network type
    ".1.3.6.1.4.1.23695.200.1.12.1.1.1.10", # Cellular band
    ".1.3.6.1.4.1.23695.200.1.12.2.1.1.2",  # Cellular IMEI
    ".1.3.6.1.4.1.23695.200.1.12.3.1.1.2",  # Cellular model
    ".1.3.6.1.4.1.23695.200.1.12.3.1.1.5",  # Cellular hardware revision
    ".1.3.6.1.4.1.23695.200.1.12.3.1.1.6",  # Cellular firmware version
    ".1.3.6.1.4.1.23695.200.1.12.5.1.1.2",  # SIM card detected
    ".1.3.6.1.4.1.23695.200.1.12.5.1.1.3",  # SIM in use
    ".1.3.6.1.4.1.23695.200.1.12.5.1.1.4",  # SIM PIN code status
    ".1.3.6.1.4.1.23695.200.1.12.5.1.1.5",  # SIM IMSI
    ".1.3.6.1.4.1.23695.200.1.12.5.1.1.6",  # SIM ICCID
]

################################################################
#                        GRANDSTREAM                           #
################################################################

# Target device configuration
grandstream_agent_ip   = "192.168.1.1"  # Device IP address
grandstream_community  = "public"       # Community string

# OIDs
grandstream_oids = [
    # --------------- Device Information ---------------------
    ".1.3.6.1.4.1.42397.1.2.801",       # HT801
    ".1.3.6.1.4.1.42397.1.2.802",       # HT802
    ".1.3.6.1.4.1.42397.1.2.1.0",       # Part number
    ".1.3.6.1.4.1.42397.1.2.3.1.0",     # Bootloader version
    ".1.3.6.1.4.1.42397.1.2.3.2.0",     # Core version
    ".1.3.6.1.4.1.42397.1.2.3.3.0",     # Base version
    ".1.3.6.1.4.1.42397.1.2.4.1.0"      # Network mode
]

################################################################

# SNMP GET operation
def snmp_get(host, oid, community='public', port=161):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((host, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print('SNMP GET operation failed: %s' % errorIndication)
    elif errorStatus:
        print('SNMP GET operation failed: %s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print('OID: %s = %s' % (varBind[0], varBind[1]))

# Device selection
# (1): Teltonika
# (2): Peplink
# (3): Grandstream

selected_device = 1

if selected_device == 1:
    
    # Sets up Teltonika SNMP agent communication
    snmp_agent_ip = teltonika_agent_ip
    community = teltonika_community
    oids = teltonika_oids

elif selected_device == 2:

    # Sets up Peplink SNMP agent communication
    snmp_agent_ip = peplink_agent_ip
    community = peplink_community
    oids = peplink_oids

elif selected_device == 3:

    # Sets up Grandstream SNMP agent communication
    snmp_agent_ip = grandstream_agent_ip
    community = grandstream_community
    oids = teltonika_oids


# Performs SNMP GET operation
for oid in oids:
    snmp_get(snmp_agent_ip, oid, community)

input("TEST COMPLETED... PRESS ENTER TO EXIT")
