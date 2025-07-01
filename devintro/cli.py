import click
from .profile import load_profile, Profile


@click.group()
@click.option('--config', type=click.Path(exists=True), help='Path to profile config file')
@click.pass_context
def cli(ctx: click.Context, config: str | None):
    """Developer introduction command line interface."""
    ctx.obj = load_profile(config)


@cli.command()
@click.pass_obj
def info(profile: Profile):
    """Show basic information."""
    click.echo(profile.bio)


@cli.command()
@click.pass_obj
def skills(profile: Profile):
    """List skills."""
    click.echo("\n".join(profile.skills))


@cli.command()
@click.pass_obj
def projects(profile: Profile):
    """List projects."""
    click.echo("\n".join(profile.projects))


@cli.command()
@click.pass_obj
def contacts(profile: Profile):
    """Show contact information."""
    for key, value in profile.contacts.items():
        click.echo(f"{key}: {value}")
