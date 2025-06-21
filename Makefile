.PHONY: new-week

# Creates a new weekly challenge structure.
# Usage:
#   make new-week               # Current year/week
#   make new-week 2024          # Current week in 2024
#   make new-week 2024 15       # Week 15 in 2024
new-week:
	@uv run scripts/new_week.py $(filter-out $@,$(MAKECMDGOALS))

# Prevent make from trying to build "2024" or "15" as targets
%:
	@: