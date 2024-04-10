<template>
  <Experiment title="causal-implicature-variation">
    <InstructionScreen :title="'Welcome'">
      Hi! Thanks for taking part!
      <br>
      This short survey consists of three tasks.
      Each part will be introduced in turn.
    </InstructionScreen>

    <InstructionScreen :title="'Task 1'">
      Your next task is to type three different descriptions to communicate the same idea.
    </InstructionScreen>

    <template v-for="(trial, i) of trials_repeat">
      <Screen :key="i">

        <!-- trial 1 -->
        <Slide>
          <p>
            Produce a description to express that <strong>{{ name1 }} causes {{ name2 }}</strong>. (Trial {{i+1}} of 3.)
            <br>
            <div v-if="group == 'cause-first'">
              <strong>Your sentence must start with "{{name1}}"!</strong>
              <br>
              <span style="color: gray">Example: '{{ name1 }} brings about {{ name2 }}.'</span>
              <br>
              <span style="color: gray">Feel free to abbreviate like this: '{{ name1.charAt(0) }} brings about {{ name2.charAt(0) }}.'</span>
            </div>
            <div v-if="group == 'effect-first'">
              <strong>Your sentence must start with "{{name2}}"!</strong>
              <br>
              <span style="color: gray">Example: '{{ name2 }} follows from {{ name1 }}.'</span>
              <br>
              <span style="color: gray">Feel free to abbreviate like this: '{{ name2.charAt(0) }} follows from {{ name1.charAt(0) }}.'</span>
            </div>
          </p>
          <TextareaInput
            :response.sync= "$magpie.measurements.response"
          />
          <p v-if= "$magpie.measurements.response && $magpie.measurements.response.length >= 0">
          <button @click="$magpie.saveAndNextScreen();">Submit</button>
          </p>
          <Record
            :data="{
              group          : group,
              trialNR        : i+1,
              trialType      : 'generation-task-1',
              name1          : trial.name1,
              name2          : trial.name2,
              name3          : trial.name3,
              name4          : trial.name4,
              name5          : trial.name5,
              name6          : trial.name6,
              prompt         : '-',
              choice1        : trial.choice1,
              choice2        : trial.choice2,
              response       : trial.C
            }"
          />
        </Slide>
      </Screen>
     </template>

    <InstructionScreen :title="'Task 2'">
      The next task is almost the same as the last one, but this time you should start with the {{group == 'cause-first' ? 'effect' : 'cause'}}, rather than the {{group == 'cause-first' ? 'cause' : 'effect'}} in your descriptions.
    </InstructionScreen>

    <template v-for="(trial, i) of trials_repeat">
      <Screen :key="i">

        <!-- trial 1 -->
        <Slide>
          <p>
            Produce a description to express that <strong>{{ name3 }} causes {{ name4 }}</strong>. (Trial {{i+1}} of 3.)
                        <div v-if="group == 'effect-first'">
              <strong>Your sentence must start with "{{name3}}"!</strong>
              <br>
              <span style="color: gray">Example: '{{ name3 }} brings about {{ name4 }}.'</span>
              <br>
              <span style="color: gray">Feel free to abbreviate like this: '{{ name3.charAt(0) }} brings about {{ name4.charAt(0) }}.'</span>
            </div>
            <div v-if="group == 'cause-first'">
              <strong>Your sentence must start with "{{name4}}"!</strong>
              <br>
              <span style="color: gray">Example: '{{ name4 }} follows from {{ name3 }}.'</span>
              <br>
              <span style="color: gray">Feel free to abbreviate like this: '{{ name4.charAt(0) }} follows from {{ name3.charAt(0) }}.'</span>
            </div>
          </p>
          <TextareaInput
            :response.sync= "$magpie.measurements.response"
          />
          <p v-if= "$magpie.measurements.response && $magpie.measurements.response.length >= 0">
          <button @click="$magpie.saveAndNextScreen();">Submit</button>
          </p>
          <Record
            :data="{
              group          : group,
              trialNR        : i+1,
              trialType      : 'generation-task-2',
              name1          : trial.name1,
              name2          : trial.name2,
              name3          : trial.name3,
              name4          : trial.name4,
              name5          : trial.name5,
              name6          : trial.name6,
              prompt         : '-',
              choice1        : trial.choice1,
              choice2        : trial.choice2,
              response       : trial.C
            }"
          />
        </Slide>
      </Screen>
     </template>

    <InstructionScreen :title="'Task 3'">
      In the last task, you are given a description similar to the ones you just produced.
      Your task is to judge which of two interpretations is more likely.
      This is essentially the inverse of the previous two tasks: ask yourself for which case it is most likely that another person would have used the given description!
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
              group          : group,
              trialNR        : i+1,
              trialType      : 'FC-interpretation',
              name1          : trial.name1,
              name2          : trial.name2,
              name3          : trial.name3,
              name4          : trial.name4,
              name5          : trial.name5,
              name6          : trial.name6,
              prompt         : trial.prompt,
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

const trials_selected = _.shuffle(trials).slice(-1);

const group = _.shuffle(["cause-first", "effect-first"])[0];

console.log(group)
console.log("association-pilots/pilot7")

export default {
  name: 'App',
  data() {
    return {
      name1: trials_selected[0].name1,
      name2: trials_selected[0].name2,
      name3: trials_selected[0].name3,
      name4: trials_selected[0].name4,
      name5: trials_selected[0].name5,
      name6: trials_selected[0].name6,
      trials: trials_selected,
      group: group,
      // five repetitions of 'trials'
      trials_repeat: trials_selected.concat(trials_selected).concat(trials_selected),
    };
  },
  computed: {
    // Expose lodash to template code
    _() {
      return _;
    }
  }
};
</script>
