from eth2spec.gen_helpers.gen_from_tests.gen import run_state_test_generators
from eth2spec.phase0 import spec as spec_phase0
from eth2spec.altair import spec as spec_altair
from eth2spec.phase1 import spec as spec_phase1
from eth2spec.test.context import PHASE0, PHASE1, ALTAIR


specs = (spec_phase0, spec_altair, spec_phase1)


if __name__ == "__main__":
    phase_0_mods = {key: 'eth2spec.test.phase0.block_processing.test_process_' + key for key in [
        'attestation',
        'attester_slashing',
        'block_header',
        'deposit',
        'proposer_slashing',
        'voluntary_exit',
    ]}
    altair_mods = {
        **{key: 'eth2spec.test.altair.block_processing.test_process_' + key for key in [
            'sync_committee',
        ]},
        **phase_0_mods,
    }  # also run the previous phase 0 tests
    phase_1_mods = {**{key: 'eth2spec.test.phase1.block_processing.test_process_' + key for key in [
        'attestation',
        'chunk_challenge',
        'custody_key_reveal',
        'custody_slashing',
        'early_derived_secret_reveal',
        'shard_transition',
    ]}, **phase_0_mods}  # also run the previous phase 0 tests (but against phase 1 spec)

    all_mods = {
        PHASE0: phase_0_mods,
        ALTAIR: altair_mods,
        PHASE1: phase_1_mods,
    }

    run_state_test_generators(runner_name="operations", specs=specs, all_mods=all_mods)
