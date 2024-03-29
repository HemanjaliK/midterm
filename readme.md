**Design Patterns:**

Command Pattern:

The Command pattern is used to encapsulate a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations. This pattern is visible in the implementation of **Command** and **CommandHandler** classes.

- **Command (Command class):** An abstract base class that declares an interface for executing operations. See [Command].
- **ConcreteCommand (AddCommand, MultiplyCommand, etc.):**Classes that extend the Command interface to implement specific operations. See [AddCommand].
- **Invoker (CommandHandler class):** Asks the command to carry out the request. See #(CommandHandler).
- **Client (App class):** Creates a ConcreteCommand object and sets its receiver. See [App].

Factory Pattern:

While not explicitly implemented in the provided code, the method '**load_plugins**' in '**App**' resembles a Factory method pattern by dynamically loading and instantiating plugins (commands) without specifying the exact class of objects to create.

**Environment Variables:**
Environment variables are used for configuration that changes between environments; for example, 'DEVELOPMENT', 'TESTING', 'PRODUCTION'. The '**App**' class loads these variables at startup using the '**dotenv**'package and makes them available throughout the application.

- **Usage:** See the implementation in App for how environment variables are loaded and accessed.

**Logging:**

Logging is configured and used across the application to record various levels of information (INFO, ERROR, etc.), which aids in debugging and monitoring the application's runtime behavior.

- **Configuration:** A configuration file ('**logging.conf**') defines the logging behavior, such as log file rotation and formatting. See logging.conf.
- **Usage:** The '**logging**' module is used within commands and the app framework to log messages. For example, see usage in AddCommand.

**Exception Handling:**

LBYL (Look Before You Leap)

This approach checks for potential errors or conditions before making a call or accessing a resource. While not explicitly shown in the provided snippets, a typical LBYL implementation could involve checking if a file exists before trying to open it.

EAFP (Easier to Ask for Forgiveness than Permission)

This strategy is preferred in Python and involves trying to perform the operation and handling the exception if it fails. This approach is visible in the '**execute_command**' method of '**CommandHandler**', where it attempts to execute a command and catches a '**KeyError**' if the command does not exist.

- **Usage:** See CommandHandler for an EAFP example.

(link for the video):