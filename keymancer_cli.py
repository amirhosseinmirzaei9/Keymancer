import click
import json
import os
from keymancer_core import GeneratorFactory
from mnemonic import Mnemonic
from rich.console import Console
from rich.table import Table
import pyperclip

console = Console()

# ---------------- Helpers ----------------
def print_and_copy(items, title, copy, item_name="Item", as_json=False, plain=False, json_file=None):
    """Unified printer for table/json/plain outputs"""
    if not items:
        console.print("[red]❌ Nothing to display[/red]")
        return

    if json_file:
        # Save JSON to file
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2)
        console.print(f"✅ Output saved to JSON file: [green]{json_file}[/green]")
        return
    
    # JSON output
    if as_json:
        click.echo(json.dumps(items, indent=2))
        return

    # Plain output
    if plain:
        for p in items:
            click.echo(p)
        return

    # Rich table output
    table = Table(title=title)
    table.add_column("Index")
    table.add_column(item_name)
    for i, p in enumerate(items, 1):
        table.add_row(str(i), p)
    console.print(table)

    # Copy to clipboard
    if copy and items:
        pyperclip.copy(items[0])
        console.print(f"✅ First {item_name} copied to clipboard")


def load_defaults():
    """Load user defaults from ~/.keymancer.json if exists"""
    config_path = os.path.expanduser("~/.keymancer.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

defaults = load_defaults()


# ---------------- CLI ----------------
@click.group()
def cli():
    """Keymancer CLI - Password & Passphrase Generator 🧙‍♂️"""
    pass


# ---------------- Random Password ----------------
@cli.command()
@click.option("--length", default=lambda: defaults.get("random_length", 16), type=int, help="Password length")
@click.option("--upper/--no-upper", default=lambda: defaults.get("random_upper", True), help="Include uppercase letters")
@click.option("--lower/--no-lower", default=lambda: defaults.get("random_lower", True), help="Include lowercase letters")
@click.option("--digits/--no-digits", default=lambda: defaults.get("random_digits", True), help="Include digits")
@click.option("--symbols/--no-symbols", default=lambda: defaults.get("random_symbols", True), help="Include symbols")
@click.option("--batch", default=lambda: defaults.get("random_batch", 1), type=int, help="Number of passwords to generate")
@click.option("--copy/--no-copy", default=False, help="Copy first password to clipboard")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
@click.option("--json-file", type=click.Path(), help="Write output to JSON file instead of terminal")
@click.option("--plain", is_flag=True, help="Output as plain text")
def random(length, upper, lower, digits, symbols, batch, copy, as_json, plain, json_file):
    """Generate random passwords"""
    if length <= 0:
        console.print("[red]❌ Length must be greater than 0[/red]")
        return
    if batch <= 0:
        console.print("[red]❌ Batch size must be greater than 0[/red]")
        return

    gen = GeneratorFactory.create("random",
                                  length=length,
                                  use_upper=upper,
                                  use_lower=lower,
                                  use_digits=digits,
                                  use_symbols=symbols)
    passwords = [gen.generate() for _ in range(batch)]
    print_and_copy(passwords, "Generated Random Passwords", copy, "Password", as_json, plain, json_file)

# ---------------- PIN ----------------
@cli.command()
@click.option("--length", default=lambda: defaults.get("pin_length", 6),type=int, help="PIN length")
@click.option("--batch", default=lambda: defaults.get("pin_batch", 1),type=int, help="Number of PINs to generate")
@click.option("--copy/--no-copy", default=False, help="Copy first PIN to clipboard")
@click.option("--json-file", type=click.Path(), help="Write output to JSON file instead of terminal")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
@click.option("--plain", is_flag=True, help="Output as plain text")
def pin(length, batch, copy, as_json, plain, json_file):
    """Generate numeric PIN codes"""
    if length <= 0:
        console.print("[red]❌ Length must be greater than 0[/red]")
        return
    if batch <= 0:
        console.print("[red]❌ Batch size must be greater than 0[/red]")
        return

    gen = GeneratorFactory.create("pin", length=length)
    pins = [gen.generate() for _ in range(batch)]
    print_and_copy(pins, "Generated PINs", copy, "PIN", as_json, plain, json_file)


# ---------------- Passphrase ----------------
@cli.command()
@click.option("--words", default=lambda: defaults.get("passphrase_words", 4),type=int, help="Number of words")
@click.option("--separator", default=lambda: defaults.get("passphrase_separator", "-"))
@click.option("--language", default=lambda: defaults.get("passphrase_language", "english"),
              type=click.Choice(Mnemonic.list_languages()))
@click.option("--strength", default=lambda: defaults.get("passphrase_strength", 256),
              type=click.Choice([128,160,192,224,256]))
@click.option("--json-file", type=click.Path(), help="Write output to JSON file instead of terminal")
@click.option("--batch", default=lambda: defaults.get("passphrase_batch", 1),type=int, help="Number of passphrases to generate")
@click.option("--copy/--no-copy", default=False, help="Copy first passphrase to clipboard")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
@click.option("--plain", is_flag=True, help="Output as plain text")
def passphrase(words, separator, language, strength, batch, copy, as_json, plain, json_file):
    """Generate secure passphrases"""
    if words <= 0:
        console.print("[red]❌ Words must be greater than 0[/red]")
        return
    if batch <= 0:
        console.print("[red]❌ Batch size must be greater than 0[/red]")
        return

    gen = GeneratorFactory.create("passphrase",
                                  words=words,
                                  separator=separator,
                                  language=language,
                                  strength=strength)
    phrases = [gen.generate() for _ in range(batch)]
    print_and_copy(phrases, "Generated Passphrases", copy, "Passphrase", as_json, plain, json_file)


# ---------------- Main ----------------
if __name__ == "__main__":
    cli()
