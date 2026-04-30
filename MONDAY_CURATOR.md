# Monday Project Curator — Running Knowledge Base

**Last Updated:** April 30, 2026  
**Status:** Active — checked at session start + after project closes + on-demand

---

## 📖 Quick Reference

This .md tracks frameworks, learnings, anti-patterns, and best practices for spinning up Monday projects from team requests. Updated organically as projects ship.

---

## 🏗️ Project Templates by Type

### Video/Content Production
**Structure:**
- Validate (review source materials, flag gaps)
- Script (draft + timeline lock)
- Dry Run (record test, team feedback)
- Edit (incorporate notes, final cut)
- Accompanying Materials (guides, one-pagers, references)
- Final Review (team sign-off)

**Best Practices:**
- Always lock timeline + storage destination (LMS vs. standalone) before kicking off
- Link reference materials directly in board (SharePoint, Google Drive)
- Use Fathom for auto-recording dry runs if available
- Keep script phase separate from production — easier to iterate

**Anti-Patterns:**
- ❌ Starting dry run without explicit script approval
- ❌ Skipping the "destination" question (causes rework)
- ❌ Not linking source deck in validate phase

**Recent Example:**
- Project: "Essential Tech for Virtual Teaching" (2-min franchisee explainer)
- Workflow: Validate → Script → Dry Run → Edit → Materials → Final Review
- Status: Framework built, awaiting timeline clarification

---

### Training/Enablement Programs
*To be documented as projects arrive*

---

### Dashboard/Automation Projects
*To be documented as projects arrive*

---

## ✅ What Works Well

### Framework Design
- **Explicit phase separation** reduces scope creep (e.g., script phase ≠ production phase)
- **Blocking questions upfront** (timeline, destination, approver) save 2–3 rework cycles
- **Direct links to source materials** in board descriptions = zero "where's the deck?" friction

### Board Structure
- **Table view for workflow tracking** (Phase | Task | Owner | Status)
- **Custom fields** for timeline + storage type + approval chain
- **Linked items** for related projects (e.g., "Edit phase" depends on "Dry Run" approval)

### Communication
- **Monday board as single source of truth** for team updates (vs. email threads)
- **Response emails that direct to Monday** = consistent async workflow
- **Dry run feedback loop through Monday comments** = cleaner than email chains

---

## ❌ What Doesn't Work

### Board Setup
- ❌ Creating a board without locking timeline first (causes phantom deadlines)
- ❌ Multiple approval chains (too many cooks) — pick ONE decision-maker per phase
- ❌ Vague phase names ("Work" vs. "Dry Run") = confusion + status updates miss stakeholders

### Workflow
- ❌ Starting production before validation is **complete** (source material gaps kill timelines)
- ❌ Skipping the "blockers" section upfront — always surface unknowns before kickoff
- ❌ Not asking "past examples?" — reinventing the wheel on style/tone/length

### Communication
- ❌ Response emails that say "link in Monday" without the actual link
- ❌ Team feedback in email instead of board comments (fragmenting context)
- ❌ Pushing timeline changes via Slack instead of updating Monday (creates confusion)

---

## 🎯 Blocking Questions Checklist

**Every project kickoff must answer:**
- [ ] **Timeline?** Hard deadline for final deliverable
- [ ] **Destination?** Where does it live post-launch (LMS, Compass, Drive, etc.)?
- [ ] **Approver?** Who signs off (Dan, Trish, Heather, etc.)?
- [ ] **Past examples?** Similar projects we've shipped (style/tone/length reference)
- [ ] **Scope clarity?** What's *in* vs. *out* (e.g., "high-level only, no deep dives")

---

## 🛠️ Monday Best Practices

### Board Setup
- **Project name:** Straight-up, searchable, no cutesy language (e.g., "Essential Tech for Virtual Teaching" not "New Zee's Tele-Conferencing Thing")
- **Groups:** Organize by phase, not by person (easier to see workflow progression)
- **Views:**
  - **Table:** Default (Phase | Task | Owner | Status)
  - **Timeline:** For Gantt-style tracking if deadlines are tight
  - **Board:** For visual kanban if team prefers

### Custom Fields
- **Timeline:** Date field for deadline
- **Destination:** Dropdown (LMS / Compass / Google Drive / Other)
- **Blocker Flag:** Checkbox (if any blocking question unanswered)
- **Approval Chain:** Text field or linked item (who signs off + when)

### Automation
- **Auto-status on item creation:** Set to "Not Started"
- **Comment notifications:** Enable for approver role only (reduce noise)
- **Dependency linking:** Link "Edit phase" to "Dry Run approval" so status visibility is clear

### Communication Template
- **Response email format:**
  - 1-line summary of what we're building
  - Direct link to Monday board
  - List of any blocking questions needing clarity
  - "All future updates in Monday" call-to-action

---

## 📊 Project Tracking

### Open Projects
| Name | Type | Status | Timeline | Approver |
|------|------|--------|----------|----------|
| Essential Tech for Virtual Teaching | Video | Framework built, awaiting timeline | TBD | Heather/Dan/Trish |

### Completed Projects
*None yet — tracking starts May 2026*

### Learnings by Project
*To be populated as projects close*

---

## 🔄 Process: How to Use This .md

### At Session Start
- I check this .md for project context, past learnings, anti-patterns
- If new project request arrives, I reference "Blocking Questions Checklist"
- If similar project exists, I pull template and adapt

### During Project Execution
- I update "Open Projects" table as status changes
- I note any new anti-patterns or wins in real-time

### After Project Closes
- I document final learnings in relevant template section
- I update "Completed Projects" + note what worked/didn't
- I archive the Monday board link for reference

### On-Demand Updates
- Ben asks "check the curator .md" → I review + surface relevant learnings
- Ben discovers something new → tells me, I add it immediately

---

## 🚀 Next Steps

- [ ] Confirm GitHub storage path + I'll commit initial version
- [ ] Build "Project Templates" board in Monday (for reusable structures)
- [ ] After first project closes: document learnings + iterate template
- [ ] Add new project types as they arrive (training, dashboards, etc.)

---

## 📝 Notes & Observations

*Living section for in-progress learnings*

- **Observation 1 (Apr 30):** Video projects need explicit "script lock" gate before production — prevents scope creep
- **Observation 2 (Apr 30):** "Destination question" (LMS vs. standalone) affects downstream tooling — always ask upfront
