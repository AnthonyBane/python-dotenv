# python-dotenv example

Often we want to store configuration information locally that isn't shared with other people or is machine specific. This can be done easily through the use of the python-dotenv module which reads key-value pairs from a file and sets them as environment variables or saves them to a dictionary.

## Requirements

You must have the module python-dotenv installed.

``` cmd
pip install python-dotenv
```

## Norms

It is standard practice to include these variables inside a .env file. You would then add the .env file path to your gitignore file to ensure your changes, and thus secrets, are not committed to the repo.

If you had a set of configuration settings you wanted to share, this could be done by creating a .env.shared file with an accompanying .env.secret file. The shared file is not added to the gitignore and is therefore shared, but the secret file is and therefore local. These can be combined through a method into a single dictionary, see the combined_dotenv_example.py script for this.

## Repo Contents

``` txt
| README.md                     <- this file
| LICENSE                       <- license information
| .gitignore                       <- gitignore file

| simple_dotenv_example.py      <- Example using a .env file
| combined_dotenv_example.py    <- Example using .env.shared and .env.secret files
| .env                          <- Example .env file           
 
+-- Config                      <- Configuration files
    | .env.shared               <- Example shared configuration file
    | .env.secret               <- Example secret configuration file
```

You can read more about the python-dotenv package in their [documentation](https://pypi.org/project/python-dotenv/).
