---

title: Team Phoenix
order: 1

---

Team Phoenix is made up of two squads, Kubernetes and Tooling.

<div class="grid cards" markdown>
{% for member in team_phoenix %}
-   ![{{ member.name }}]({{ member.picture }}){ width="150" align="left" }
    **{{ member.name }}**

    **Contact:** [:fontawesome-brands-slack:]({{ member.contact.slack }}) [:fontawesome-solid-envelope:](mailto:{{ member.contact.email }})

    **Skills:** {{ member.skills | join(', ') }}

    **Hobbies:** {{ member.hobbies | join(', ') }}

    **Fun Fact:** {{ member.fun_fact }}
{% endfor %}
</div>