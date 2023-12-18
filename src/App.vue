<template>
  <Experiment title="causal-implicature-variation">
    <InstructionScreen :title="'Welcome'">
      This is a short short survey where you will read a piece of information and answer a single question about it.
    </InstructionScreen>

    <template v-for="(trial, i) of trials">
      <Screen :key="i">
        <Slide>
          <p>Suppose you read the following piece of information:</p>
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
              trialNR: i,
              condition: condition,
              name1:name1,
              name2:name2,
              prompt:prompt,
              choiceNameFirst:choiceNameFirst,
              choice1: choice1,
              choice2: choice2,
              response: trial.C
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
    return { trials: _.shuffle(trials)[1]};
  },
  computed: {
    // Expose lodash to template code
    _() {
      return _;
    }
  }
};
</script>
