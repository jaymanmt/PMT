#custom templates to do calculation on basket.templates
from django import template 

register = template.Library()

@register.simple_tag
def calculate_total(quantity, cost):
    if quantity >= 5:
        discounted_cost = ((quantity*cost)/100)*0.9
        return int(discounted_cost)
    else:
        new_cost = (quantity*cost)/100
        return int(new_cost)