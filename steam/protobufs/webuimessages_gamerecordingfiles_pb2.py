# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: webuimessages_gamerecordingfiles.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.enums_pb2 as enums__pb2
import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.webuimessages_base_pb2 as webuimessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&webuimessages_gamerecordingfiles.proto\x1a\x0b\x65nums.proto\x1a\x18steammessages_base.proto\x1a\x18webuimessages_base.proto\"\xbc\x01\n\x12\x43GameRecordingFile\x12\x32\n\ttimelines\x18\x01 \x03(\x0b\x32\x1f.CGameRecordingTimelineMetadata\x12\x37\n\x0fpostgame_events\x18\x02 \x03(\x0b\x32\x1e.CGameRecordingPostGameSummary\x12\x17\n\x0ftemporary_clips\x18\x03 \x03(\t\x12 \n\x04tags\x18\x04 \x03(\x0b\x32\x12.CGameRecordingTag\"\xc1\x03\n\x16\x43GameRecordingClipFile\x12\x32\n\ttimelines\x18\x01 \x03(\x0b\x32\x1f.CGameRecordingTimelineMetadata\x12&\n\x1e\x66irst_timeline_start_offset_ms\x18\x02 \x01(\x04\x12\x15\n\rdate_recorded\x18\x03 \x01(\r\x12\x0f\n\x07game_id\x18\x04 \x01(\x04\x12\x19\n\x11published_file_id\x18\x05 \x01(\x06\x12\x15\n\rsize_in_bytes\x18\x06 \x01(\x04\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x11\n\ttemporary\x18\x08 \x01(\x08\x12\x17\n\x0foriginal_device\x18\t \x01(\t\x12#\n\x1boriginal_gaming_device_type\x18\n \x01(\r\x12\x17\n\x0f\x64\x61te_downloaded\x18\x0b \x01(\r\x12\x17\n\x0fthumbnail_width\x18\x0c \x01(\r\x12\x18\n\x10thumbnail_height\x18\r \x01(\r\x12 \n\x04tags\x18\x0e \x03(\x0b\x32\x12.CGameRecordingTag\x12$\n\x06phases\x18\x0f \x03(\x0b\x32\x14.CGameRecordingPhase\"\xe0\x04\n\x1e\x43GameRecordingTimelineMetadata\x12\x13\n\x0btimeline_id\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\x04\x12\x15\n\rdate_recorded\x18\x03 \x01(\r\x12\x13\n\x0b\x64uration_ms\x18\x04 \x01(\x04\x12=\n\nrecordings\x18\x05 \x03(\x0b\x32).CGameRecordingTimelineMetadata.Recording\x12$\n\x06phases\x18\x06 \x03(\x0b\x32\x14.CGameRecordingPhase\x12\x38\n\x12significant_events\x18\x07 \x03(\x0b\x32\x1c.CGameRecordingTimelineEvent\x1a\xcc\x02\n\tRecording\x12\x14\n\x0crecording_id\x18\x01 \x01(\t\x12\x17\n\x0fstart_offset_ms\x18\x02 \x01(\x04\x12\x13\n\x0b\x64uration_ms\x18\x03 \x01(\x04\x12I\n\x0erecording_type\x18\x04 \x01(\x0e\x32\x13.EGameRecordingType:\x1ck_EGameRecordingType_Unknown\x12\x19\n\x11\x64\x65lete_on_cleanup\x18\x05 \x01(\x08\x12\x1d\n\x15video_manager_clip_id\x18\x06 \x01(\x04\x12\x1e\n\x16video_manager_video_id\x18\x07 \x01(\x04\x12\x18\n\x10\x63\x64n_manifest_url\x18\x08 \x01(\t\x12\x11\n\tfile_size\x18\t \x01(\x04\x12)\n!recording_zero_timeline_offset_ms\x18\n \x01(\x04\"^\n\x1d\x43GameRecordingPostGameSummary\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12,\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x1c.CGameRecordingTimelineEvent\"\xf1\x01\n\x1b\x43GameRecordingTimelineEvent\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x12\n\nrt_created\x18\x02 \x01(\r\x12\x15\n\rpossible_clip\x18\x03 \x01(\x05\x12\x13\n\x0btimeline_id\x18\x04 \x01(\t\x12\x10\n\x08\x65ntry_id\x18\x05 \x01(\x04\x12\x1a\n\x12timeline_offset_ms\x18\x06 \x01(\x04\x12\x13\n\x0b\x64uration_ms\x18\x07 \x01(\x04\x12\x13\n\x0bmarker_icon\x18\x08 \x01(\t\x12\x14\n\x0cmarker_title\x18\t \x01(\t\x12\x13\n\x0buser_marker\x18\n \x01(\x08\"\xb6\x01\n\x11\x43GameRecordingTag\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x1a\n\x03tag\x18\x02 \x01(\x0b\x32\r.CTimelineTag\x12/\n\nreferences\x18\x03 \x03(\x0b\x32\x1b.CGameRecordingTag.Timeline\x1a\x43\n\x08Timeline\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\x12\x13\n\x0btimeline_id\x18\x02 \x01(\t\x12\x11\n\toffset_ms\x18\x03 \x01(\x04\"s\n\x19\x43GameRecordingTagInstance\x12\x13\n\x0btimeline_id\x18\x01 \x01(\t\x12\x10\n\x08\x65ntry_id\x18\x02 \x01(\x04\x12\x1a\n\x12timeline_offset_ms\x18\x03 \x01(\x04\x12\x13\n\x0b\x64uration_ms\x18\x04 \x01(\x04\"\x84\x02\n\x13\x43GameRecordingPhase\x12\x10\n\x08phase_id\x18\x04 \x01(\t\x12\x13\n\x0b\x64uration_ms\x18\x05 \x01(\x04\x12&\n\x04tags\x18\x06 \x03(\x0b\x32\x18.CGameRecordingPhase.Tag\x12\x30\n\x0e\x63ontained_tags\x18\x07 \x03(\x0b\x32\x18.CGameRecordingPhase.Tag\x12\"\n\x1a\x62\x61\x63kground_timeline_offset\x18\x08 \x01(\x04\x12$\n\nattributes\x18\t \x03(\x0b\x32\x10.CPhaseAttribute\x1a\"\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\"K\n\x0c\x43TimelineTag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x10\n\x08priority\x18\x04 \x01(\r\"A\n\x0f\x43PhaseAttribute\x12\r\n\x05group\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x10\n\x08priority\x18\x03 \x01(\rB\x05H\x01\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webuimessages_gamerecordingfiles_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\001'
  _globals['_CGAMERECORDINGFILE']._serialized_start=108
  _globals['_CGAMERECORDINGFILE']._serialized_end=296
  _globals['_CGAMERECORDINGCLIPFILE']._serialized_start=299
  _globals['_CGAMERECORDINGCLIPFILE']._serialized_end=748
  _globals['_CGAMERECORDINGTIMELINEMETADATA']._serialized_start=751
  _globals['_CGAMERECORDINGTIMELINEMETADATA']._serialized_end=1359
  _globals['_CGAMERECORDINGTIMELINEMETADATA_RECORDING']._serialized_start=1027
  _globals['_CGAMERECORDINGTIMELINEMETADATA_RECORDING']._serialized_end=1359
  _globals['_CGAMERECORDINGPOSTGAMESUMMARY']._serialized_start=1361
  _globals['_CGAMERECORDINGPOSTGAMESUMMARY']._serialized_end=1455
  _globals['_CGAMERECORDINGTIMELINEEVENT']._serialized_start=1458
  _globals['_CGAMERECORDINGTIMELINEEVENT']._serialized_end=1699
  _globals['_CGAMERECORDINGTAG']._serialized_start=1702
  _globals['_CGAMERECORDINGTAG']._serialized_end=1884
  _globals['_CGAMERECORDINGTAG_TIMELINE']._serialized_start=1817
  _globals['_CGAMERECORDINGTAG_TIMELINE']._serialized_end=1884
  _globals['_CGAMERECORDINGTAGINSTANCE']._serialized_start=1886
  _globals['_CGAMERECORDINGTAGINSTANCE']._serialized_end=2001
  _globals['_CGAMERECORDINGPHASE']._serialized_start=2004
  _globals['_CGAMERECORDINGPHASE']._serialized_end=2264
  _globals['_CGAMERECORDINGPHASE_TAG']._serialized_start=2230
  _globals['_CGAMERECORDINGPHASE_TAG']._serialized_end=2264
  _globals['_CTIMELINETAG']._serialized_start=2266
  _globals['_CTIMELINETAG']._serialized_end=2341
  _globals['_CPHASEATTRIBUTE']._serialized_start=2343
  _globals['_CPHASEATTRIBUTE']._serialized_end=2408
# @@protoc_insertion_point(module_scope)
