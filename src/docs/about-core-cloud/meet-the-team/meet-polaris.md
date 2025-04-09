---

title: Team Polaris
order: 1
---

:fontawesome-solid-music: Do you want to build a developer portal? :fontawesome-solid-music: :fontawesome-solid-snowman:

<div class="grid cards" markdown>
{% for member in team_polaris %}
-   ![{{ member.name }}]({{ member.picture }}){ width="150" align="left" }
    **{{ member.name }}**

    **Contact:** [:fontawesome-brands-slack:]({{ member.contact.slack }}) [:fontawesome-solid-envelope:](mailto:{{ member.contact.email }})

    **Skills:** {{ member.skills | join(', ') }}

    **Hobbies:** {{ member.hobbies | join(', ') }}

    **Fun Fact:** {{ member.fun_fact }}
{% endfor %}
</div>