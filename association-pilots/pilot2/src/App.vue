<template>
  <Experiment title="causal-implicature-variation">
    <InstructionScreen :title="'Welcome'">
      This is a short short survey where you will read a piece of information and answer a single question about it.

      The task may seem very easy at first, but we ask you to <strong>think about the answer for a moment before you make a decision</strong>.
    </InstructionScreen>

    <template v-for="(trial, i) of trials">
      <Screen :key="i">
        <Slide>
          <p>Suppose you are reading a newspaper report about something called 
            <span v-if="trial.condition=='firstTopic'">{{ trial.name1 }}</span>
            <span v-else>{{ trial.name2 }}</span>.</p> 
          <p>In the article, you encounter the following piece of information:</p>
          <p>
            <strong>{{ trial.promptPart1 }}, {{ trial.promptPart2 }}</strong> 
          </p>
          <p>
            <strong>Question:</strong> Which of the following is more likely?
          </p>
          
          <ForcedChoiceInput
            :response.sync="$magpie.measurements.response"
            :options="[trial.choice1, trial.choice2]"
            @update:response="$magpie.saveAndNextScreen()"
          />
          <Record
            :data="{
              trialNR        : i,
              condition      : trial.condition,
              name1          : trial.name1,
              name2          : trial.name2,
              promptPart1    : trial.prompt_part1,
              promptPart2    : trial.prompt_part2,
              choiceNameFirst: trial.choiceNameFirst,
              choice1        : trial.choice1,
              choice2        : trial.choice2,
              response       : trial.C
            }"
          />
        </Slide>
      </Screen>
     </template>

    <PostTestScreen />

    <SubmitResultsScreen />

  </Experiment>
</template>

<script>
import trials from '../trials/trials.csv';
import _ from 'lodash';

console.log("association-pilots/pilot2")

export default {
  name: 'App',
  data() {
    return { trials: _.shuffle(trials).slice(-1)};
  },
  computed: {
    // Expose lodash to template code
    _() {
      return _;
    }
  }
};
</script>
