#!/usr/bin/env python

import re
from keyword import kwlist
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper
from steam.enums import common as common_enums
from os import listdir
from os.path import isfile, join

kwlist = set(kwlist + ['None'])

_proto_modules = [file.replace(".py", "") for file in listdir(join("steam", "protobufs")) if isfile(join("steam", "protobufs", file)) and file != "__init__.py"]
_proto_module = __import__("steam.protobufs", globals(), locals(), _proto_modules, 0)

classes = {}

for name in _proto_modules:

    proto = getattr(_proto_module, name)
    gvars = globals()

    for class_name, value in proto.__dict__.items():
        if not isinstance(value, EnumTypeWrapper) or hasattr(common_enums, class_name):
            continue

        attrs_starting_with_number = False
        attrs = {}

        for ikey, ivalue in value.items():
            ikey = re.sub(r'^(k_)?(%s_)?' % class_name, '', ikey)
            attrs[ikey] = ivalue

            if ikey[0:1].isdigit() or ikey in kwlist:
                attrs_starting_with_number = True

        classes[class_name] = attrs, attrs_starting_with_number

# print out enums as python Enum
print("from steam.enums.base import SteamIntEnum")

for class_name, (attrs, attrs_starting_with_number) in sorted(classes.items(), key=lambda x: x[0].lower()):
        if attrs_starting_with_number:
            print(f"\n{class_name} = SteamIntEnum({class_name!r}, {{")
            for ikey, ivalue in attrs.items():
                print(f"    {ikey!r}: {ivalue!r},")
            print("    })")
        else:
            print(f"\nclass {class_name}(SteamIntEnum):")
            for ikey, ivalue in attrs.items():
                print(f"    {ikey} = {ivalue}")

print("\n__all__ = [")

for class_name in sorted(classes, key=lambda x: x.lower()):
    print("    %r," % class_name)

print("    ]")
