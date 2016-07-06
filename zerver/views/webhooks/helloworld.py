# Webhooks for external integrations.
from __future__ import absolute_import
from django.utils.translation import ugettext as _
from zerver.lib.actions import check_send_message
from zerver.lib.response import json_success, json_error
from zerver.decorator import REQ, has_request_variables, api_key_only_webhook_view
from zerver.lib.validator import check_dict, check_string

@api_key_only_webhook_view('HelloWorld')
@has_request_variables
def api_helloworld_webhook(request, user_profile, client,
                           payload=REQ(argument_type='body'), stream=REQ(default='test'),
                           topic=REQ(default='Hello World')):

    # construct the body of the message
    body = ('Hello! I am happy to be here! :smile: ')

    # try to add the Wikipedia article of the day
    # return appropriate error if not successful
    try:
        body_template = '\nThe Wikipedia featured article for today is **[%s](%s)**'
        body += body_template % (payload['featured_title'], payload['featured_url'])
    except KeyError as e:
        return json_error(_("Missing key %s in JSON") % (e.message,))

    # send the message
    check_send_message(user_profile, client, 'stream', [stream], topic, body)

    return json_success()
