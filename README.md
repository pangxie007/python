<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: animations|bazel|benchpress|common|compiler|compiler-cli|core|
  │                          elements|forms|http|language-service|localize|platform-browser|
  │                          platform-browser-dynamic|platform-server|router|service-worker|
  │                          upgrade|zone.js|packaging|changelog|docs-infra|migrations|
  │                          devtools
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test

type can be one of the following:
    * build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
    * ci: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
    * docs: Documentation only changes
    * feat: A new feature
    * fix: A bug fix
    * perf: A code change that improves performance
    * refactor: A code change that neither fixes a bug nor adds a feature
    * test: Adding missing tests or correcting existing tests

scope could be anything specifying place of the commit change. For example $location, $browser, $compile, $rootScope, ngHref, ngClick, ngView, etc...

summary is a very short description of the change: