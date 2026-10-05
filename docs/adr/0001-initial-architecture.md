# ADR-0001: Initial Architecture

- Date: 05/10/2026
- Status: Accepted

## Context

We need a minimal public baseline for Kubernetes-focused AI tooling with clear delivery and deployment patterns.

## Decision

Use a small FastAPI service packaged with Docker and deployable both by raw Kubernetes manifests and Helm chart.

## Consequences

- Fast onboarding for contributors
- Standard CI pipeline for Python tests and image build
- Extensible structure for domain-specific troubleshooting modules
