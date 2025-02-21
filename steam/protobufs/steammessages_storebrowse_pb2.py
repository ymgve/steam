# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_storebrowse.proto
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
import steam.protobufs.enums_productinfo_pb2 as enums__productinfo__pb2
import steam.protobufs.enums_pb2 as enums__pb2
import steam.protobufs.contenthubs_pb2 as contenthubs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsteammessages_storebrowse.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\x1a\x17\x65nums_productinfo.proto\x1a\x0b\x65nums.proto\x1a\x11\x63ontenthubs.proto\"z\n\x0bStoreItemID\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\tpackageid\x18\x02 \x01(\r\x12\x10\n\x08\x62undleid\x18\x03 \x01(\r\x12\r\n\x05tagid\x18\x04 \x01(\r\x12\x11\n\tcreatorid\x18\x05 \x01(\r\x12\x15\n\rhubcategoryid\x18\x06 \x01(\r\"d\n\x12StoreBrowseContext\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x11\n\telanguage\x18\x02 \x01(\x05\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\x12\x13\n\x0bsteam_realm\x18\x04 \x01(\x05\"\xb3\x04\n\x1aStoreBrowseItemDataRequest\x12\x16\n\x0einclude_assets\x18\x01 \x01(\x08\x12\x17\n\x0finclude_release\x18\x02 \x01(\x08\x12\x19\n\x11include_platforms\x18\x03 \x01(\x08\x12$\n\x1cinclude_all_purchase_options\x18\x04 \x01(\x08\x12\x1b\n\x13include_screenshots\x18\x05 \x01(\x08\x12\x18\n\x10include_trailers\x18\x06 \x01(\x08\x12\x17\n\x0finclude_ratings\x18\x07 \x01(\x08\x12\x19\n\x11include_tag_count\x18\x08 \x01(\x05\x12\x17\n\x0finclude_reviews\x18\t \x01(\x08\x12\x1a\n\x12include_basic_info\x18\n \x01(\x08\x12#\n\x1binclude_supported_languages\x18\x0b \x01(\x08\x12 \n\x18include_full_description\x18\x0c \x01(\x08\x12\x1e\n\x16include_included_items\x18\r \x01(\x08\x12?\n\x1aincluded_item_data_request\x18\x0e \x01(\x0b\x32\x1b.StoreBrowseItemDataRequest\x12(\n include_assets_without_overrides\x18\x0f \x01(\x08\x12\x1a\n\x12\x61pply_user_filters\x18\x10 \x01(\x08\x12\x15\n\rinclude_links\x18\x11 \x01(\x08\"\x93\x01\n\x1d\x43StoreBrowse_GetItems_Request\x12\x19\n\x03ids\x18\x01 \x03(\x0b\x32\x0c.StoreItemID\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.StoreBrowseContext\x12\x31\n\x0c\x64\x61ta_request\x18\x03 \x01(\x0b\x32\x1b.StoreBrowseItemDataRequest\"\x95,\n\tStoreItem\x12<\n\titem_type\x18\x01 \x01(\x0e\x32\x0f.EStoreItemType:\x18k_EStoreItemType_Invalid\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0f\n\x07success\x18\x03 \x01(\r\x12\x0f\n\x07visible\x18\x04 \x01(\x08\x12*\n\"unvailable_for_country_restriction\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x16\n\x0estore_url_path\x18\x07 \x01(\t\x12\r\n\x05\x61ppid\x18\t \x01(\r\x12\x32\n\x04type\x18\n \x01(\x0e\x32\x0e.EStoreAppType:\x14k_EStoreAppType_Game\x12&\n\x0eincluded_types\x18\x0b \x03(\x0e\x32\x0e.EStoreAppType\x12\x17\n\x0fincluded_appids\x18\x0c \x03(\r\x12\x0f\n\x07is_free\x18\r \x01(\x08\x12\x17\n\x0fis_early_access\x18\x0e \x01(\x08\x12.\n\rrelated_items\x18\x0f \x01(\x0b\x32\x17.StoreItem.RelatedItems\x12\x30\n\x0eincluded_items\x18\x10 \x01(\x0b\x32\x18.StoreItem.IncludedItems\x12\x34\n\x15\x63ontent_descriptorids\x18\x14 \x03(\x0e\x32\x15.EContentDescriptorID\x12\x0e\n\x06tagids\x18\x15 \x03(\r\x12)\n\ncategories\x18\x16 \x01(\x0b\x32\x15.StoreItem.Categories\x12#\n\x07reviews\x18\x17 \x01(\x0b\x32\x12.StoreItem.Reviews\x12(\n\nbasic_info\x18\x18 \x01(\x0b\x32\x14.StoreItem.BasicInfo\x12\x1c\n\x04tags\x18\x19 \x03(\x0b\x32\x0e.StoreItem.Tag\x12!\n\x06\x61ssets\x18\x1e \x01(\x0b\x32\x11.StoreItem.Assets\x12\'\n\x07release\x18\x1f \x01(\x0b\x32\x16.StoreItem.ReleaseInfo\x12\'\n\tplatforms\x18  \x01(\x0b\x32\x14.StoreItem.Platforms\x12%\n\x0bgame_rating\x18! \x01(\x0b\x32\x10.StoreGameRating\x12\x16\n\x0eis_coming_soon\x18\" \x01(\x08\x12\x37\n\x14\x62\x65st_purchase_option\x18( \x01(\x0b\x32\x19.StoreItem.PurchaseOption\x12\x33\n\x10purchase_options\x18) \x03(\x0b\x32\x19.StoreItem.PurchaseOption\x12.\n\x0b\x61\x63\x63\x65ssories\x18* \x03(\x0b\x32\x19.StoreItem.PurchaseOption\x12\x37\n\x14self_purchase_option\x18+ \x01(\x0b\x32\x19.StoreItem.PurchaseOption\x12+\n\x0bscreenshots\x18\x32 \x01(\x0b\x32\x16.StoreItem.Screenshots\x12%\n\x08trailers\x18\x33 \x01(\x0b\x32\x13.StoreItem.Trailers\x12\x39\n\x13supported_languages\x18\x34 \x03(\x0b\x32\x1c.StoreItem.SupportedLanguage\x12\x1f\n\x17store_url_path_override\x18\x35 \x01(\t\x12,\n\x0c\x66ree_weekend\x18\x36 \x01(\x0b\x32\x16.StoreItem.FreeWeekend\x12\x10\n\x08unlisted\x18\x37 \x01(\x08\x12\x12\n\ngame_count\x18\x38 \x01(\r\x12\x15\n\rinternal_name\x18\x39 \x01(\t\x12\x18\n\x10\x66ull_description\x18: \x01(\t\x12\x1b\n\x13is_free_temporarily\x18; \x01(\x08\x12\x33\n\x18\x61ssets_without_overrides\x18< \x01(\x0b\x32\x11.StoreItem.Assets\x12\x36\n\x13user_filter_failure\x18\x46 \x01(\x0b\x32\x19.StoreBrowseFilterFailure\x12\x1e\n\x05links\x18G \x03(\x0b\x32\x0f.StoreItem.Link\x1aW\n\x0cRelatedItems\x12\x14\n\x0cparent_appid\x18\x01 \x01(\r\x12\x12\n\ndemo_appid\x18\x02 \x03(\r\x12\x1d\n\x15standalone_demo_appid\x18\x03 \x03(\r\x1aY\n\rIncludedItems\x12!\n\rincluded_apps\x18\x01 \x03(\x0b\x32\n.StoreItem\x12%\n\x11included_packages\x18\x02 \x03(\x0b\x32\n.StoreItem\x1ao\n\nCategories\x12$\n\x1csupported_player_categoryids\x18\x02 \x03(\r\x12\x1b\n\x13\x66\x65\x61ture_categoryids\x18\x03 \x03(\r\x12\x1e\n\x16\x63ontroller_categoryids\x18\x04 \x03(\r\x1a\xb2\x02\n\x07Reviews\x12?\n\x10summary_filtered\x18\x01 \x01(\x0b\x32%.StoreItem.Reviews.StoreReviewSummary\x12\x41\n\x12summary_unfiltered\x18\x02 \x01(\x0b\x32%.StoreItem.Reviews.StoreReviewSummary\x1a\xa2\x01\n\x12StoreReviewSummary\x12\x14\n\x0creview_count\x18\x01 \x01(\r\x12\x18\n\x10percent_positive\x18\x02 \x01(\x05\x12@\n\x0creview_score\x18\x03 \x01(\x0e\x32\x11.EUserReviewScore:\x17k_EUserReviewScore_None\x12\x1a\n\x12review_score_label\x18\x04 \x01(\t\x1a\xb0\x02\n\tBasicInfo\x12\x19\n\x11short_description\x18\x01 \x01(\t\x12\x38\n\npublishers\x18\x02 \x03(\x0b\x32$.StoreItem.BasicInfo.CreatorHomeLink\x12\x38\n\ndevelopers\x18\x03 \x03(\x0b\x32$.StoreItem.BasicInfo.CreatorHomeLink\x12\x38\n\nfranchises\x18\x04 \x03(\x0b\x32$.StoreItem.BasicInfo.CreatorHomeLink\x12\x18\n\x10\x63\x61psule_headline\x18\x05 \x01(\t\x1a@\n\x0f\x43reatorHomeLink\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x17\x63reator_clan_account_id\x18\x02 \x01(\r\x1a$\n\x03Tag\x12\r\n\x05tagid\x18\x01 \x01(\r\x12\x0e\n\x06weight\x18\x02 \x01(\r\x1a\xd0\x02\n\x06\x41ssets\x12\x18\n\x10\x61sset_url_format\x18\x01 \x01(\t\x12\x14\n\x0cmain_capsule\x18\x02 \x01(\t\x12\x15\n\rsmall_capsule\x18\x03 \x01(\t\x12\x0e\n\x06header\x18\x04 \x01(\t\x12\x16\n\x0epackage_header\x18\x05 \x01(\t\x12\x17\n\x0fpage_background\x18\x06 \x01(\t\x12\x14\n\x0chero_capsule\x18\x07 \x01(\t\x12\x17\n\x0fhero_capsule_2x\x18\x08 \x01(\t\x12\x17\n\x0flibrary_capsule\x18\t \x01(\t\x12\x1a\n\x12library_capsule_2x\x18\n \x01(\t\x12\x14\n\x0clibrary_hero\x18\x0b \x01(\t\x12\x17\n\x0flibrary_hero_2x\x18\x0c \x01(\t\x12\x16\n\x0e\x63ommunity_icon\x18\r \x01(\t\x12\x13\n\x0b\x63lan_avatar\x18\x0e \x01(\t\x1a\xcc\x02\n\x0bReleaseInfo\x12\x1a\n\x12steam_release_date\x18\x01 \x01(\r\x12\x1d\n\x15original_release_date\x18\x02 \x01(\r\x12#\n\x1boriginal_steam_release_date\x18\x03 \x01(\r\x12\x16\n\x0eis_coming_soon\x18\x04 \x01(\x08\x12\x12\n\nis_preload\x18\x05 \x01(\x08\x12#\n\x1b\x63ustom_release_date_message\x18\x06 \x01(\t\x12 \n\x18is_abridged_release_date\x18\x07 \x01(\x08\x12\x1b\n\x13\x63oming_soon_display\x18\x08 \x01(\t\x12\x17\n\x0fis_early_access\x18\n \x01(\x08\x12\x18\n\x10mac_release_date\x18\x14 \x01(\r\x12\x1a\n\x12linux_release_date\x18\x15 \x01(\r\x1a\xe5\x02\n\tPlatforms\x12\x0f\n\x07windows\x18\x01 \x01(\x08\x12\x0b\n\x03mac\x18\x02 \x01(\x08\x12\x15\n\rsteamos_linux\x18\x03 \x01(\x08\x12\x32\n\nvr_support\x18\n \x01(\x0b\x32\x1e.StoreItem.Platforms.VRSupport\x12o\n\x1asteam_deck_compat_category\x18\x0b \x01(\x0e\x32 .ESteamDeckCompatibilityCategory:)k_ESteamDeckCompatibilityCategory_Unknown\x1a~\n\tVRSupport\x12\r\n\x05vrhmd\x18\x01 \x01(\x08\x12\x12\n\nvrhmd_only\x18\x02 \x01(\x08\x12\x10\n\x08htc_vive\x18( \x01(\x08\x12\x13\n\x0boculus_rift\x18) \x01(\x08\x12\x12\n\nwindows_mr\x18* \x01(\x08\x12\x13\n\x0bvalve_index\x18+ \x01(\x08\x1a\xa8\x08\n\x0ePurchaseOption\x12\x11\n\tpackageid\x18\x01 \x01(\x05\x12\x10\n\x08\x62undleid\x18\x02 \x01(\x05\x12\x1c\n\x14purchase_option_name\x18\x03 \x01(\t\x12\x1c\n\x14\x66inal_price_in_cents\x18\x05 \x01(\x03\x12\x1f\n\x17original_price_in_cents\x18\x06 \x01(\x03\x12\x1d\n\x15\x66ormatted_final_price\x18\x08 \x01(\t\x12 \n\x18\x66ormatted_original_price\x18\t \x01(\t\x12\x14\n\x0c\x64iscount_pct\x18\n \x01(\x05\x12\x1b\n\x13\x62undle_discount_pct\x18\x0c \x01(\x05\x12\x17\n\x0fis_free_to_keep\x18\r \x01(\x08\x12$\n\x1cprice_before_bundle_discount\x18\x0e \x01(\x03\x12.\n&formatted_price_before_bundle_discount\x18\x0f \x01(\t\x12<\n\x10\x61\x63tive_discounts\x18\x14 \x03(\x0b\x32\".StoreItem.PurchaseOption.Discount\x12!\n\x19user_can_purchase_as_gift\x18\x1f \x01(\x08\x12\x1d\n\x15is_commercial_license\x18( \x01(\x08\x12$\n\x1cshould_suppress_discount_pct\x18) \x01(\x08\x12/\n hide_discount_pct_for_compliance\x18* \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x13included_game_count\x18+ \x01(\x05:\x01\x31\x12$\n\x1clowest_recent_price_in_cents\x18, \x01(\x03\x12\x19\n\x11requires_shipping\x18- \x01(\x08\x12\x41\n\x0frecurrence_info\x18. \x01(\x0b\x32(.StoreItem.PurchaseOption.RecurrenceInfo\x12\x19\n\x11\x66ree_to_keep_ends\x18/ \x01(\r\x1a\\\n\x08\x44iscount\x12\x17\n\x0f\x64iscount_amount\x18\x01 \x01(\x03\x12\x1c\n\x14\x64iscount_description\x18\x02 \x01(\t\x12\x19\n\x11\x64iscount_end_date\x18\x03 \x01(\r\x1a\xbc\x01\n\x0eRecurrenceInfo\x12\x11\n\tpackageid\x18\x01 \x01(\x05\x12\x1e\n\x16\x62illing_agreement_type\x18\x02 \x01(\x05\x12\x19\n\x11renewal_time_unit\x18\x03 \x01(\x05\x12\x1b\n\x13renewal_time_period\x18\x04 \x01(\x05\x12\x1e\n\x16renewal_price_in_cents\x18\x05 \x01(\x03\x12\x1f\n\x17\x66ormatted_renewal_price\x18\x06 \x01(\t\x1a\xc6\x01\n\x0bScreenshots\x12?\n\x14\x61ll_ages_screenshots\x18\x02 \x03(\x0b\x32!.StoreItem.Screenshots.Screenshot\x12\x45\n\x1amature_content_screenshots\x18\x03 \x03(\x0b\x32!.StoreItem.Screenshots.Screenshot\x1a/\n\nScreenshot\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0f\n\x07ordinal\x18\x02 \x01(\x05\x1a\x97\x04\n\x08Trailers\x12/\n\nhighlights\x18\x01 \x03(\x0b\x32\x1b.StoreItem.Trailers.Trailer\x12\x33\n\x0eother_trailers\x18\x02 \x03(\x0b\x32\x1b.StoreItem.Trailers.Trailer\x1a-\n\x0bVideoSource\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x1a\xf5\x02\n\x07Trailer\x12\x14\n\x0ctrailer_name\x18\x01 \x01(\t\x12\x1a\n\x12trailer_url_format\x18\x02 \x01(\t\x12G\n\x10trailer_category\x18\r \x01(\x0e\x32\x11.ETrailerCategory:\x1ak_ETrailerCategory_Invalid\x12\x35\n\x0ctrailer_480p\x18\x03 \x03(\x0b\x32\x1f.StoreItem.Trailers.VideoSource\x12\x34\n\x0btrailer_max\x18\x04 \x03(\x0b\x32\x1f.StoreItem.Trailers.VideoSource\x12\x35\n\x0cmicrotrailer\x18\x05 \x03(\x0b\x32\x1f.StoreItem.Trailers.VideoSource\x12\x19\n\x11screenshot_medium\x18\n \x01(\t\x12\x17\n\x0fscreenshot_full\x18\x0b \x01(\t\x12\x17\n\x0ftrailer_base_id\x18\x0c \x01(\x05\x1a\x85\x01\n\x11SupportedLanguage\x12\x15\n\telanguage\x18\x01 \x01(\x05:\x02-1\x12\x1f\n\x13\x65\x61\x64\x64itionallanguage\x18\x05 \x01(\x05:\x02-1\x12\x11\n\tsupported\x18\x02 \x01(\x08\x12\x12\n\nfull_audio\x18\x03 \x01(\x08\x12\x11\n\tsubtitles\x18\x04 \x01(\x08\x1a\x41\n\x0b\x46reeWeekend\x12\x12\n\nstart_time\x18\x01 \x01(\r\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\r\x12\x0c\n\x04text\x18\x03 \x01(\t\x1a\\\n\x04Link\x12\x39\n\tlink_type\x18\x01 \x01(\x0e\x32\x0f.EStoreLinkType:\x15k_EStoreLinkType_None\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\"\xb7\x01\n\x0fStoreGameRating\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06rating\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scriptors\x18\x03 \x03(\t\x12\x1c\n\x14interactive_elements\x18\x04 \x01(\t\x12\x14\n\x0crequired_age\x18\n \x01(\x05\x12\x14\n\x0cuse_age_gate\x18\x0b \x01(\x08\x12\x11\n\timage_url\x18\x14 \x01(\t\x12\x14\n\x0cimage_target\x18\x15 \x01(\t\"\xa1\x03\n\x18StoreBrowseFilterFailure\x12T\n\x0e\x66ilter_failure\x18\x01 \x01(\x0e\x32\x1a.EStoreBrowseFilterFailure: k_EStoreBrowseFilterFailure_None\x12\x15\n\ralready_owned\x18\x05 \x01(\x08\x12\x13\n\x0bon_wishlist\x18\x06 \x01(\x08\x12\x0f\n\x07ignored\x18\x07 \x01(\x08\x12\x1d\n\x15not_in_users_language\x18\n \x01(\x08\x12\x1d\n\x15not_on_users_platform\x18\x0b \x01(\x08\x12\x1b\n\x13\x64\x65mo_for_owned_game\x18\x0c \x01(\x08\x12\x1c\n\x14\x64lc_for_unowned_game\x18\r \x01(\x08\x12!\n\x19nonpreferred_product_type\x18\x14 \x01(\x08\x12\x17\n\x0f\x65xcluded_tagids\x18\x15 \x03(\r\x12=\n\x1e\x65xcluded_content_descriptorids\x18\x1e \x03(\x0e\x32\x15.EContentDescriptorID\"A\n\x1e\x43StoreBrowse_GetItems_Response\x12\x1f\n\x0bstore_items\x18\x01 \x03(\x0b\x32\n.StoreItem\"R\n\'CStoreBrowse_GetStoreCategories_Request\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x15\n\telanguage\x18\x02 \x01(\x05:\x02-1\"\xea\x02\n(CStoreBrowse_GetStoreCategories_Response\x12\x46\n\ncategories\x18\x01 \x03(\x0b\x32\x32.CStoreBrowse_GetStoreCategories_Response.Category\x1a\xf5\x01\n\x08\x43\x61tegory\x12\x12\n\ncategoryid\x18\x01 \x01(\r\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x13.EStoreCategoryType:\x1dk_EStoreCategoryType_Category\x12\x15\n\rinternal_name\x18\x03 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\x12\x11\n\timage_url\x18\x05 \x01(\t\x12\x16\n\x0eshow_in_search\x18\x06 \x01(\x08\x12\x10\n\x08\x63omputed\x18\x07 \x01(\x08\x12\x10\n\x08\x65\x64it_url\x18\x08 \x01(\t\x12\x17\n\x0f\x65\x64it_sort_order\x18\t \x01(\r\"Q\n\"CStoreBrowse_GetPriceStops_Request\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12\x15\n\rcurrency_code\x18\x02 \x01(\t\"\xc1\x01\n#CStoreBrowse_GetPriceStops_Response\x12\x43\n\x0bprice_stops\x18\x01 \x03(\x0b\x32..CStoreBrowse_GetPriceStops_Response.PriceStop\x12\x15\n\rcurrency_code\x18\x02 \x01(\t\x1a>\n\tPriceStop\x12\x18\n\x10\x66ormatted_amount\x18\x01 \x01(\t\x12\x17\n\x0f\x61mount_in_cents\x18\x02 \x01(\x03\"\xa7\x01\n\"CStoreBrowse_GetDLCForApps_Request\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.StoreBrowseContext\x12,\n\x11store_page_filter\x18\x02 \x01(\x0b\x32\x11.CStorePageFilter\x12\x1c\n\x06\x61ppids\x18\x03 \x03(\x0b\x32\x0c.StoreItemID\x12\x0f\n\x07steamid\x18\x04 \x01(\x04\"\xfe\x02\n#CStoreBrowse_GetDLCForApps_Response\x12>\n\x08\x64lc_data\x18\x01 \x03(\x0b\x32,.CStoreBrowse_GetDLCForApps_Response.DLCData\x12\x45\n\x08playtime\x18\x02 \x03(\x0b\x32\x33.CStoreBrowse_GetDLCForApps_Response.PlaytimeForApp\x1a\x87\x01\n\x07\x44LCData\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x13\n\x0bparentappid\x18\x02 \x01(\r\x12\x14\n\x0crelease_date\x18\x03 \x01(\r\x12\x13\n\x0b\x63oming_soon\x18\x04 \x01(\x08\x12\r\n\x05price\x18\x05 \x01(\x03\x12\x10\n\x08\x64iscount\x18\x06 \x01(\r\x12\x0c\n\x04\x66ree\x18\x07 \x01(\x08\x1a\x46\n\x0ePlaytimeForApp\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08playtime\x18\x02 \x01(\r\x12\x13\n\x0blast_played\x18\x03 \x01(\r\"\xab\x01\n&CStoreBrowse_GetDLCForAppsSolr_Request\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.StoreBrowseContext\x12\x0e\n\x06\x61ppids\x18\x02 \x03(\r\x12\x0e\n\x06\x66lavor\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\r\x12,\n\x11store_page_filter\x18\x05 \x01(\x0b\x32\x11.CStorePageFilter\"\xa3\x01\n\'CStoreBrowse_GetDLCForAppsSolr_Response\x12\x43\n\tdlc_lists\x18\x01 \x03(\x0b\x32\x30.CStoreBrowse_GetDLCForAppsSolr_Response.DLCList\x1a\x33\n\x07\x44LCList\x12\x14\n\x0cparent_appid\x18\x01 \x01(\r\x12\x12\n\ndlc_appids\x18\x02 \x03(\r\"`\n%CStoreBrowse_GetHardwareItems_Request\x12\x11\n\tpackageid\x18\x01 \x03(\r\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.StoreBrowseContext\"\x94\x04\n\x17\x43HardwarePackageDetails\x12\x11\n\tpackageid\x18\x01 \x01(\r\x12\x1b\n\x13inventory_available\x18\x03 \x01(\x08\x12\x1b\n\x13high_pending_orders\x18\x04 \x01(\x08\x12*\n\"account_restricted_from_purchasing\x18\x05 \x01(\x08\x12\x1c\n\x14requires_reservation\x18\x06 \x01(\x08\x12$\n\x1crtime_estimated_notification\x18\x07 \x01(\r\x12\x19\n\x11notificaton_token\x18\x08 \x01(\t\x12\x19\n\x11reservation_state\x18\t \x01(\x05\x12\x0f\n\x07\x65xpired\x18\n \x01(\x08\x12\x14\n\x0ctime_expires\x18\x0b \x01(\r\x12\x15\n\rtime_reserved\x18\x0c \x01(\r\x12\x1f\n\x17\x61llow_quantity_purchase\x18\r \x01(\x08\x12!\n\x19max_quantity_per_purchase\x18\x0e \x01(\x05\x12!\n\x19\x61llow_purchase_in_country\x18\x0f \x01(\x08\x12\x30\n(estimated_delivery_soonest_business_days\x18\x11 \x01(\r\x12/\n\'estimated_delivery_latest_business_days\x18\x12 \x01(\r\"S\n&CStoreBrowse_GetHardwareItems_Response\x12)\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x18.CHardwarePackageDetails*\x80\x02\n\x0e\x45StoreItemType\x12%\n\x18k_EStoreItemType_Invalid\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x18\n\x14k_EStoreItemType_App\x10\x00\x12\x1c\n\x18k_EStoreItemType_Package\x10\x01\x12\x1b\n\x17k_EStoreItemType_Bundle\x10\x02\x12\x18\n\x14k_EStoreItemType_Mtx\x10\x03\x12\x18\n\x14k_EStoreItemType_Tag\x10\x04\x12\x1c\n\x18k_EStoreItemType_Creator\x10\x05\x12 \n\x1ck_EStoreItemType_HubCategory\x10\x06*\xab\x03\n\rEStoreAppType\x12\x18\n\x14k_EStoreAppType_Game\x10\x00\x12\x18\n\x14k_EStoreAppType_Demo\x10\x01\x12\x17\n\x13k_EStoreAppType_Mod\x10\x02\x12\x19\n\x15k_EStoreAppType_Movie\x10\x03\x12\x17\n\x13k_EStoreAppType_DLC\x10\x04\x12\x19\n\x15k_EStoreAppType_Guide\x10\x05\x12\x1c\n\x18k_EStoreAppType_Software\x10\x06\x12\x19\n\x15k_EStoreAppType_Video\x10\x07\x12\x1a\n\x16k_EStoreAppType_Series\x10\x08\x12\x1b\n\x17k_EStoreAppType_Episode\x10\t\x12\x1c\n\x18k_EStoreAppType_Hardware\x10\n\x12\x19\n\x15k_EStoreAppType_Music\x10\x0b\x12\x18\n\x14k_EStoreAppType_Beta\x10\x0c\x12\x18\n\x14k_EStoreAppType_Tool\x10\r\x12\x1f\n\x1bk_EStoreAppType_Advertising\x10\x0e*\x85\x03\n\x10\x45UserReviewScore\x12\x1b\n\x17k_EUserReviewScore_None\x10\x00\x12-\n)k_EUserReviewScore_OverwhelminglyNegative\x10\x01\x12#\n\x1fk_EUserReviewScore_VeryNegative\x10\x02\x12\x1f\n\x1bk_EUserReviewScore_Negative\x10\x03\x12%\n!k_EUserReviewScore_MostlyNegative\x10\x04\x12\x1c\n\x18k_EUserReviewScore_Mixed\x10\x05\x12%\n!k_EUserReviewScore_MostlyPositive\x10\x06\x12\x1f\n\x1bk_EUserReviewScore_Positive\x10\x07\x12#\n\x1fk_EUserReviewScore_VeryPositive\x10\x08\x12-\n)k_EUserReviewScore_OverwhelminglyPositive\x10\t*\xf7\x01\n\x10\x45TrailerCategory\x12\x1e\n\x1ak_ETrailerCategory_Invalid\x10\x00\x12\x1f\n\x1bk_ETrailerCategory_Gameplay\x10\x01\x12\x1d\n\x19k_ETrailerCategory_Teaser\x10\x02\x12 \n\x1ck_ETrailerCategory_Cinematic\x10\x03\x12\x1d\n\x19k_ETrailerCategory_Update\x10\x04\x12 \n\x1ck_ETrailerCategory_Accolades\x10\x05\x12 \n\x1ck_ETrailerCategory_Interview\x10\x06*\xa7\x02\n\x19\x45StoreBrowseFilterFailure\x12$\n k_EStoreBrowseFilterFailure_None\x10\x00\x12)\n%k_EStoreBrowseFilterFailure_Redundant\x10\n\x12,\n(k_EStoreBrowseFilterFailure_NotPreferred\x10\x14\x12-\n)k_EStoreBrowseFilterFailure_NotInterested\x10\x1e\x12/\n+k_EStoreBrowseFilterFailure_UnwantedContent\x10(\x12+\n\'k_EStoreBrowseFilterFailure_Unavailable\x10\x32*\xcb\x05\n\x0e\x45StoreLinkType\x12\x19\n\x15k_EStoreLinkType_None\x10\x00\x12\x1c\n\x18k_EStoreLinkType_YouTube\x10\x01\x12\x1d\n\x19k_EStoreLinkType_Facebook\x10\x02\x12\x1c\n\x18k_EStoreLinkType_Twitter\x10\x03\x12\x1b\n\x17k_EStoreLinkType_Twitch\x10\x04\x12\x1c\n\x18k_EStoreLinkType_Discord\x10\x05\x12\x17\n\x13k_EStoreLinkType_QQ\x10\x06\x12\x17\n\x13k_EStoreLinkType_VK\x10\x07\x12\x1d\n\x19k_EStoreLinkType_Bilibili\x10\x08\x12\x1a\n\x16k_EStoreLinkType_Weibo\x10\t\x12\x1b\n\x17k_EStoreLinkType_Reddit\x10\n\x12\x1e\n\x1ak_EStoreLinkType_Instagram\x10\x0b\x12\x1b\n\x17k_EStoreLinkType_Tumblr\x10\x0c\x12\x1a\n\x16k_EStoreLinkType_Tieba\x10\r\x12\x1b\n\x17k_EStoreLinkType_Tiktok\x10\x0e\x12\x1d\n\x19k_EStoreLinkType_Telegram\x10\x0f\x12\x1d\n\x19k_EStoreLinkType_LinkedIn\x10\x10\x12\x1b\n\x17k_EStoreLinkType_WeChat\x10\x11\x12\x1b\n\x17k_EStoreLinkType_QQLink\x10\x12\x12\x1b\n\x17k_EStoreLinkType_Douyin\x10\x13\x12\x1c\n\x18k_EStoreLinkType_Bluesky\x10\x14\x12\x1d\n\x19k_EStoreLinkType_Mastodon\x10\x15\x12\x1c\n\x18k_EStoreLinkType_Threads\x10\x16\x12\x18\n\x14k_EStoreLinkType_MAX\x10\x17*\xf4\x01\n\x12\x45StoreCategoryType\x12!\n\x1dk_EStoreCategoryType_Category\x10\x00\x12)\n%k_EStoreCategoryType_SupportedPlayers\x10\x01\x12 \n\x1ck_EStoreCategoryType_Feature\x10\x02\x12*\n&k_EStoreCategoryType_ControllerSupport\x10\x03\x12$\n k_EStoreCategoryType_CloudGaming\x10\x04\x12\x1c\n\x18k_EStoreCategoryType_MAX\x10\x05\x32\xca\x04\n\x0bStoreBrowse\x12K\n\x08GetItems\x12\x1e.CStoreBrowse_GetItems_Request\x1a\x1f.CStoreBrowse_GetItems_Response\x12i\n\x12GetStoreCategories\x12(.CStoreBrowse_GetStoreCategories_Request\x1a).CStoreBrowse_GetStoreCategories_Response\x12Z\n\rGetPriceStops\x12#.CStoreBrowse_GetPriceStops_Request\x1a$.CStoreBrowse_GetPriceStops_Response\x12Z\n\rGetDLCForApps\x12#.CStoreBrowse_GetDLCForApps_Request\x1a$.CStoreBrowse_GetDLCForApps_Response\x12\x66\n\x11GetDLCForAppsSolr\x12\'.CStoreBrowse_GetDLCForAppsSolr_Request\x1a(.CStoreBrowse_GetDLCForAppsSolr_Response\x12\x63\n\x10GetHardwareItems\x12&.CStoreBrowse_GetHardwareItems_Request\x1a\'.CStoreBrowse_GetHardwareItems_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_storebrowse_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_ESTOREITEMTYPE']._serialized_start=9765
  _globals['_ESTOREITEMTYPE']._serialized_end=10021
  _globals['_ESTOREAPPTYPE']._serialized_start=10024
  _globals['_ESTOREAPPTYPE']._serialized_end=10451
  _globals['_EUSERREVIEWSCORE']._serialized_start=10454
  _globals['_EUSERREVIEWSCORE']._serialized_end=10843
  _globals['_ETRAILERCATEGORY']._serialized_start=10846
  _globals['_ETRAILERCATEGORY']._serialized_end=11093
  _globals['_ESTOREBROWSEFILTERFAILURE']._serialized_start=11096
  _globals['_ESTOREBROWSEFILTERFAILURE']._serialized_end=11391
  _globals['_ESTORELINKTYPE']._serialized_start=11394
  _globals['_ESTORELINKTYPE']._serialized_end=12109
  _globals['_ESTORECATEGORYTYPE']._serialized_start=12112
  _globals['_ESTORECATEGORYTYPE']._serialized_end=12356
  _globals['_STOREITEMID']._serialized_start=152
  _globals['_STOREITEMID']._serialized_end=274
  _globals['_STOREBROWSECONTEXT']._serialized_start=276
  _globals['_STOREBROWSECONTEXT']._serialized_end=376
  _globals['_STOREBROWSEITEMDATAREQUEST']._serialized_start=379
  _globals['_STOREBROWSEITEMDATAREQUEST']._serialized_end=942
  _globals['_CSTOREBROWSE_GETITEMS_REQUEST']._serialized_start=945
  _globals['_CSTOREBROWSE_GETITEMS_REQUEST']._serialized_end=1092
  _globals['_STOREITEM']._serialized_start=1095
  _globals['_STOREITEM']._serialized_end=6748
  _globals['_STOREITEM_RELATEDITEMS']._serialized_start=2666
  _globals['_STOREITEM_RELATEDITEMS']._serialized_end=2753
  _globals['_STOREITEM_INCLUDEDITEMS']._serialized_start=2755
  _globals['_STOREITEM_INCLUDEDITEMS']._serialized_end=2844
  _globals['_STOREITEM_CATEGORIES']._serialized_start=2846
  _globals['_STOREITEM_CATEGORIES']._serialized_end=2957
  _globals['_STOREITEM_REVIEWS']._serialized_start=2960
  _globals['_STOREITEM_REVIEWS']._serialized_end=3266
  _globals['_STOREITEM_REVIEWS_STOREREVIEWSUMMARY']._serialized_start=3104
  _globals['_STOREITEM_REVIEWS_STOREREVIEWSUMMARY']._serialized_end=3266
  _globals['_STOREITEM_BASICINFO']._serialized_start=3269
  _globals['_STOREITEM_BASICINFO']._serialized_end=3573
  _globals['_STOREITEM_BASICINFO_CREATORHOMELINK']._serialized_start=3509
  _globals['_STOREITEM_BASICINFO_CREATORHOMELINK']._serialized_end=3573
  _globals['_STOREITEM_TAG']._serialized_start=3575
  _globals['_STOREITEM_TAG']._serialized_end=3611
  _globals['_STOREITEM_ASSETS']._serialized_start=3614
  _globals['_STOREITEM_ASSETS']._serialized_end=3950
  _globals['_STOREITEM_RELEASEINFO']._serialized_start=3953
  _globals['_STOREITEM_RELEASEINFO']._serialized_end=4285
  _globals['_STOREITEM_PLATFORMS']._serialized_start=4288
  _globals['_STOREITEM_PLATFORMS']._serialized_end=4645
  _globals['_STOREITEM_PLATFORMS_VRSUPPORT']._serialized_start=4519
  _globals['_STOREITEM_PLATFORMS_VRSUPPORT']._serialized_end=4645
  _globals['_STOREITEM_PURCHASEOPTION']._serialized_start=4648
  _globals['_STOREITEM_PURCHASEOPTION']._serialized_end=5712
  _globals['_STOREITEM_PURCHASEOPTION_DISCOUNT']._serialized_start=5429
  _globals['_STOREITEM_PURCHASEOPTION_DISCOUNT']._serialized_end=5521
  _globals['_STOREITEM_PURCHASEOPTION_RECURRENCEINFO']._serialized_start=5524
  _globals['_STOREITEM_PURCHASEOPTION_RECURRENCEINFO']._serialized_end=5712
  _globals['_STOREITEM_SCREENSHOTS']._serialized_start=5715
  _globals['_STOREITEM_SCREENSHOTS']._serialized_end=5913
  _globals['_STOREITEM_SCREENSHOTS_SCREENSHOT']._serialized_start=5866
  _globals['_STOREITEM_SCREENSHOTS_SCREENSHOT']._serialized_end=5913
  _globals['_STOREITEM_TRAILERS']._serialized_start=5916
  _globals['_STOREITEM_TRAILERS']._serialized_end=6451
  _globals['_STOREITEM_TRAILERS_VIDEOSOURCE']._serialized_start=6030
  _globals['_STOREITEM_TRAILERS_VIDEOSOURCE']._serialized_end=6075
  _globals['_STOREITEM_TRAILERS_TRAILER']._serialized_start=6078
  _globals['_STOREITEM_TRAILERS_TRAILER']._serialized_end=6451
  _globals['_STOREITEM_SUPPORTEDLANGUAGE']._serialized_start=6454
  _globals['_STOREITEM_SUPPORTEDLANGUAGE']._serialized_end=6587
  _globals['_STOREITEM_FREEWEEKEND']._serialized_start=6589
  _globals['_STOREITEM_FREEWEEKEND']._serialized_end=6654
  _globals['_STOREITEM_LINK']._serialized_start=6656
  _globals['_STOREITEM_LINK']._serialized_end=6748
  _globals['_STOREGAMERATING']._serialized_start=6751
  _globals['_STOREGAMERATING']._serialized_end=6934
  _globals['_STOREBROWSEFILTERFAILURE']._serialized_start=6937
  _globals['_STOREBROWSEFILTERFAILURE']._serialized_end=7354
  _globals['_CSTOREBROWSE_GETITEMS_RESPONSE']._serialized_start=7356
  _globals['_CSTOREBROWSE_GETITEMS_RESPONSE']._serialized_end=7421
  _globals['_CSTOREBROWSE_GETSTORECATEGORIES_REQUEST']._serialized_start=7423
  _globals['_CSTOREBROWSE_GETSTORECATEGORIES_REQUEST']._serialized_end=7505
  _globals['_CSTOREBROWSE_GETSTORECATEGORIES_RESPONSE']._serialized_start=7508
  _globals['_CSTOREBROWSE_GETSTORECATEGORIES_RESPONSE']._serialized_end=7870
  _globals['_CSTOREBROWSE_GETSTORECATEGORIES_RESPONSE_CATEGORY']._serialized_start=7625
  _globals['_CSTOREBROWSE_GETSTORECATEGORIES_RESPONSE_CATEGORY']._serialized_end=7870
  _globals['_CSTOREBROWSE_GETPRICESTOPS_REQUEST']._serialized_start=7872
  _globals['_CSTOREBROWSE_GETPRICESTOPS_REQUEST']._serialized_end=7953
  _globals['_CSTOREBROWSE_GETPRICESTOPS_RESPONSE']._serialized_start=7956
  _globals['_CSTOREBROWSE_GETPRICESTOPS_RESPONSE']._serialized_end=8149
  _globals['_CSTOREBROWSE_GETPRICESTOPS_RESPONSE_PRICESTOP']._serialized_start=8087
  _globals['_CSTOREBROWSE_GETPRICESTOPS_RESPONSE_PRICESTOP']._serialized_end=8149
  _globals['_CSTOREBROWSE_GETDLCFORAPPS_REQUEST']._serialized_start=8152
  _globals['_CSTOREBROWSE_GETDLCFORAPPS_REQUEST']._serialized_end=8319
  _globals['_CSTOREBROWSE_GETDLCFORAPPS_RESPONSE']._serialized_start=8322
  _globals['_CSTOREBROWSE_GETDLCFORAPPS_RESPONSE']._serialized_end=8704
  _globals['_CSTOREBROWSE_GETDLCFORAPPS_RESPONSE_DLCDATA']._serialized_start=8497
  _globals['_CSTOREBROWSE_GETDLCFORAPPS_RESPONSE_DLCDATA']._serialized_end=8632
  _globals['_CSTOREBROWSE_GETDLCFORAPPS_RESPONSE_PLAYTIMEFORAPP']._serialized_start=8634
  _globals['_CSTOREBROWSE_GETDLCFORAPPS_RESPONSE_PLAYTIMEFORAPP']._serialized_end=8704
  _globals['_CSTOREBROWSE_GETDLCFORAPPSSOLR_REQUEST']._serialized_start=8707
  _globals['_CSTOREBROWSE_GETDLCFORAPPSSOLR_REQUEST']._serialized_end=8878
  _globals['_CSTOREBROWSE_GETDLCFORAPPSSOLR_RESPONSE']._serialized_start=8881
  _globals['_CSTOREBROWSE_GETDLCFORAPPSSOLR_RESPONSE']._serialized_end=9044
  _globals['_CSTOREBROWSE_GETDLCFORAPPSSOLR_RESPONSE_DLCLIST']._serialized_start=8993
  _globals['_CSTOREBROWSE_GETDLCFORAPPSSOLR_RESPONSE_DLCLIST']._serialized_end=9044
  _globals['_CSTOREBROWSE_GETHARDWAREITEMS_REQUEST']._serialized_start=9046
  _globals['_CSTOREBROWSE_GETHARDWAREITEMS_REQUEST']._serialized_end=9142
  _globals['_CHARDWAREPACKAGEDETAILS']._serialized_start=9145
  _globals['_CHARDWAREPACKAGEDETAILS']._serialized_end=9677
  _globals['_CSTOREBROWSE_GETHARDWAREITEMS_RESPONSE']._serialized_start=9679
  _globals['_CSTOREBROWSE_GETHARDWAREITEMS_RESPONSE']._serialized_end=9762
  _globals['_STOREBROWSE']._serialized_start=12359
  _globals['_STOREBROWSE']._serialized_end=12945
_builder.BuildServices(DESCRIPTOR, 'steammessages_storebrowse_pb2', _globals)
# @@protoc_insertion_point(module_scope)
