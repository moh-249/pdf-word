# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python3
    pkgs.jdk20
  ];

  # Sets environment variables in the workspace
  env = {
    VENV_DIR = ".venv";
    MAIN_FILE = "main.py";
    };
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"
      "ms-python.python"
      "ms-python.debugpy"
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
          web = {
        #   # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
        #   # and show it in IDX's web preview panel
        #   command = ["npm" "run" "dev"];
        #   manager = "web";
             # cwd = "subfolder"
            command = [
              "bash"
              "-c"
              ''
              # activate the virtual environment
              source $VENV_DIR/bin/activate
              
              # run app in hot reload mode on a port provided by IDX
              flet run $MAIN_FILE --web --port $PORT
              ''
            ];
            env = {PORT = "$PORT";};
            manager = "web";
         # Environment variables to set for your server
             
           };
         };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Example: install JS dependencies from NPM
        # npm-install = "npm install";
        create-venv = ''
          python -m venv $VENV_DIR

          if [ ! -f requirements.txt ]; then
            echo "requirements.txt not found. Creating one with flet..."
            echo "flet" > requirements.txt
          fi

          # activate virtual env and install requirements
          source $VENV_DIR/bin/activate
          pip install -r requirements.txt
        '';

        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "requirements.txt" "$MAIN_FILE" ];
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Example: start a background task to watch and re-build backend code
        # watch-backend = "npm run watch-backend";
        check-venv-existence = ''
          if [ ! -d $VENV_DIR ]; then
            echo "Virtual environment not found. Creating one..."
            python -m venv $VENV_DIR
          fi

          if [ ! -f requirements.txt ]; then
            echo "requirements.txt not found. Creating one with flet..."
            echo "flet" > requirements.txt
          fi

          # activate virtual env and install requirements
          source $VENV_DIR/bin/activate
          pip install -r requirements.txt
        '';

        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "requirements.txt" "$MAIN_FILE" ];
      };
    };
  };
}
