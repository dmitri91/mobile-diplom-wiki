def abs_path_from_project(relative_path: str):
    import helper
    from pathlib import Path

    return (
        Path(helper.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
