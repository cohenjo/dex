__author__ = 'eric'

import json
from bson import json_util

################################################################################
# Utilities
################################################################################
def pretty_json(obj):
    return json.dumps(obj, indent=4, default=json_util.default)


def small_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(',',':'))