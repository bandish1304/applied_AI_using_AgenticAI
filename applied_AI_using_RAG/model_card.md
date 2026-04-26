## Reflection and Ethics: Limitations and Biases

The summarization AI can reflect biases present in its training data and may miss important context or nuance, especially with short or ambiguous inputs. It generates summaries based on patterns, not true understanding, so results should always be reviewed by a human. Users should not rely on the AI for critical decisions without oversight.

## Could your AI be misused, and how would you prevent that?

Yes, the AI could be misused to generate misleading or biased summaries, or to process sensitive information without proper oversight. To prevent misuse, I recommend using the AI only for low-stakes, educational, or exploratory tasks, and always having a human review outputs before acting on them. Sensitive or critical content should never be processed without explicit safeguards and user awareness.

## What surprised you while testing your AI's reliability?

I was surprised by how the summarizer sometimes produced accurate but differently worded outputs than expected, making strict tests fail even when the summary was good. It also handled most typical cases well, but struggled with very short or ambiguous inputs.

## Collaboration with AI

The AI was helpful when it suggested moving the check_guess function into a separate logic_utils module, which improved code organization and testability. However, it once gave a flawed suggestion by recommending string-based comparisons for numbers, which caused incorrect game hints until corrected.

