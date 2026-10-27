# Impact bank

Working notes for CV bullets and letter evidence. Not deployed — only `site/` is.

The problem this solves: *"I always make an impact but I don't know how to articulate it."*
An impact claim needs a mechanism, not an adjective. Each bullet follows five beats.
Most CVs stop at beat 2, which is why they read as a task list.

1. **Constraint** — what was broken, underspecified, or commercially impossible
2. **Decision** — the non-obvious call you made
3. **Change** — what is measurably different now
4. **Who felt it** — team, client, business
5. **Counterfactual** — what would have happened if nobody did it

Beat 5 is the cheap one: *"what would have happened if this hadn't been done?"* is the impact.

---

## 1. Spot FX feed — FIX 4.2, 56 pairs

**Confirmed**
- Client: a bank, reached through SNAPP' (two degrees of separation)
- Inherited integration and a vendor's rewrite attempt: neither usable
- Rebuilt from the protocol spec: codec, session lifecycle, reconnect with
  resubscription, price normalization including inverted quotes
- Single-threaded async architecture, chosen so message ordering stays deterministic
- 56 FX pairs; live pair state served over HTTP
- Delivered inside an unfunded rewrite window, billed at ~8 h/week, told to ship
  ASAP with no test budget
- Trade logic stayed with the bank and was out of scope — the team was not allowed
  to touch it. It is probably still messy; that is not your claim to make.
- Pain was felt by the integration team: you and your colleagues. The beneficiaries
  are the bank's end clients.

**Resolved — no outcome claim.** You never observed the client-side effect, so the
feed's own behaviour *is* the claim. Anything beyond it would be invention. That's
fine: a bullet can stop at beat 3 and still be strong.

**FR**
> Repris un flux de change au comptant (FIX 4.2 sur WebSocket, 56 paires de devises)
> dont ni l'intégration existante ni la réécriture d'un prestataire n'étaient
> exploitables, et reconstruit à partir de la spécification du protocole : codec,
> cycle de vie des sessions, reconnexion avec réabonnement, normalisation des prix.
> Architecture asynchrone mono-thread, choisie pour que l'ordre des messages reste
> déterministe. Le flux se rétablit seul après une coupure, sans intervention manuelle.

**EN**
> Took over a Spot FX price feed (FIX 4.2 over WebSocket, 56 currency pairs) where
> neither the inherited integration nor a vendor's rewrite attempt was salvageable,
> and rebuilt it against the protocol spec: codec, session lifecycle,
> reconnect-with-resubscription, price normalization. Single-threaded async
> architecture, chosen so message ordering stays deterministic. The feed recovers
> from connection drops on its own, without manual intervention.

---

## 2. Authorization layer

**Git evidence** — `amfie-api`, 111 commits tagged `(auth)`, **95 of them yours**.

| Date | What | Whose |
|---|---|---|
| Oct 2024 | `role`, `authorization`, `role_authorization` CSVs + migration — the data model | Cyryl Balma Tivola, Julien Hertout |
| Jul 2025 | `AccessControl`: one dependency checking session **and** authorization, hybrid JWT-scope + DB lookup | you |
| Jul 2025 | `AuthorizationOperations`, `AuthorizationPayload`, custom session authorizations | you |
| Oct 2025 | privilege sweep across every domain (`any` / `restricted` / `internal`) | you |
| Oct 2025 | impersonation — "Login As" endpoint | you |
| Jan–Mar 2026 | 2FA: TOTP, account blocking, audit of failed attempts, `TwoFactorAuthProcessor` | you |
| Jun 2026 | localized auth errors, no identifier leak on a bad OTP | you |

**The honest split:** the *schema* predates you by eight months. The *enforcement layer* is
yours. That is a stronger claim than "my lead designed it", and it's verifiable.

**Numbers, checked in the repo** — supporting detail only, never the headline
- `authorization.csv` → 135 rows = **135 permissions**, exact
- `role.csv` → **10 roles** (an earlier "20 roles" figure was wrong; it's not on the CV)
- `role_authorization.csv` → 344 role→permission mappings
- code format is `action:domain:privilege`, e.g. `create:access-token:restricted`

**Two claims to drop.** "Just a simple bearer token" doesn't survive the repo: an
`AuthorizationChecker` dependency and the authorization tables already existed before your
refactor. What was missing was a *unified* enforcement path, not a model. And "my lead
designed it" is too generous — he and Cyryl built the tables in 2024; you built everything
that enforces them.

**The claim that matters — not the counts**

The number of roles or permissions is not the story. The story is the **consolidation**:
`get_current_user` (session) and `AuthorizationChecker` (permissions) were two separate
dependencies. You merged them into `AccessControl` (Jul 2025), then absorbed the root
perimeter, individual identity, 2FA certification and read-only state into the same place
(Mar–May 2026). Five concerns, one dependency, one declaration per route.

Counts are available if asked — 135 permissions, 10 roles in `role.csv` — but they are
supporting detail, not the headline.

**FR**
> Fusionné le contrôle d'accès d'une API bancaire en une dépendance unique : validation de
> session, permissions (scopes JWT et autorisations en base), périmètre de comptes,
> identité, 2FA et sessions en lecture seule — à partir du code « action:domaine:privilège »
> déclaré par chaque route. Ajouter une route devient une déclaration, pas un cas particulier.

**EN**
> Consolidated the access control of a banking API into one dependency: session validity,
> permissions (JWT scopes and DB authorizations), root perimeter, individual identity, 2FA
> certification and read-only state — driven by the `action:domain:privilege` code each
> route declares. Adding a route becomes a declaration, not a special case.

If the 2FA, blocking or audit work was shared with colleagues, write "contribué à" for those
and keep the first person for what was yours alone.


---

## 3. Margaux Systems

**Confirmed**
- Scheduling and production-planning models in Python and MiniZinc
- Published case studies, direct outbound prospecting to manufacturers
- No client engagement. Prospecting and client acquisition were the failure, not the modelling.

**Missing**
- Nothing. This one is finished. Keep it to one line; do not imply traction.

**FR**
> R&D indépendante en recherche opérationnelle : modélisation d'ordonnancement et
> de planification de production en Python et MiniZinc, études de cas publiées,
> prospection directe auprès d'industriels. Aucun client signé — la contrainte
> bloquante était l'accès au décideur, pas le solveur.

**EN**
> Independent R&D in operations research: scheduling and production-planning models
> in Python and MiniZinc, published case studies, direct outbound prospecting to
> manufacturers. No client engagement — the binding constraint was access to the
> person who owns the planning decision, not the solver.

---

## Auth, in one page (interview refresher)

**The question it answers:** which user can call which route, on which data.

**The model** — three tables, created Oct 2024, before you joined
- `role` — 10 roles (`member`, `admin_ext`, `it_staff`, `compliance_manager`, …)
- `authorization` — 135 rows, one per permission
- `role_authorization` — 344 rows, which role grants which permission
- a permission's identity is a string, `domain:action:privilege`, e.g. `beneficiary:create:restricted`

**At login** (`SessionService.create_session`)
1. compute the user's root perimeter, and whether the session must be read-only
   (HOLD on a BLOCKED root, or impersonation)
2. derive the effective authorizations: explicit (password reset), or read-only → only
   active+read, otherwise everything the user holds
3. bake them into the JWT as `scopes`
4. create a session row keyed by the token's JTI

**On every request** (`AccessControl.__call__`, one dependency)
1. is the session active?
2. read-only session hitting a non-read route? → 403 + a log line
3. required codes ⊆ token scopes? → otherwise 401/403, localized
4. `root_number` in the session's roots?
5. `individual_id` matches the session's user?
6. 2FA certified, if the route requires it
7. touch `last_activity`

**Why "hybrid":** the DB is the source of truth at login; the JWT is the fast path per
request — no join per permission check. Revocation invalidates the session (JTI lookup),
it doesn't rewrite tokens.

**Declaring a route**
```python
dependencies=[Depends(AccessControl([AuthorizationForRoute(
    auth_domain=AuthorizationDomain.beneficiary,
    auth_action=AuthorizationAction.create,
    auth_privilege=AuthorizationPrivilege.restricted,
)]))]
```

**The `restricted` / `any` trap — the one to remember**
- The words read backwards. `restricted` sounds like admin-only; it is the *member* level.
  `any` sounds like everyone; it is the *admin / broad* level.
- The functional difference: privilege is part of the permission **string**, so
  `country:read:any` and `country:read:restricted` are two different permissions. A role
  granted one does not satisfy a route declaring the other — silent 403.
- It also drives the 2FA default: `any` / `internal` → no 2FA; `restricted` → 2FA required
  unless the route overrides.
- That's why the inversion was expensive: it fails as an authorization mismatch, not as a
  crash, so nothing tells you the name is wrong.

**2FA** (yours, Jan–Mar 2026)
- second factor after the password: OTP by SMS (Sinch), then authenticator app (Authy/TOTP)
- `UserDoubleAuthAttempt` records attempts for audit
- blocked accounts are rejected immediately in TOTP flows
- `TwoFactorAuthProcessor` centralises OTP validation
- sessions carry `is_double_auth_certified`, enforced per route by `AccessControl`

**Impersonation** ("Login As", Oct 2025) — issues a session for the impersonated user,
forced read-only, with an X-Real-IP check on the caller.

---

## What to do with this

- These three bullets are the raw material for `cv.md` / `cv-fr.md`.
- Tag them with `<!-- v:backend -->`, `<!-- v:or -->`, `<!-- v:fintech -->` as the
  variants diverge.
- The `evidence` field of the letter builder draws on section 1 and 2.

## Never write

- "absolute garbage code", "not a line survived" — say *unusable, rebuilt from the spec*
- "I worked for free" / "16-hour days" — interview story about judgment, not a CV line
- hour totals — the tracked hours are sold volume, not hours worked
- any claim of a test suite on the FIX work — you were directed to ship without one
- sole design credit for the authorization model — the tables predate you (Oct 2024);
  the enforcement layer is yours
- "just a simple bearer token" — an `AuthorizationChecker` and the tables already existed
- the client bank's name — under a one-year non-solicitation, until roughly March 2027
