{ pkgs ? import <nixpkgs> {}}:
  pkgs.mkShell {
    nativeBuildInputs = let
      env = pyPkgs : with pyPkgs; [
        matplotlib
        numpy
      ];
    in with pkgs; [
      (python39.withPackages env)
    ];
}
