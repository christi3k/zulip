# Webhooks for external integrations.
from __future__ import absolute_import
from zerver.lib.actions import check_send_message
from zerver.lib.response import json_success
from zerver.decorator import REQ, has_request_variables, api_key_only_webhook_view
from zerver.lib.validator import check_dict, check_string

@api_key_only_webhook_view('Zapier')
@has_request_variables
def api_zapier_webhook(request, user_profile, client, stream=REQ(default='zapier')):
    check_send_message(user_profile, client, 'stream', [stream], 'test topic','hello world!')
    return json_success()
