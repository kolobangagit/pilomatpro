"""
Yandex.Metrica template tags and filters.
"""

import json
import re

from django.conf import settings
from django.template import Library, Node, TemplateSyntaxError
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from store.utils import disable_html, get_required_setting, is_internal_ip

COUNTER_ID_RE = re.compile(r'^\d{8}$')
COUNTER_CODE = """
    <script type="text/javascript">
        (function (d, w, c) {
            (w[c] = w[c] || []).push(function() {
                try {
                    w.yaCounter%(counter_id)s = new Ya.Metrika(%(options)s);
                } catch(e) { }
            });

            var n = d.getElementsByTagName("script")[0],
                s = d.createElement("script"),
                f = function () { n.parentNode.insertBefore(s, n); };
            s.type = "text/javascript";
            s.async = true;
            s.src = "https://mc.yandex.ru/metrika/watch.js";

            if (w.opera == "[object Opera]") {
                d.addEventListener("DOMContentLoaded", f, false);
            } else { f(); }
        })(document, window, "yandex_metrika_callbacks");
    </script>
    
"""  # noqa


register = Library()


@register.inclusion_tag('location/tags/_yandex.html', takes_context=True)
def yandex_metrica(context):
    return {
        'options': {
            'id':int(context['counter_id']),
            'clickmap':context['clickmap'],
            'trackLinks':context['counter_id'],
            'accurateTrackBounce':context['counter_id']
        },
        'counter_id': context['counter_id'],
        'noscript': '<div><img src="https://mc.yandex.ru/watch/{}" style="position:absolute; left:-9999px;" alt="" /></div>' .format(context['counter_id'])
    }



# @register.simple_tag(takes_context=True)
# def yandex_metrica(context):
#     counter_id = context['counter_id']
#     options = {
#             'id': int(counter_id),
#             'clickmap': True,
#             'trackLinks': True,
#             'accurateTrackBounce': True
#         }
#     html = COUNTER_CODE % {
#             'counter_id': counter_id,
#             'options': json.dumps(options),
#         }
#     html = mark_safe(html)
#     return html + mark_safe('<noscript>') + format_html('<div><img src="https://mc.yandex.ru/watch/%(counter_id)s" style="position:absolute; left:-9999px;" alt="" /></div>' % {"counter_id": counter_id}) + mark_safe('</noscript>')

