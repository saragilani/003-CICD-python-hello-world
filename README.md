# 003-CICD-python-hello-world

Note: the name of our deployed application is: asg-ak-python-hello-world

Note: this repo has a failing pipeline. Can you fix it so that the tests pass and it deploys to Heroku?

## 1. Fork this repo

In order to have a working copy, fork this repository. You will need to enable workflows in your repository which will automatically create a pipeline which you can see by accessing the "Actions" tab here in GitHub.

In the .github/workflows/pipeline.yml file you will find the code which defines our pipeline. There are three different "jobs" - *Build*, *Test* and *Deploy*.

&bigstar; On the Actions tab, click "Run Workflow" to start the pipeline for the first time.

Note that if you make a small change (e.g. the name of a step) it will trigger the pipeline automatically.

![forked-repo](https://user-images.githubusercontent.com/910448/136774899-304070b8-ee52-4035-9890-41065ba53c96.png)

## 2. Fix the failing Test stage

![broken-pipeline](https://user-images.githubusercontent.com/910448/136773118-3f24f41b-3c49-47a5-a756-265f327b4c25.png)

You can see that the Test stage ("job" in GitHub lingo) is failing, and that the Deploy stage doesn't even get to run.

&bigstar; Click the test stage to navigate to an expanded view showing the details of what's going wrong.

Once you have found the source of the problem, you will need to modify the file in question and commit your changes back to your repository.

## 3. Fix the Deploy stage

![broken-pipeline-deploy](https://user-images.githubusercontent.com/910448/136778503-eaa780d5-df05-4c67-b786-54f784e7b60c.png)

&bigstar; Click the Deploy step to determine what's not working. Note that there's not quite enough detail shown to debug the issue.

![broken-pipeline-deploy-reason](https://user-images.githubusercontent.com/910448/136778511-ee9bd735-3643-40c2-b7af-07b015418661.png)

&bigstar; Inspect the pipeline code at .github/workflows/pipeline.yml. You should see that it's trying to deploy the application to Heroku using two secrets, HEROKU_API_KEY and HEROKU_APP_NAME.


```
  deploy:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v2

      - name: Deploy to Heroku
        run: |
          git remote add heroku https://heroku:${{ secrets.HEROKU_API_KEY }}@git.heroku.com/${{ secrets.HEROKU_APP_NAME }}.git
          git push heroku `git subtree split --prefix src main`:/refs/heads/main --force
```

&bigstar; Sign up for a Heroku account using https://signup.heroku.com/python

&bigstar; Create an application on Heroku

![heroku-create-app](https://user-images.githubusercontent.com/910448/136778303-051d19e3-bfed-460e-a896-e230c5905f84.png)

&bigstar; Retrieve your API key

You can find your API key in your Heroku account's Account Settings > Account tab


*Note: don't disclose this to other people. This API key allows programmatic access to your Heroku account.*

![heroku-api-key](https://user-images.githubusercontent.com/910448/136779185-9c46a7e7-71c0-49c0-ae2a-2a2a2f050e05.png)

&bigstar; Update your repository, adding both HEROKU_API_KEY and HEROKU_APP_NAME as Repository Secrets

After adding HEROKU_API_KEY it should look like this:

![secrets](https://user-images.githubusercontent.com/910448/136779412-fe866160-b122-49bb-8442-782764e31cb6.png)

Adding HEROKU_APP_NAME:

![adding-a-secret](https://user-images.githubusercontent.com/910448/136779420-a727aa48-ecf5-46bc-a161-47a79d17d32e.png)


&bigstar; Re-run your workflow using the "Re-run all jobs" button as shown in the top-right below:

![re-run job](https://user-images.githubusercontent.com/910448/136779447-bd289240-838c-4d63-b62d-e337f7e90568.png)


## Finish

If everything went well, you should now have a green pipeline. Visiting the URL for your Heroku app should display the message "Hello world".

Your Heroku URL is usually https://{your-application-name}.herokuapp.com.

## Extension (optional)

If you've finished the above with time to spare, try this bonus activity...

Let's imagine users of the Hello World app require a second route, '/goodbye', which will output the text 'Goodbye'.

Following the discipline of TDD, add a new failing test to `src/test_main.py` which will test this new route.

+ *What happens when you commit the updated test code to main?*
+ *Can the app still be accessed at the URL?* and *Why is this?*
