<template>
  <Experiment title="causal-implicature-variation">
    <InstructionScreen :title="'Welcome'">
      This is a sample introduction screen.
    </InstructionScreen>

    <template v-for="(trial, i) of trials">
      <Screen :key="i">
        <Slide>
          <p><strong>Band:</strong> {{ trial.A }}</p>
          <p>
            <strong>Album:</strong> {{ trial.B }}
          </p>
          <p>
            Rating: <strong>{{ trial.C }}</strong>
          </p>
          <p><strong>Question:</strong> Do you agree?</p>
          <ForcedChoiceInput
            :response.sync="$magpie.measurements.response"
            :options="['yes', 'hell, yesss!']"
            @update:response="$magpie.saveAndNextScreen()"
          />
          <Record
            :data="{
              trialNR: i,
              band: trial.A,
              album: trial.B,
              rating: trial.C
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
    return { trials: _.shuffle(trials)};
  },
  computed: {
    // Expose lodash to template code
    _() {
      return _;
    }
  }
};
</script>
