<template>
  <Experiment title="causal-implicature-variation">
    <InstructionScreen :title="'Welcome'">
      This is a short short survey where you will read a piece of information and answer a single question about it.

      The task may seem very easy at first, but we ask you to <strong>think about the answer for a moment before you make a decision</strong>.
    </InstructionScreen>

    <template v-for="(trial, i) of trials">
      <Screen :key="i">
        <Slide>
          <p>Suppose you are reading a newspaper report about a disease called 
            <span v-if="trial.targeted=='first'">{{ trial.name1 }}</span>
            <span v-else>{{ trial.name2 }}</span>.</p> 
          <p>In the article, you encounter the following piece of information:</p>
          <p>
            <strong>{{ trial.prompt }}</strong> 
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
              targeted       : trial.targeted,
              position       : trial.targeted == 'first' ? 'subj' : 'PP',
              modifier       : trial.itemType,
              name1          : trial.name1,
              name2          : trial.name2,
              prompt         : trial.prompt,
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

console.log("Hi, I'm Dan's first experiment. Hope, I'm here to stay.")

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
