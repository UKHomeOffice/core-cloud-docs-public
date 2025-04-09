---

title: Team Andromeda
order: 2
---

It's always DNS

<div class="grid cards" markdown>
{% for member in team_andromeda %}
-   ![{{ member.name }}]({{ member.picture }}){ width="150" align="left" }
    **{{ member.name }}**

    **Contact:** [:fontawesome-brands-slack:]({{ member.contact.slack }}) [:fontawesome-solid-envelope:](mailto:{{ member.contact.email }})

    **Skills:** {{ member.skills | join(', ') }}

    **Hobbies:** {{ member.hobbies | join(', ') }}

    **Fun Fact:** {{ member.fun_fact }}
{% endfor %}
</div>