---

title: Meet the delivery team
order: 0
---

Under 30 minutes or it's free.

<div class="grid cards" markdown>
{% for member in team_delivery %}
-   ![{{ member.name }}]({{ member.picture }}){ width="150" align="left" }
    **{{ member.name }}**

    **Contact:** [:fontawesome-brands-slack:]({{ member.contact.slack }}) [:fontawesome-solid-envelope:](mailto:{{ member.contact.email }})

    **Skills:** {{ member.skills | join(', ') }}

    **Hobbies:** {{ member.hobbies | join(', ') }}

    **Fun Fact:** {{ member.fun_fact }}
{% endfor %}
</div>