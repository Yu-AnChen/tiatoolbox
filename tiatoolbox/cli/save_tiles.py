# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# The Original Code is Copyright (C) 2021, TIA Centre, University of Warwick
# All rights reserved.
# ***** END GPL LICENSE BLOCK *****

"""Command line interface for save_tiles."""
from tiatoolbox.cli.common import (
    cli_file_type,
    cli_img_input,
    cli_output_path,
    cli_tile_objective,
    cli_tile_read_size,
    cli_verbose,
    prepare_file_dir_cli,
    tiatoolbox_cli,
)


@tiatoolbox_cli.command()
@cli_img_input()
@cli_output_path(
    usage_help="Path to output directory to save the output.", default="tiles"
)
@cli_file_type()
@cli_tile_objective()
@cli_tile_read_size()
@cli_verbose()
def save_tiles(
    img_input,
    output_path,
    file_types,
    tile_objective_value,
    tile_read_size,
    verbose=True,
):
    """Display or save WSI metadata."""
    from tiatoolbox import wsicore

    files_all, output_path = prepare_file_dir_cli(
        img_input, output_path, file_types, "save", "tiles"
    )

    for curr_file in files_all:
        wsicore.save_tiles.save_tiles(
            input_path=curr_file,
            output_dir=output_path,
            tile_objective_value=tile_objective_value,
            tile_read_size=tile_read_size,
            verbose=verbose,
        )
