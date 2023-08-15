from django import template

register = template.Library()

@register.filter(name="add_attr")
def add_attr(field, css):
    attrs = {}
    class_, value = css.split(':')
    attrs[class_] = value
    return field.as_widget(attrs=attrs)