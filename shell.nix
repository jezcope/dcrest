{ pkgs ? import <nixpkgs> { } }:

with pkgs;

mkShell {
  buildInputs = [ (python3.withPackages (py: [ py.poetry py.ipython ])) ];
}
