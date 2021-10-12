{
  description = "dcrest Python package";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.simpleFlake {
      inherit self nixpkgs;
      name = "dcrest";
      # overlay = ./overlay.nix;
      shell = ./shell.nix;
    };
}
