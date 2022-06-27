(about/roles-for-service)=
# Team structure and roles

The Managed JupyterHub Service is a **collaborative cloud service** run in partnership with the communities that we serve.
This page describes the major teams and roles that are involved in running this service.

## Teams and key stakeholders

The Managed JupyterHub Service is composed of a {term}`Service Team` along with three sub-teams.

```{figure} https://drive.google.com/uc?export=download&id=16r5xE7SguunLfMh5LhSynSUfjb7IXs_n
An overview of the major teams that collaborate around the cloud service in order to serve a community of users. There are three main teams, and this diagram shows the major traits of each team, as well as a few ways in which they interact with one another.
```

### Service team structure

```{glossary}
Managed JupyterHub Service Team
Service Team
  The group of people that collaborate together to run a collaborative cloud service. It is comprised of three major sub-teams:

  1. The {term}`Cloud Engineering Team`
  2. The {term}`Community Support Team`
  3. The {term}`Partnerships Team`
  4. The {term}`Community Leadership Team`

Cloud Engineering Team
Engineering Team
  A team of engineers with expertise in cloud infrastructure and open source tools that we use as part of our services. This group of people oversees the cloud infrastructure that a community uses. They perform new development and upgrades, make changes per the request of {term}`Community Representatives`, and coordinate with the {term}`Community Support Team` during incidents and outages.
  This is roughly equivalent to a {term}`tc:Site Reliability Engineering Team`.

  See [our Infrastructure documentation](https://infrastructure.2i2c.org/en/latest/) for more information.

Community Support Team
Support Team
  A team of expert practitioners with familiarity in user workflows as well as the technical use-cases that 2i2c's cloud services enable. This group acts as a bridge between the communities we work with and our {term}`Cloud Engineering Team`, facilitating information transfer, signal-boosting community needs and requests, and guiding communities in utilizing the infrastructure more effectively.

  See the {ref}`Support Team Documentation <tc:support:guide>` for more information.

Partnerships Team
  A team of experts in building cross-organizational collaborations, contracts, and grants. This team is tasked with forging new partnerships with communities and their organizations, identifying the resources needed to make these partnerships sustainable, and leading the contracting and invoicing process (when needed) to recover our costs. They are the primary interface with our {term}`tc:Fiscal Sponsor`, {term}`Code for Science and Society`.

Community Leadership Team
Community Team
  A team of leaders *within the community that we work with* who act as {term}`Community Representatives` on behalf of their community. This team coordinates more closely with our {term}`Community Support Team`, facilitates the transfer of knowledge between 2i2c teams and communities of users, and helps manage the structure and dynamics of these communities. They also define the strategic mission and goals of each user community, and help us define the definition of "success" for the hub service.
```

### Key stakeholders

In addition, there are two groups of stakeholders that are not directly involved in running the service, but that are important to consider to ensure that each service has the impact that we wish to achieve.
Our {term}`Service Team` spends extra effort interacting with and getting feedback from these stakeholder communities.

```{glossary}
User Community
User Communities
  Anybody that uses the infrastructure on a given hub. These tend to be students, researchers, collaborators, or workshop attendees. They come from a variety of backgrounds and skillsets, but they are all considered to be a part of the community that a hub serves (even if only for a short time). This community is important to our services because the impact of the service is ultimately driven by the work that this community does.

Open Source Communities
Open Source Community
  The distributed communities that lead, develop, and support the open source infrastructure that is used in our collaborative cloud service. Members of the {term}`Service Team` are often also members of these open source communities, and act as liasons to help upstream improvements and lead discussions that are surfaced as part of running our cloud service together. This community is important to our services because part of 2i2c's mission involves using its resources and experience to support and improve the open source communities that underlie our service.
```

## Community roles

The following roles are overseen by one or more members of the user community.
They help direct the infrastructure and service in order to help the community accomplish its goal, and act as leaders to empower the community in using the infrastructure.

```{glossary}
Community Representative
Community Representatives
  Acts as the primary point of contact for a community, and ensures that the interests of the {term}`Hub Community` are represented in the infrastructure, and that the hub serves their needs.
    They have the authority to speak on behalf of the community, and make decisions about the infrastructure that the community uses.

    There must be **one or two community representatives for a given community**.
    This role is usually filled by someone that is a member of the hub's community of practice.

    Their main responsibilities include:

    - The main point of contact between the hub engineer and the {term}`Hub Community`.
    - Collect feedback and questions from users on a hub.
    - Surface questions and requests to Hub Engineers via support tickets.
    - Oversee the {term}`Hub Administrators`.

Hub Administrator
Hub Administrators
  Trusted community members that perform common administrative operations on a hub that do not require intervention from a {term}`tc:Hub Engineer`.
  {term}`Community Representatives` are the first Hub Administrators, and they may add new Hub Administrators via the JupyterHub interface.
  They are able to add users, start/stop servers, and generally have more control over operations on the hub.

  Their responsibilities include:

  - Provide support to users of a hub for common problems that don't require a Hub Engineer to resolve.
  - Add new users to a hub, including administrative users.
  - Surface major issues or requests to the Community Representative(s).
```

Roles that are specific to 2i2c are defined [in the 2i2c Team Compass](https://team-compass.2i2c.org).
