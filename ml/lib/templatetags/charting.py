__author__ = 'brett'
from django import template


register = template.Library()

@register.simple_tag(takes_context=True)
def chart(context, chart_obj):
    chart_js_include = '' if '_chart_js_included' in context \
        else '<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.js"></script>'
    context['_chart_js_included'] = True

    html = \
    """
    {chart_js_include}
    <canvas id="{element_id}" width="{width}" height="{height}"></canvas>

    <script type="text/javascript">
        (function(){{
            Chart.defaults.global.responsive = true;
            Chart.defaults.global.maintainAspectRatio = true;
            var ctx = document.getElementById("{element_id}").getContext("2d");
            var chart = new Chart(ctx).{chart_type}({data}, {options});

        }}).call(this);
    </script>


    """.format(chart_js_include=chart_js_include, **chart_obj)

    return html
