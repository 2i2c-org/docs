# Documentation structure and strategy

## Purpose

This documentation provides information for key archetypes of [2i2c's managed interactive computing service](https://2i2c.org/).
It is also a way for us to share expertise and helpful information about managed open infrastructure workflows with the outside world.

## Overview

Our documentation follows a structure like this:

```
/[reader-archetype]/[high-level-topic]/[specific-topic.md]
```

For example:

```
docs/
  └── user/                   # Reader archetype
      ├── index.md            # Archetype landing page
      └── environment/        # High-level topic
          └── customize.md    # Specific topic
```

Each archetype is explained on our documentation landing page in a section like the following:

````md
## [archetype]

[short description of archetype]

```{toctree}
:caption: [archetype]
./[archetype]/[topic]/page.md
```
````

## Reader archetypes / personas

- A user of a hub (`user/`). They use features enabled for them by a hub administrator
- A hub administrator (`admin/`). They carry out technical actions with the hub on behalf of a community.
- A community leader (`community-lead/`). They make decisions about the community's service, care about cost and billing, etc.

❌ Not included: A general researcher data scientist who wants to learn about cloud workfows. We imagine either linking to other community documentation for this, or having a dedicated resource in the future.

## Top-level guides

There are a few special topics we include as top-level guides.

- **Getting starged** (`get-started/`). Meant for a newcomer who needs orientation. Could be any other user persona. They want to learn about the service and triage themselves into a persona.
- **Contributing guide** (`contribute/`). Could be any persona or a 2i2c team member. They need information for how to contribute to the documentation.
