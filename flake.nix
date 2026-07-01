{
  description = "A minimal UV-to-NixOS devShell for the BiteTrack API";
  ## check: pydevtools.com/handbook/how-to/how-to-use-uv-on-nixos/

  inputs = {
    # Pin to NixOS stable
    # https://nixos.wiki/wiki/Nix_channels -- checked: 2026-06-29
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
    flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = { self, nixpkgs, flake-utils }:
      flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
       
      in {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [ uv ruff];
        };
      });
}
