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

**Missing**
- Beat 4: who felt the pain — trading desk, ops, or whoever babysat the reconnects?
- Any evidence for the "stale or slow prices" hypothesis. Do **not** claim it without it.

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

**Confirmed**
- Permissions are rows in a `(domain, action, privilege)` namespace
- Granted through roles, carried as JWT scopes
- Routes declare the tuple they need; one FastAPI dependency does the subset check
- 20 roles, 135 permissions
- Also: multi-channel 2FA (SMS via Sinch, then Authy), login lockout,
  per-role session limits, IP allow-listing, session-before-authorization ordering

**Missing**
- Beat 3, if you have it: what specifically got easier — onboarding a role,
  auditing access, adding a route? One sentence makes this bullet land.

**FR**
> Reconstruit le modèle d'autorisation d'une API bancaire autour d'un espace de
> permissions (domaine, action, privilège) : les permissions sont des données,
> portées par des rôles et transmises en scopes JWT, et un unique middleware FastAPI
> vérifie que le tuple déclaré par la route est inclus dans les scopes. Ajouter une
> route devient une déclaration et non un cas particulier — ce qui permet de tenir
> 20 rôles et 135 permissions sans que le code se disperse. Complété par la 2FA
> multi-canal (SMS puis application d'authentification), le verrouillage de
> connexion, les limites de session par rôle et une liste blanche d'IP.

**EN**
> Rebuilt the authorization model of a banking API around a `(domain, action,
> privilege)` permission namespace: permissions are data, granted through roles,
> carried as JWT scopes, and enforced by a single FastAPI dependency that checks
> the tuple each route declares. Adding a route became a declaration rather than a
> special case — which is what kept 135 permissions across 20 roles from turning
> into 135 bespoke checks. Extended with multi-channel 2FA (SMS, then authenticator
> app), login lockout, per-role session limits, and IP allow-listing.

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
- the client bank's name — under a one-year non-solicitation, until roughly March 2027
