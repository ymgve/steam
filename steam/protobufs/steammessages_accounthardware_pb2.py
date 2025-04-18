# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_accounthardware.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#steammessages_accounthardware.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"b\n0CAccountHardware_RegisterSteamController_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\"3\n1CAccountHardware_RegisterSteamController_Response\"n\n<CAccountHardware_CompleteSteamControllerRegistration_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\"?\n=CAccountHardware_CompleteSteamControllerRegistration_Response\"j\n8CAccountHardware_QueryAccountsRegisteredToSerial_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\"m\n9CAccountHardware_QueryAccountsRegisteredToSerial_Accounts\x12\x11\n\taccountid\x18\x01 \x01(\r\x12\x1d\n\x15registration_complete\x18\x02 \x01(\x08\"\x89\x01\n9CAccountHardware_QueryAccountsRegisteredToSerial_Response\x12L\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32:.CAccountHardware_QueryAccountsRegisteredToSerial_Accounts\"\x80\x01\n:CAccountHardware_SteamControllerSetConfig_ControllerConfig\x12\x13\n\x0b\x61ppidorname\x18\x01 \x01(\t\x12\x17\n\x0fpublishedfileid\x18\x02 \x01(\x04\x12\x14\n\x0ctemplatename\x18\x03 \x01(\t\"\x8c\x02\n1CAccountHardware_SteamControllerSetConfig_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\x12\x11\n\taccountid\x18\x03 \x01(\r\x12S\n\x0e\x63onfigurations\x18\x04 \x03(\x0b\x32;.CAccountHardware_SteamControllerSetConfig_ControllerConfig\x12\x1a\n\x0f\x63ontroller_type\x18\x05 \x01(\x05:\x01\x32\x12#\n\x14only_for_this_serial\x18\x06 \x01(\x08:\x05\x66\x61lse\"4\n2CAccountHardware_SteamControllerSetConfig_Response\"\xcc\x01\n1CAccountHardware_SteamControllerGetConfig_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\x12\x11\n\taccountid\x18\x03 \x01(\r\x12\x13\n\x0b\x61ppidorname\x18\x04 \x01(\t\x12\x1a\n\x0f\x63ontroller_type\x18\x05 \x01(\x05:\x01\x32\x12#\n\x14only_for_this_serial\x18\x06 \x01(\x08:\x05\x66\x61lse\"\xb0\x01\n:CAccountHardware_SteamControllerGetConfig_ControllerConfig\x12\x13\n\x0b\x61ppidorname\x18\x01 \x01(\t\x12\x17\n\x0fpublishedfileid\x18\x02 \x01(\x04\x12\x14\n\x0ctemplatename\x18\x03 \x01(\t\x12\x15\n\rserial_number\x18\x04 \x01(\t\x12\x17\n\x08\x61utosave\x18\x05 \x01(\x08:\x05\x66\x61lse\"\x89\x01\n2CAccountHardware_SteamControllerGetConfig_Response\x12S\n\x0e\x63onfigurations\x18\x01 \x03(\x0b\x32;.CAccountHardware_SteamControllerGetConfig_ControllerConfig\"w\n2CAccountHardware_DeRegisterSteamController_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\x12\x11\n\taccountid\x18\x03 \x01(\r\"5\n3CAccountHardware_DeRegisterSteamController_Response\"t\n/CAccountHardware_SetPersonalizationFile_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0fpublishedfileid\x18\x02 \x01(\x04\x12\x11\n\taccountid\x18\x03 \x01(\r\"2\n0CAccountHardware_SetPersonalizationFile_Response\"[\n/CAccountHardware_GetPersonalizationFile_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x11\n\taccountid\x18\x02 \x01(\r\"K\n0CAccountHardware_GetPersonalizationFile_Response\x12\x17\n\x0fpublishedfileid\x18\x01 \x01(\x04\"\xae\x01\n-CAccountHardware_VRCompatibilityCheck_Request\x12\x14\n\x0cproduct_name\x18\x01 \x01(\t\x12\x43\n\x06values\x18\x02 \x03(\x0b\x32\x33.CAccountHardware_VRCompatibilityCheck_Request.Pair\x1a\"\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xb0\x02\n.CAccountHardware_VRCompatibilityCheck_Response\x12\x44\n\x06values\x18\x01 \x03(\x0b\x32\x34.CAccountHardware_VRCompatibilityCheck_Response.Pair\x12T\n\ncomponents\x18\x02 \x03(\x0b\x32@.CAccountHardware_VRCompatibilityCheck_Response.ComponentDisplay\x1a\"\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a>\n\x10\x43omponentDisplay\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\xfa\x01\n4CAccountHardware_RegisterValveIndexComponent_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\"\n\x1amanufacturer_serial_number\x18\x02 \x01(\t\x12\x16\n\x0e\x63omponent_code\x18\x03 \x01(\t\x12L\n\x0e\x63omponent_type\x18\x04 \x01(\x0e\x32\x15.EValveIndexComponent:\x1dk_EValveIndexComponentUnknown\x12!\n\x19\x65stimated_time_registered\x18\x05 \x01(\x05\"7\n5CAccountHardware_RegisterValveIndexComponent_Response\"a\n/CAccountHardware_GetSteamDeckComponents_Request\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_code\x18\x02 \x01(\t\"K\n0CAccountHardware_GetSteamDeckComponents_Response\x12\x17\n\x0fjson_components\x18\x01 \x01(\t*\xdd\x01\n\x14\x45ValveIndexComponent\x12!\n\x1dk_EValveIndexComponentUnknown\x10\x00\x12\x1d\n\x19k_EValveIndexComponentHMD\x10\x01\x12%\n!k_EValveIndexComponentLeftKnuckle\x10\x02\x12&\n\"k_EValveIndexComponentRightKnuckle\x10\x03\x12\x10\n\x0ck_ETempDTst1\x10\x04\x12\x10\n\x0ck_ETempDTst2\x10\x05\x12\x10\n\x0ck_ETempDTst3\x10\x06\x32\x9a\x0c\n\x0f\x41\x63\x63ountHardware\x12\x80\x01\n\x17RegisterSteamController\x12\x31.CAccountHardware_RegisterSteamController_Request\x1a\x32.CAccountHardware_RegisterSteamController_Response\x12\xa4\x01\n#CompleteSteamControllerRegistration\x12=.CAccountHardware_CompleteSteamControllerRegistration_Request\x1a>.CAccountHardware_CompleteSteamControllerRegistration_Response\x12\x9c\x01\n#QueryAccountsRegisteredToController\x12\x39.CAccountHardware_QueryAccountsRegisteredToSerial_Request\x1a:.CAccountHardware_QueryAccountsRegisteredToSerial_Response\x12\x8b\x01\n SetDesiredControllerConfigForApp\x12\x32.CAccountHardware_SteamControllerSetConfig_Request\x1a\x33.CAccountHardware_SteamControllerSetConfig_Response\x12\x8b\x01\n GetDesiredControllerConfigForApp\x12\x32.CAccountHardware_SteamControllerGetConfig_Request\x1a\x33.CAccountHardware_SteamControllerGetConfig_Response\x12\x86\x01\n\x19\x44\x65RegisterSteamController\x12\x33.CAccountHardware_DeRegisterSteamController_Request\x1a\x34.CAccountHardware_DeRegisterSteamController_Response\x12\x87\x01\n SetControllerPersonalizationFile\x12\x30.CAccountHardware_SetPersonalizationFile_Request\x1a\x31.CAccountHardware_SetPersonalizationFile_Response\x12\x87\x01\n GetControllerPersonalizationFile\x12\x30.CAccountHardware_GetPersonalizationFile_Request\x1a\x31.CAccountHardware_GetPersonalizationFile_Response\x12w\n\x14VRCompatibilityCheck\x12..CAccountHardware_VRCompatibilityCheck_Request\x1a/.CAccountHardware_VRCompatibilityCheck_Response\x12\x8c\x01\n\x1bRegisterValveIndexComponent\x12\x35.CAccountHardware_RegisterValveIndexComponent_Request\x1a\x36.CAccountHardware_RegisterValveIndexComponent_Response\x12}\n\x16GetSteamDeckComponents\x12\x30.CAccountHardware_GetSteamDeckComponents_Request\x1a\x31.CAccountHardware_GetSteamDeckComponents_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_accounthardware_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_EVALVEINDEXCOMPONENT']._serialized_start=3257
  _globals['_EVALVEINDEXCOMPONENT']._serialized_end=3478
  _globals['_CACCOUNTHARDWARE_REGISTERSTEAMCONTROLLER_REQUEST']._serialized_start=99
  _globals['_CACCOUNTHARDWARE_REGISTERSTEAMCONTROLLER_REQUEST']._serialized_end=197
  _globals['_CACCOUNTHARDWARE_REGISTERSTEAMCONTROLLER_RESPONSE']._serialized_start=199
  _globals['_CACCOUNTHARDWARE_REGISTERSTEAMCONTROLLER_RESPONSE']._serialized_end=250
  _globals['_CACCOUNTHARDWARE_COMPLETESTEAMCONTROLLERREGISTRATION_REQUEST']._serialized_start=252
  _globals['_CACCOUNTHARDWARE_COMPLETESTEAMCONTROLLERREGISTRATION_REQUEST']._serialized_end=362
  _globals['_CACCOUNTHARDWARE_COMPLETESTEAMCONTROLLERREGISTRATION_RESPONSE']._serialized_start=364
  _globals['_CACCOUNTHARDWARE_COMPLETESTEAMCONTROLLERREGISTRATION_RESPONSE']._serialized_end=427
  _globals['_CACCOUNTHARDWARE_QUERYACCOUNTSREGISTEREDTOSERIAL_REQUEST']._serialized_start=429
  _globals['_CACCOUNTHARDWARE_QUERYACCOUNTSREGISTEREDTOSERIAL_REQUEST']._serialized_end=535
  _globals['_CACCOUNTHARDWARE_QUERYACCOUNTSREGISTEREDTOSERIAL_ACCOUNTS']._serialized_start=537
  _globals['_CACCOUNTHARDWARE_QUERYACCOUNTSREGISTEREDTOSERIAL_ACCOUNTS']._serialized_end=646
  _globals['_CACCOUNTHARDWARE_QUERYACCOUNTSREGISTEREDTOSERIAL_RESPONSE']._serialized_start=649
  _globals['_CACCOUNTHARDWARE_QUERYACCOUNTSREGISTEREDTOSERIAL_RESPONSE']._serialized_end=786
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERSETCONFIG_CONTROLLERCONFIG']._serialized_start=789
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERSETCONFIG_CONTROLLERCONFIG']._serialized_end=917
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERSETCONFIG_REQUEST']._serialized_start=920
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERSETCONFIG_REQUEST']._serialized_end=1188
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERSETCONFIG_RESPONSE']._serialized_start=1190
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERSETCONFIG_RESPONSE']._serialized_end=1242
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERGETCONFIG_REQUEST']._serialized_start=1245
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERGETCONFIG_REQUEST']._serialized_end=1449
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERGETCONFIG_CONTROLLERCONFIG']._serialized_start=1452
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERGETCONFIG_CONTROLLERCONFIG']._serialized_end=1628
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERGETCONFIG_RESPONSE']._serialized_start=1631
  _globals['_CACCOUNTHARDWARE_STEAMCONTROLLERGETCONFIG_RESPONSE']._serialized_end=1768
  _globals['_CACCOUNTHARDWARE_DEREGISTERSTEAMCONTROLLER_REQUEST']._serialized_start=1770
  _globals['_CACCOUNTHARDWARE_DEREGISTERSTEAMCONTROLLER_REQUEST']._serialized_end=1889
  _globals['_CACCOUNTHARDWARE_DEREGISTERSTEAMCONTROLLER_RESPONSE']._serialized_start=1891
  _globals['_CACCOUNTHARDWARE_DEREGISTERSTEAMCONTROLLER_RESPONSE']._serialized_end=1944
  _globals['_CACCOUNTHARDWARE_SETPERSONALIZATIONFILE_REQUEST']._serialized_start=1946
  _globals['_CACCOUNTHARDWARE_SETPERSONALIZATIONFILE_REQUEST']._serialized_end=2062
  _globals['_CACCOUNTHARDWARE_SETPERSONALIZATIONFILE_RESPONSE']._serialized_start=2064
  _globals['_CACCOUNTHARDWARE_SETPERSONALIZATIONFILE_RESPONSE']._serialized_end=2114
  _globals['_CACCOUNTHARDWARE_GETPERSONALIZATIONFILE_REQUEST']._serialized_start=2116
  _globals['_CACCOUNTHARDWARE_GETPERSONALIZATIONFILE_REQUEST']._serialized_end=2207
  _globals['_CACCOUNTHARDWARE_GETPERSONALIZATIONFILE_RESPONSE']._serialized_start=2209
  _globals['_CACCOUNTHARDWARE_GETPERSONALIZATIONFILE_RESPONSE']._serialized_end=2284
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_REQUEST']._serialized_start=2287
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_REQUEST']._serialized_end=2461
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_REQUEST_PAIR']._serialized_start=2427
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_REQUEST_PAIR']._serialized_end=2461
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_RESPONSE']._serialized_start=2464
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_RESPONSE']._serialized_end=2768
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_RESPONSE_PAIR']._serialized_start=2427
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_RESPONSE_PAIR']._serialized_end=2461
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_RESPONSE_COMPONENTDISPLAY']._serialized_start=2706
  _globals['_CACCOUNTHARDWARE_VRCOMPATIBILITYCHECK_RESPONSE_COMPONENTDISPLAY']._serialized_end=2768
  _globals['_CACCOUNTHARDWARE_REGISTERVALVEINDEXCOMPONENT_REQUEST']._serialized_start=2771
  _globals['_CACCOUNTHARDWARE_REGISTERVALVEINDEXCOMPONENT_REQUEST']._serialized_end=3021
  _globals['_CACCOUNTHARDWARE_REGISTERVALVEINDEXCOMPONENT_RESPONSE']._serialized_start=3023
  _globals['_CACCOUNTHARDWARE_REGISTERVALVEINDEXCOMPONENT_RESPONSE']._serialized_end=3078
  _globals['_CACCOUNTHARDWARE_GETSTEAMDECKCOMPONENTS_REQUEST']._serialized_start=3080
  _globals['_CACCOUNTHARDWARE_GETSTEAMDECKCOMPONENTS_REQUEST']._serialized_end=3177
  _globals['_CACCOUNTHARDWARE_GETSTEAMDECKCOMPONENTS_RESPONSE']._serialized_start=3179
  _globals['_CACCOUNTHARDWARE_GETSTEAMDECKCOMPONENTS_RESPONSE']._serialized_end=3254
  _globals['_ACCOUNTHARDWARE']._serialized_start=3481
  _globals['_ACCOUNTHARDWARE']._serialized_end=5043
_builder.BuildServices(DESCRIPTOR, 'steammessages_accounthardware_pb2', _globals)
# @@protoc_insertion_point(module_scope)
