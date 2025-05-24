**pybrainorg Implementation Roadmap**

**Phase 1: Core Essentials and Basic Simulation (MVP - Minimum Viable Product)**

*   **Objective:** Be able to create a simple organoid, simulate its activity with Brian2, and record spikes.
*   **Focus Modules:** `core`, `organoid`, `simulation` (partial), `visualization` (basic), `electrophysiology` (basic monitors).
*   **Tasks:**
    1.  **`core.neuron_models`**:
        *   Implement basic neuron models (e.g., LIF, simple Izhikevich, AdEx, QIF, simplified HH).
        *   Ensure they return dictionaries compatible with `brian2.NeuronGroup` (equations, parameters, threshold, reset, refractory, method).
    2.  **`core.synapse_models`**:
        *   Implement basic synapse models (e.g., static synapse with fixed weight, simple exponential synapse).
    3.  **`organoid.spatial`**:
        *   Functions to generate 3D coordinates (e.g., random in cube/sphere).
    4.  **`organoid.organoid.Organoid`**:
        *   `Organoid` class: initialization, methods to add `NeuronGroup`.
        *   Method to add `Synapses` connecting neuron groups (simple connectivity, e.g., all-to-all or random).
        *   Internal management of Brian2 objects and their positions.
    5.  **`electrophysiology.brian_monitors`**:
        *   Functions to create `SpikeMonitor` and `StateMonitor` (for Vm).
    6.  **`simulation.simulator.Simulator`**:
        *   `Simulator` class: initialization with an `Organoid`.
        *   Basic construction of the `brian2.Network` from the organoid.
        *   Method to add monitors (using `brian_monitors`).
        *   `run()` method to execute the simulation.
        *   `get_data()` method to retrieve data from monitors.
    7.  **`visualization.spike_plotter`**:
        *   Function for `raster_plot`.
        *   Function to plot Vm traces.
    8.  **Examples:** Notebooks `01_Creating_Your_First_Organoid` and `02_Running_a_Simple_Simulation_and_Recording_Spikes`.
    9.  **Tests:** Unit tests for models, organoid creation, and basic simulation.
    10. **Documentation:** Docstrings for implemented components.

**Phase 2: MEA Interaction and Expanded Electrophysiology**

*   **Objective:** Simulate stimuli and recordings via MEA, and persistently record data.
*   **Focus Modules:** `mea`, `electrophysiology` (full), `simulation` (expanded).
*   **Tasks:**
    1.  **`mea.mea.MEA`**:
        *   `MEA` class: define electrode geometry, map nearby neurons to electrodes.
    2.  **`electrophysiology.stimulus_generator`**:
        *   Functions to create `TimedArray` for different stimulus patterns (pulses, ramps, etc.).
    3.  **`simulation.simulator.Simulator`**:
        *   Integrate `MEA` object.
        *   `add_stimulus()` method: apply stimuli via MEA to target neurons.
        *   Logic to simulate MEA "reading" (e.g., simple LFP proxy, spikes from neurons near an electrode).
    4.  **`electrophysiology.data_persistence`**:
        *   `db_schema.py`: Define SQLite schema.
        *   `sqlite_writer.py`: Implement writing of simulation metadata, spikes, states.
        *   Integrate `SQLiteWriter` into `Simulator` to save data automatically.
    5.  **`core.neuron_models` / `electrophysiology.brian_monitors`**:
        *   Consider how to calculate an LFP proxy (e.g., summing synaptic currents, or a special `StateMonitor`).
    6.  **Examples:** Notebooks `05_MEA_Stimulation_and_Basic_Recording`, `06_Simulating_Spontaneous_Activity_and_LFP_Proxy`, `07_Patterned_Stimulation_and_Response_Analysis`, `11_Data_Persistence_Saving_and_Loading_with_SQLite`.
    7.  **Tests:** Tests for MEA, stimuli, MEA recording, data persistence.
    8.  **Documentation:** Docstrings and guides for new functionalities.

**Phase 3: Network Plasticity**

*   **Objective:** Implement synaptic and structural plasticity rules.
*   **Focus Modules:** `plasticity`.
*   **Tasks:**
    1.  **`plasticity.stdp`**:
        *   Implement STDP models (e.g., classic additive pair).
        *   Functions to integrate STDP equations into `Synapses` objects.
    2.  **`plasticity.structural_plasticity`**:
        *   Develop a strategy to simulate synapse formation/elimination (e.g., pool of potential synapses with activity-based activation/deactivation).
        *   Implement structural plasticity rules.
    3.  **(Optional) `plasticity.homeostatic`**:
        *   Implement a simple homeostatic rule (e.g., synaptic scaling).
    4.  **`simulation.simulator.Simulator`**:
        *   `add_plasticity_rule()` method to apply plasticity rules to specific synapses.
        *   Modify `build_network()` to incorporate plasticity models into `Synapses` creation.
    5.  **Examples:** Notebooks `08_Implementing_Synaptic_Plasticity_STDP` and `09_Simulating_Structural_Plasticity_Network_Formation`.
    6.  **Tests:** Tests to verify that plasticity rules modify weights/connections as expected.
    7.  **Documentation:** Detail how to use and configure plasticity rules.

**Phase 4: Calcium Imaging and Advanced Analysis**

*   **Objective:** Simulate calcium dynamics, analyze more complex data, and infer networks.
*   **Focus Modules:** `core` (calcium models), `analysis`, `visualization` (expanded).
*   **Tasks:**
    1.  **`core.neuron_models`**:
        *   Add equations for intracellular calcium dynamics and indicator fluorescence (e.g., GCaMP) to neuron models.
    2.  **`electrophysiology.brian_monitors`**:
        *   Functions to set up `StateMonitor` for recording calcium/fluorescence variables.
    3.  **`analysis.calcium_analysis`**:
        *   Functions to calculate ΔF/F, detect calcium events.
    4.  **`analysis.spike_analysis`**:
        *   Functions for burst analysis, synchrony.
    5.  **`analysis.network_inference`**:
        *   Implement `SpikeConnectivityInferrer` (e.g., with STTC, cross-correlation).
        *   Implement `CalciumConnectivityInferrer` (e.g., with Pearson correlation).
    6.  **`visualization.calcium_plotter`**:
        *   Plotting of calcium/ΔF/F traces, calcium activity maps.
    7.  **`visualization.network_plotter`**:
        *   Visualization of inferred functional connectivity graphs.
    8.  **Examples:** Notebooks `10_Modeling_Calcium_Dynamics_and_Fluorescence_Imaging`, `12_Inferring_Functional_Networks_from_Spike_Data`, `13_Inferring_Functional_Networks_from_Calcium_Data`, `14_Advanced_Analysis_Bursting_and_Synchrony`.
    9.  **Tests:** Tests for calcium models, analysis, and inference modules.
    10. **Documentation:** Guides for calcium simulation and new analysis tools.

**Phase 5: Refinement, Utilities, and Use Cases**

*   **Objective:** Improve usability, add utilities, and demonstrate applications.
*   **Focus Modules:** `utils`, complex examples.
*   **Tasks:**
    1.  **`utils.config_parser`**:
        *   Implement reading of simulation configurations from files (JSON, YAML).
    2.  **`electrophysiology.data_persistence.sqlite_reader`**:
        *   Implement functions to conveniently read data from SQLite.
    3.  **Refactoring and Optimization:** Review code for performance and clarity improvements.
    4.  **Advanced Examples:** Notebook `15_Example_Modeling_a_Simplified_Disease_Phenotype`.
    5.  **Documentation:** Complete all guides, tutorials, and the API reference.
    6.  **Tests:** Increase test coverage.

