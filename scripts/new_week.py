import shutil
import sys
from datetime import UTC, datetime
from pathlib import Path


def create_week(year=None, week=None) -> bool:
    # Default to current year/week if not provided
    if year is None:
        year = datetime.now(UTC).year
    if week is None:
        week = datetime.now(UTC).isocalendar()[1]  # ISO week number

    # Ensure inputs are correct types
    year = int(year)
    week = int(week)

    # Format week with zero-padding
    week_str = f"{week:02d}"

    # Check if template exists
    template_path = Path("template")
    if not template_path.exists():
        print(f"❌ Error: {template_path} not found!")
        print("Are you in the repo root directory?")
        return False

    # Create year directory
    year_dir = Path("challenges") / str(year)
    year_dir.mkdir(parents=True, exist_ok=True)

    # Target directory
    target_dir = year_dir / week_str

    # Check if already exists
    if target_dir.exists():
        response = input(f"⚠️  {target_dir} already exists. Overwrite? (y/N): ")
        if response.lower() != "y":
            print("❌ Cancelled")
            return False
        shutil.rmtree(target_dir)

    # Copy template
    shutil.copytree(template_path, target_dir)

    print(f"✅ Created week {week_str} for year {year}")
    print(f"📁 Location: {target_dir}")

    # List created files
    print("📄 Files created:")
    for file_path in target_dir.iterdir():
        print(f"   - {file_path.name}")

    return True


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments - use current year/week
        create_week()
    elif len(sys.argv) == 2:
        # Year provided - use current week
        create_week(sys.argv[1])
    elif len(sys.argv) == 3:
        # Year and week provided
        create_week(sys.argv[1], sys.argv[2])
    else:
        print("Usage:")
        print("  python scripts/new_week.py              # Current year/week")
        print("  python scripts/new_week.py 2024         # Current week in 2024")
        print("  python scripts/new_week.py 2024 15      # Week 15 in 2024")
