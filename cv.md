# Summary

Software engineer and physicist specializing in Python backend development, API design, data processing, and optimization. Combines production backend experience — FastAPI, MySQL, Docker, RabbitMQ — with a strong foundation in mathematical modeling and discrete optimization.

# Experience

## Margaux Systems — Founder, Operations Research
*Mar 2026 – Present*

- Independent R&D in operations research: scheduling and production-planning models in Python and MiniZinc, documented as published case studies; direct outbound prospecting to manufacturers.

## SNAPP' — Python Backend Engineer (Contractor)
*Feb 2025 – Mar 2026*

- Unified the access control of a banking API into one dependency: session, JWT scopes and database authorizations, from the `action:domain:privilege` code each route declares — a route becomes a declaration, not a special case. Extended with impersonation, TOTP 2FA, account blocking and audit of failed attempts. <!-- v:backend,fintech -->
- Took over a Spot FX price feed (FIX 4.2 over WebSocket, 56 currency pairs) where neither the inherited integration nor a vendor's rewrite attempt was salvageable, and rebuilt it against the protocol spec: codec, session lifecycle, reconnect-with-resubscription, price normalization. Single-threaded async, so message ordering stays deterministic; the feed recovers from a dropped connection on its own.
- Designed asynchronous FastAPI REST services and authentication middleware, services communicating over RabbitMQ RPC, backed by three MySQL databases (SQLAlchemy, Alembic) and a pytest suite.
- Co-built the request-processing engine: typed workflows, audit trail, documents, and internal messaging.

## SIAL — Laboratory Technician
*Mar 2024 – Mar 2025*

- Laboratory testing, sample preparation, and experimental data management.

## Independent Software Development
*Oct 2022 – Mar 2024*

- Built and deployed web applications and software tools as self-directed projects; several are listed under Selected Projects.

## Frontend Developer — Remote
*Mar 2022 – Oct 2022*

- Built responsive web application features with React, Next.js, TypeScript, and Chakra UI.

# Education

## Universidad de los Andes — B.Sc. Physics (cum laude)
*Mérida, Venezuela — 2018*

Background in mathematical modeling and computational methods; moved into software engineering through 70+ self-directed courses in algorithms, architecture, compilers, discrete optimization, and machine learning.

# Skills

**Programming languages:** Python, SQL, JavaScript

**Backend:** FastAPI, asynchronous Python, REST APIs, RabbitMQ, SQLAlchemy, Alembic

**Databases & infrastructure:** MySQL, Docker, Git, Linux

**Optimization:** MiniZinc, discrete optimization, mathematical modeling, algorithms

**Spoken languages:** French (fluent), English (bilingual), Spanish (native)

**Work authorization:** France — full right to work, no employer sponsorship required

# Selected Projects

[**Starisk**](https://starisk.matiasagelvis.com) — Course ratings recomputed from the most-upvoted reviews: dependency-free Python crawler and scorer, vote weighting by square root, calibrated against a human ranking (ρ = 0.70 vs 0.42). 426 courses, Astro site.

[**Significado Total**](https://semioteca.vercel.app) — Linguistics research application built with Python and Svelte

[**OmegaInt**](https://github.com/matiasagelvis/omegaint) — Arbitrary-precision integer library in C++
