# Example Project Setups

These examples show how to adapt the workflow after the initial collaboration mechanism is confirmed. Treat profiles as starting points, not fixed team structures.

## Static Data Query Website

Possible ownership split:

```text
manager: confirm scope, acceptance criteria, dispatch, collect, report
design: UX structure and interaction brief
preview: isolated static previews and screenshots
code: production implementation and local tests
data: data source, schema, generated files, audits, field facts
assets: image, carousel, compression, asset references
research: external references and implementation notes
release: git status, diff checks, commit/push only after approval
docs: project memory and handoff consistency
```

Example flow:

```text
User asks to improve mobile results
-> manager proposes mechanism and asks for confirmation
-> design writes the mobile information hierarchy brief
-> preview creates isolated options
-> user selects one option
-> code implements the selected direction
-> validator checks screenshots and tests
-> docs records the decision
-> release acts only after explicit user approval
```

Important boundaries:

- Data field judgments belong to the data owner.
- Preview work stays in an isolated preview folder.
- Production code changes follow an accepted brief.
- Release actions require explicit user approval.

## Content Operations Team

Possible ownership split:

```text
manager: positioning, rhythm, priorities, acceptance criteria
topic: topic planning and idea pool
content: outline, script, copy, title, description
material: cover, screenshots, asset checklist, prompts
review: data pull, performance review, lessons
```

Example flow:

```text
topic proposes ideas
-> content drafts the selected idea
-> material prepares cover and assets
-> human records or publishes
-> review analyzes performance
-> manager adjusts the next direction
```

## GitHub PR Fix

Possible ownership split:

```text
manager: define the PR objective and acceptance criteria
explorer: inspect failing checks, review comments, and relevant files
executor: implement the scoped fix
validator: rerun tests or checks and review the diff
release: commit, push, or update PR only after approval
```

Example flow:

```text
User asks to fix a failing PR
-> manager confirms whether release actions are allowed
-> explorer gathers failure evidence
-> executor patches only the responsible files
-> validator reruns the smallest relevant checks
-> release pushes only after explicit approval
```

## Data Analysis Project

Possible ownership split:

```text
manager: business question and output format
data: source files, schema, cleaning, calculation facts
analysis: interpretation and findings
visual: charts or report layout
validator: formula checks, sample checks, source traceability
docs: final report and assumptions
```

The exact team should be selected from the real task boundaries, not from the profile name.
