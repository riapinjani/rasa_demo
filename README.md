## Banking example chatbot

### Run the bot

Use `rasa train` to train a model.

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions
```
Then to talk to the bot, run:
```
rasa shell --debug
```

Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working
under the hood. To simply talk to the bot, you can remove this flag.


You can also try out your bot locally using Rasa X by running
```
rasa x
```
### Things you can ask the bot
- Check Balance
- Make a transaction
- FAQs
- chitchat

### Overview of the file structure
data/nlu.md <-- Training data for NLU model\
data/stories.md <-- Training data for dialogue model\
actions/actions.py <-- custom actions\
domain.yml <-- the domain file, including bot response templates\
config.yml <-- training configurations for the NLU pipeline and policy ensemble\
tests <-- end-to-end test stories

