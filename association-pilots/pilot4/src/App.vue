<template>
  <Experiment title="causal-implicature-variation">
    <InstructionScreen :title="'Welcome'">
      This is a short short survey where you will read a brief conversation between two people answer a single question about how you understand it.
    </InstructionScreen>

    <template v-for="(trial, i) of trials">
      <Screen :key="i">
        <Slide>
          <p style='text-align: left; text-indent: 50px;'>Suppose you overhead two scientists having a discussion about some lab results:</p> 
          <p style='text-align: left; text-indent: 150px;'>
            <strong>Scientist 1:</strong> {{ trial.QUD }}
          </p>
          <p style='text-align: left; text-indent: 150px;'>
            <strong>Scientist 2:</strong> {{ trial.statement }} 
          </p> 
          <p style='text-align: left; text-indent: 50px;'>
            <strong>Question:</strong> Given what the scientists have said, which of the following do you think is more likely?
          </p>
          <br>
          <ForcedChoiceInput 
            :response.sync="$magpie.measurements.response"
            :options="[trial.choice1, trial.choice2]"
            @update:response="$magpie.saveAndNextScreen()"
          />
          <Record
            :data="{
              trialNR         : i,
              QUDTarget       : trial.QUDTarget,
              statementFirst  : trial.statementFirst,
              treatment       : trial.treatment,
              name1           : trial.name1,
              name2           : trial.name2,
              QUD             : trial.QUD,
              statement       : trial.statement,
              choiceNameFirst : trial.choiceNameFirst,
              choice1         : trial.choice1,
              choice2         : trial.choice2,
              response        : trial.C
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
