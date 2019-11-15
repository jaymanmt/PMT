#custom templates to do calculation on basket.templates
from django import template 

register = template.Library()

@register.simple_tag
def calculate_total_tag(quantity, cost):
    new_cost = (quantity*cost)/100
    return int(new_cost)