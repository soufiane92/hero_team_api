### How to enrich the documentation

We are using mkdocs to generate our documentation. the purpose is to automate as much as possible the job and to deploy
it automatically to GitHub.

Mkdocs documentation can be found [here](https://www.mkdocs.org/user-guide/)

#### In a nutshell
- Add any new pages in the yml file mkdocs.yml located at the project root folder
- All pages are written in markdown described [here](https://www.markdownguide.org/basic-syntax/)
- To build documentation and access logs for warnings and errors, you can execute `mkdocs build`
- To generate the documentation, execute the following command `mkdocs gh-deploy` 

!!! Info
    * `gh-deploy` might fail pushing the result to github pages, it can be solved by
    * pushing the branch gh-pages yourself.