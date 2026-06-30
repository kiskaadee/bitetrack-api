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
        libs = with pkgs;
          [
            stdenv.cc.cc.lib  # provides libstdc++ and libgcc_s
            glibc             # GNU C library - system calls, malloc, I/O processing
            zlib              # Compression library used extensively by Python's standard
            libffi            # Foreign-function-interface: calling conventions -> this allows code written in one language to call code written in another language
            openssl           # Cryptography and secure communication; required by Python's ssl module and networking packages such as `request`, `httpx` or `urllib3`
            postgresql        # Provides libpq.so required by psycopg / asyncpg
          ];
      in {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [ uv ruff];
        };
      });
}
