# Summary

Software engineer and physicist specializing in Python backend development, API design, data processing, and optimization. Combines production backend experience — FastAPI, MySQL, Docker, RabbitMQ — with a strong foundation in mathematical modeling and discrete optimization.

# Experience

## Margaux Systems — Founder, Operations Research
*Mar 2026 – Present*

- Independent R&D in operations research: scheduling and production-planning models in Python and MiniZinc, documented as published case studies; direct outbound prospecting to manufacturers.

## SNAPP' — Python Backend Engineer (Contractor)
*Feb 2025 – Mar 2026*

- Took over a Spot FX price feed (FIX 4.2 over WebSocket, 56 currency pairs) where neither the inherited integration nor a vendor's rewrite attempt was salvageable, and rebuilt it against the protocol spec: codec, session lifecycle, reconnect-with-resubscription, price normalization. Single-threaded async, so message ordering stays deterministic; the feed recovers from a dropped connection on its own.
- Consolidated the access control of a banking API into one dependency: session validity, permissions (JWT scopes and DB authorizations), root perimeter, individual identity, 2FA certification and read-only state — driven by the `action:domain:privilege` code each route declares. Adding a route becomes a declaration, not a special case. <!-- v:backend,fintech -->
- Built 200+ REST endpoints (FastAPI, SQLAlchemy, Pydantic), the authentication middleware and the RabbitMQ/RPC services to external banking systems, across three MySQL databases with Alembic migrations and a pytest suite.
- Co-built the request-processing engine: typed workflows, audit trail, documents, and internal messaging.

## SIAL — Laboratory Technician
*Mar 2024 – Mar 2025*

- Laboratory testing, sample preparation, and experimental data management.

## Independent Developer
*Jul 2019 – Mar 2024*

- Web applications then software tools, self-directed; several are listed under Selected Projects.

## RENYT Tech — Frontend Developer
*Mar 2022 – Oct 2022*

- Web application features with React, Next.js, TypeScript, and Chakra UI.

# Education

## Universidad de los Andes — B.Sc. Physics (cum laude)
*Mérida, Venezuela — 2018*

Background in mathematical modeling and computational methods; moved into software engineering through 70+ self-directed courses in algorithms, architecture, compilers, discrete optimization, and machine learning.

**Research Assistant — Nonlinear Dynamics Group** (2017–2018): data analysis, literature reviews, and publications.

# Skills

**Programming languages:** Python, SQL, JavaScript

**Backend:** FastAPI, asynchronous Python, REST APIs, RabbitMQ, SQLAlchemy, Alembic

**Databases & infrastructure:** MySQL, Docker, Git, Linux

**Optimization:** MiniZinc, discrete optimization, mathematical modeling, algorithms

**Spoken languages:** French (fluent), English (bilingual), Spanish (native)

**Work authorization:** France — full right to work, no employer sponsorship required

# Selected Projects

[**Starisk**](https://starisk.matiasagelvis.com) — Course ratings recomputed from the most-upvoted reviews: dependency-free Python crawler and scorer, vote weighting by square root, calibrated against a human ranking (ρ = 0.70 vs 0.42). 426 courses, Astro site.

[**Significado Total**](https://semioteca.vercel.app) — Semiotics archive of 2,709 cards: extraction pipeline (ODT → DOCX → text, card-boundary and footnote detection), automatic tagging via zero-shot NLI and multilingual embeddings, static SvelteKit site with full-text search.
