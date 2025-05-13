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

中文版：
<type>(<scope>): <short summary>
│       │             │
│       │             └─⫸ 简单总结。不要大写。结尾没有句点。
│       │
│       └─⫸ 提交范围：animations|bazel|benchpress|common|compiler|compiler-cli|core|元素|表单|http|语言服务|本地化|平台浏览器|
│               平台浏览器动态|平台服务器|路由器|服务工作者|upgrade|zone.js|packaging|changelog|docs-infra|migrations|开发工具
│               
│               
│               
│
└─⫸ 提交类型：build|ci|docs|feat|fix|perf|refactor|test

type 可以是以下值之一：
    * build：影响构建系统或外部依赖项的更改（示例范围：gulp、broccoli、npm）
    * ci：对 CI 配置文件和脚本的更改（示例范围：Travis、Circle、BrowserStack、SauceLabs）
    * docs：仅文档更改
    * feat：新功能
    * fix：一个 bug 修复
    * perf：提高性能的代码更改
    * refactor：既不修复 bug 也不添加功能的代码更改
    * test：添加缺失的测试或更正现有测试

summary 是更改的非常简短的描述：
scope 可以是指定提交更改位置的任何内容。例如 $location、$browser、$compile、$rootScope、ngHref、ngClick、ngView 等......