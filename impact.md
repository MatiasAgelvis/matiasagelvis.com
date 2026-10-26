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

**Confirmed**
- Before: a plain bearer token. The permission model was designed by your lead and
  partially, poorly implemented by the bank.
- You implemented that model and extended it.
- Permissions as `(domain, action, privilege)` rows, granted through roles, carried
  as JWT scopes, enforced by one middleware that checks the tuple each route declares
- 20 roles, 135 permissions
- Added: session revocation, account blocking, multi-channel 2FA (SMS via Sinch, then
  Authy), per-role session limits, audit of failed authentications, IP allow-listing

**Attribution matters.** Do not write "j'ai conçu". You implemented a design that was
your lead's, on top of a bad partial implementation. In an interview that version is
*more* credible, not less — and it survives a call to the lead.

You said "we added" for the extensions. If the 2FA, blocking or audit work was shared
with colleagues, write "contribué à" for those and keep the first person for what was
yours alone.

**FR**
> Repris l'authentification d'une API bancaire qui n'était qu'un simple jeton bearer,
> en mettant en œuvre le modèle de permissions défini par le lead : permissions en
> (domaine, action, privilège), portées par des rôles et transmises en scopes JWT,
> vérifiées par un middleware unique à partir du tuple déclaré par chaque route —
> ajouter une route devient une déclaration, pas un cas particulier. Étendu avec la
> révocation de session, le blocage de compte, la 2FA multi-canal, les limites de
> session par rôle et l'audit des authentifications échouées.

**EN**
> Took over the authentication of a banking API that was a plain bearer token,
> implementing the permission model my lead had designed: permissions as
> `(domain, action, privilege)` rows, granted through roles, carried as JWT scopes,
> and enforced by a single middleware that checks the tuple each route declares — so
> adding a route is a declaration, not a special case. Extended it with session
> revocation, account blocking, multi-channel 2FA, per-role session limits, and audit
> of failed authentications.

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
- sole design credit for the authorization model — your lead designed it, you
  implemented and extended it
- the client bank's name — under a one-year non-solicitation, until roughly March 2027
