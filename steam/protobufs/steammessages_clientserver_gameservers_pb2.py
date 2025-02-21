# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_clientserver_gameservers.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,steammessages_clientserver_gameservers.proto\x1a\x18steammessages_base.proto\"\xed\x01\n\x10\x43MsgGSServerType\x12\x15\n\rapp_id_served\x18\x01 \x01(\r\x12\r\n\x05\x66lags\x18\x02 \x01(\r\x12\"\n\x1a\x64\x65precated_game_ip_address\x18\x03 \x01(\r\x12\x11\n\tgame_port\x18\x04 \x01(\r\x12\x10\n\x08game_dir\x18\x05 \x01(\t\x12\x14\n\x0cgame_version\x18\x06 \x01(\t\x12\x17\n\x0fgame_query_port\x18\x07 \x01(\r\x12\x17\n\x0fgame_port_local\x18\n \x01(\r\x12\x11\n\tsdr_logon\x18\x08 \x01(\x0c\x12\x0f\n\x07\x66\x61ke_ip\x18\t \x01(\x07\"&\n\x11\x43MsgGSStatusReply\x12\x11\n\tis_secure\x18\x01 \x01(\x08\"\xa9\x01\n\x10\x43MsgGSPlayerList\x12)\n\x07players\x18\x01 \x03(\x0b\x32\x18.CMsgGSPlayerList.Player\x1aj\n\x06Player\x12\x10\n\x08steam_id\x18\x01 \x01(\x04\x12\x1c\n\x14\x64\x65precated_public_ip\x18\x02 \x01(\r\x12\r\n\x05token\x18\x03 \x01(\x0c\x12!\n\tpublic_ip\x18\x04 \x01(\x0b\x32\x0e.CMsgIPAddress\"u\n\x11\x43MsgGSUserPlaying\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x1c\n\x14\x64\x65precated_public_ip\x18\x02 \x01(\r\x12\r\n\x05token\x18\x03 \x01(\x0c\x12!\n\tpublic_ip\x18\x04 \x01(\x0b\x32\x0e.CMsgIPAddress\"*\n\x16\x43MsgGSDisconnectNotice\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\"\x97\x04\n\x12\x43MsgGameServerData\x12\x10\n\x08revision\x18\x18 \x01(\r\x12\x12\n\nquery_port\x18\x03 \x01(\r\x12\x11\n\tgame_port\x18\x04 \x01(\r\x12\x16\n\x0espectator_port\x18\x05 \x01(\r\x12\x13\n\x0bserver_name\x18\x16 \x01(\t\x12\x18\n\x10game_description\x18\x1d \x01(\t\x12\x1d\n\x15spectator_server_name\x18\x1b \x01(\t\x12\x0f\n\x07\x66\x61ke_ip\x18\x1c \x01(\x07\x12\x19\n\x11sdr_ping_location\x18\x1e \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x06 \x01(\r\x12\x0f\n\x07gamedir\x18\x07 \x01(\t\x12\x0f\n\x07version\x18\x08 \x01(\t\x12\x0f\n\x07product\x18\t \x01(\t\x12\x0e\n\x06region\x18\n \x01(\t\x12+\n\x07players\x18\x0b \x03(\x0b\x32\x1a.CMsgGameServerData.Player\x12\x13\n\x0bmax_players\x18\x0c \x01(\r\x12\x11\n\tbot_count\x18\r \x01(\r\x12\x10\n\x08password\x18\x0e \x01(\x08\x12\x0e\n\x06secure\x18\x0f \x01(\x08\x12\x11\n\tdedicated\x18\x10 \x01(\x08\x12\n\n\x02os\x18\x11 \x01(\t\x12\x11\n\tgame_data\x18\x12 \x01(\t\x12\x11\n\tgame_type\x18\x14 \x01(\t\x12\x0b\n\x03map\x18\x15 \x01(\t\x1a\x1a\n\x06Player\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\"M\n\x14\x43MsgGameServerRemove\x12\x1a\n\x12legacy_steam_id_gs\x18\x01 \x01(\x06\x12\x19\n\x11legacy_query_port\x18\x03 \x01(\r\"\x82\x01\n\x18\x43MsgClientGMSServerQuery\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x17\n\x0fgeo_location_ip\x18\x02 \x01(\r\x12\x13\n\x0bregion_code\x18\x03 \x01(\r\x12\x13\n\x0b\x66ilter_text\x18\x04 \x01(\t\x12\x13\n\x0bmax_servers\x18\x05 \x01(\r\"\xa5\x07\n CMsgGMSClientServerQueryResponse\x12\x39\n\x07servers\x18\x01 \x03(\x0b\x32(.CMsgGMSClientServerQueryResponse.Server\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x45\n\x13\x64\x65\x66\x61ult_server_data\x18\x03 \x01(\x0b\x32(.CMsgGMSClientServerQueryResponse.Server\x12\x16\n\x0eserver_strings\x18\x04 \x03(\t\x1a\xa0\x05\n\x06Server\x12\x1c\n\x14\x64\x65precated_server_ip\x18\x01 \x01(\r\x12\x12\n\nquery_port\x18\x02 \x01(\r\x12\x14\n\x0c\x61uth_players\x18\x03 \x01(\r\x12!\n\tserver_ip\x18\x04 \x01(\x0b\x32\x0e.CMsgIPAddress\x12\x10\n\x08steam_id\x18\x06 \x01(\x06\x12\x10\n\x08revision\x18\x07 \x01(\r\x12\x0f\n\x07players\x18\x08 \x01(\r\x12\x11\n\tgame_port\x18\t \x01(\r\x12\x11\n\tsdr_popid\x18\n \x01(\x07\x12\x19\n\x11sdr_ping_location\x18  \x01(\t\x12\r\n\x05\x66lags\x18\x0b \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x0c \x01(\r\x12\x13\n\x0bmax_players\x18\r \x01(\r\x12\x0c\n\x04\x62ots\x18\x0e \x01(\r\x12\x16\n\x0espectator_port\x18\x0f \x01(\r\x12\x13\n\x0bgamedir_str\x18\x10 \x01(\t\x12\x18\n\x10gamedir_strindex\x18\x11 \x01(\r\x12\x0f\n\x07map_str\x18\x12 \x01(\t\x12\x14\n\x0cmap_strindex\x18\x13 \x01(\r\x12\x10\n\x08name_str\x18\x14 \x01(\t\x12\x15\n\rname_strindex\x18\x15 \x01(\r\x12\x1c\n\x14game_description_str\x18\x16 \x01(\t\x12!\n\x19game_description_strindex\x18\x17 \x01(\r\x12\x13\n\x0bversion_str\x18\x18 \x01(\t\x12\x18\n\x10version_strindex\x18\x19 \x01(\r\x12\x14\n\x0cgametype_str\x18\x1a \x01(\t\x12\x19\n\x11gametype_strindex\x18\x1b \x01(\r\x12\x1a\n\x12spectator_name_str\x18\x1e \x01(\t\x12\x1f\n\x17spectator_name_strindex\x18\x1f \x01(\r\"5\n\x06\x45\x46lags\x12\x17\n\x13k_EFlag_HasPassword\x10\x01\x12\x12\n\x0ek_EFlag_Secure\x10\x02\"O\n\x17\x43MsgGameServerOutOfDate\x12\x13\n\x0bsteam_id_gs\x18\x01 \x01(\x06\x12\x0e\n\x06reject\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\"0\n\x17\x43MsgGSAssociateWithClan\x12\x15\n\rsteam_id_clan\x18\x01 \x01(\x06\"L\n\x1f\x43MsgGSAssociateWithClanResponse\x12\x15\n\rsteam_id_clan\x18\x01 \x01(\x06\x12\x12\n\x07\x65result\x18\x02 \x01(\r:\x01\x32\"A\n#CMsgGSComputeNewPlayerCompatibility\x12\x1a\n\x12steam_id_candidate\x18\x01 \x01(\x06\"\xcf\x01\n+CMsgGSComputeNewPlayerCompatibilityResponse\x12\x1a\n\x12steam_id_candidate\x18\x01 \x01(\x06\x12\x12\n\x07\x65result\x18\x02 \x01(\r:\x01\x32\x12\x16\n\x0eis_clan_member\x18\x03 \x01(\x08\x12\x18\n\x10\x63t_dont_like_you\x18\x04 \x01(\x05\x12\x18\n\x10\x63t_you_dont_like\x18\x05 \x01(\x05\x12$\n\x1c\x63t_clanmembers_dont_like_you\x18\x06 \x01(\x05\x42\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_clientserver_gameservers_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGGSSERVERTYPE']._serialized_start=75
  _globals['_CMSGGSSERVERTYPE']._serialized_end=312
  _globals['_CMSGGSSTATUSREPLY']._serialized_start=314
  _globals['_CMSGGSSTATUSREPLY']._serialized_end=352
  _globals['_CMSGGSPLAYERLIST']._serialized_start=355
  _globals['_CMSGGSPLAYERLIST']._serialized_end=524
  _globals['_CMSGGSPLAYERLIST_PLAYER']._serialized_start=418
  _globals['_CMSGGSPLAYERLIST_PLAYER']._serialized_end=524
  _globals['_CMSGGSUSERPLAYING']._serialized_start=526
  _globals['_CMSGGSUSERPLAYING']._serialized_end=643
  _globals['_CMSGGSDISCONNECTNOTICE']._serialized_start=645
  _globals['_CMSGGSDISCONNECTNOTICE']._serialized_end=687
  _globals['_CMSGGAMESERVERDATA']._serialized_start=690
  _globals['_CMSGGAMESERVERDATA']._serialized_end=1225
  _globals['_CMSGGAMESERVERDATA_PLAYER']._serialized_start=1199
  _globals['_CMSGGAMESERVERDATA_PLAYER']._serialized_end=1225
  _globals['_CMSGGAMESERVERREMOVE']._serialized_start=1227
  _globals['_CMSGGAMESERVERREMOVE']._serialized_end=1304
  _globals['_CMSGCLIENTGMSSERVERQUERY']._serialized_start=1307
  _globals['_CMSGCLIENTGMSSERVERQUERY']._serialized_end=1437
  _globals['_CMSGGMSCLIENTSERVERQUERYRESPONSE']._serialized_start=1440
  _globals['_CMSGGMSCLIENTSERVERQUERYRESPONSE']._serialized_end=2373
  _globals['_CMSGGMSCLIENTSERVERQUERYRESPONSE_SERVER']._serialized_start=1646
  _globals['_CMSGGMSCLIENTSERVERQUERYRESPONSE_SERVER']._serialized_end=2318
  _globals['_CMSGGMSCLIENTSERVERQUERYRESPONSE_EFLAGS']._serialized_start=2320
  _globals['_CMSGGMSCLIENTSERVERQUERYRESPONSE_EFLAGS']._serialized_end=2373
  _globals['_CMSGGAMESERVEROUTOFDATE']._serialized_start=2375
  _globals['_CMSGGAMESERVEROUTOFDATE']._serialized_end=2454
  _globals['_CMSGGSASSOCIATEWITHCLAN']._serialized_start=2456
  _globals['_CMSGGSASSOCIATEWITHCLAN']._serialized_end=2504
  _globals['_CMSGGSASSOCIATEWITHCLANRESPONSE']._serialized_start=2506
  _globals['_CMSGGSASSOCIATEWITHCLANRESPONSE']._serialized_end=2582
  _globals['_CMSGGSCOMPUTENEWPLAYERCOMPATIBILITY']._serialized_start=2584
  _globals['_CMSGGSCOMPUTENEWPLAYERCOMPATIBILITY']._serialized_end=2649
  _globals['_CMSGGSCOMPUTENEWPLAYERCOMPATIBILITYRESPONSE']._serialized_start=2652
  _globals['_CMSGGSCOMPUTENEWPLAYERCOMPATIBILITYRESPONSE']._serialized_end=2859
# @@protoc_insertion_point(module_scope)
