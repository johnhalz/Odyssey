# Overall Structure

The overall structure of the Odyssey database is shown below:

![Odyssey Structure](../img/database_structure_black.svg#only-light)
![Odyssey Structure](../img/database_structure.svg#only-dark)

## Fields
### Values & Units Tables
The values and units tables are one of the big strengths of the Odyssey framework, as they allow efficient and flexible storage of physical measurements in numerical, string or array forms. The units tables categorise units into different types, and conversions between units are accessible through the linear parameters defined with each unit.

While a base unit system is provided, users can add more units that are pertinent to their application if they need to.

#### Unit Type
This table defines the different types of units that are stored in the Unit table.
Each `UnitType` entry contains the following data:

- `name` (Text): The name of the unit type

#### Unit
As its name implies, the `Unit` table stores all of the units along with their conversion factors. To simplify unit conversion, we define a base unit for each unit type. For each unit, we then define the factors to convert from that unit back to the base unit. We use the following formula to convert a value in an arbitrary unit $x$ to a value $y$ in the base unit:

$$
y = \frac{\left(x + x_{offset} \right) \cdot multiplicand}{denominator} + y_{offset}
$$

Each `Unit` entry stores the following data:

- `name` (Text): The name of the unit
- `plural_name` (Text): The plural name of the unit
- `space_after_value` (Boolean): This field specifies if a space should be added between the value and the unit when printing the quantity (value and unit)
- `base_unit` (`Unit`): Link to the base unit of the unit type (will be null if the entry is the base unit)
- `abbreviation` (Text): Unit abbreviation
- `create_ts` (Date & Time): When this entry was created
- `x_offset` (Decimal): value
- `y_offset` (Decimal): value
- `multiplicand` (Decimal): value
- `denominator` (Decimal): value

#### Value

As multiple different types of values can be stored (strings, integers, decimal numbers and array), the `Value` table offers a single point where users can access this data. We have created this table so that developers that interact with Odyssey and its APIs have a high-performance (database-level) access point to values of any type (hence removing any logic that would required to check the desired type before querying the database). This can become very useful when searching for values, and is already used within the Odyssey database when another table links to a value.

Each `Value` entry is automatically created in the database when a new `String`, `Integer`, `Decimal` or `Array` is created and each `Value` entry contains the following data:

- `content_type`: The type of content that the entry is linking to (needed for database logic)
- `object_id` (Integer): The id of the object we are linking to
- `content_object`: This is the content of the object (this is what developers would need to access through this table)
- `create_ts` (Date & Time): When this entry was created

#### String

The `String` table contains all of the stored strings that are to be used as values. While using strings for containing numerical values is discouraged (there are specific tables for this). The odd case can still arise where a string is the only possible usable type.

Each `String` entry stores the following data:

- `string` (Text): The text of the string
- `create_ts` (Date & Time): When this entry was created
- `value` (`Value`): The value that the entry is connected to

#### Integer

The `Integer` table stores integer values that can be linked to a unit (although this is optional).

Each `Integer` entry stores the following data:

- `integer` (Integer): Integer value
- `unit` (`Unit`): A linked unit (can be left blank)
- `create_ts` (Date & Time): When this entry was created
- `value` (`Value`): The value that the entry is connected to

#### Decimal

The `Decimal` table stores any float number that can be linked to a unit (although this is optional).

Each `Decimal` entry stores the following data:

- `decimal` (Float): The decimal number's value
- `unit` (`Unit`): A linked unit (can be left blank)
- `create_ts` (Date & Time): When this entry was created
- `value` (`Value`): The value that the entry is connected to

#### Array

The `Array` table stores any array of numbers that can be linked to a unit (although this is optional).

Each `Array` entry stores the following data:

- `array` (`Array[Float]`): The array value
- `unit` (`Unit`): A linked unit (can be left blank)
- `create_ts` (Date & Time): When this entry was created
- `value` (`Value`): The value that the entry is connected to

#### Version

As configurations, software and hardware typically have versions assigned to them, we create a `Version` table to store all of these versions. We enforce the use of semantic versioning numbers with major, minor and patch number values.

Each `Version` entry stores the following data:

- `name` (Text): An associated name of the version
- `major` (Integer): The major version number
- `minor` (Integer): The minor version number
- `patch` (Integer): The patch version number
- `create_ts` (Date & Time): When this entry was created
- `description` (Text): An optional description of the version

#### Range

Typically when defining specifications, different ranges are defined that give a minimum and maximum bounds to the spec. The `Range` table is meant to hold such data.

Each `Range` entry stores the following data:

- `name` (Text): Name of the range
- `lower` (`Value`): Lower value
- `upper` (`Value`): Upper value
- `create_ts` (Date & Time): When this entry was created

### Hardware Tables

#### Hardware Model

The `HardwareModel` table is meant to store the model of the assembled hardware. It is meant to store the assembly logic (which part goes where, and where different sub-assemblies are).

Each `HardwareModel` entry stores the following data:

- `name` (Text): The name of the hardware in question
- `position` (Text): The position of the hardware in its assembly
- `parent` (`HardwareModel`): The parent assembly (this will be empty if this is the top assembly)
- `version` (`Version`): The version of this part
- `create_ts` (Date & Time): When this entry was created

#### Hardware

The `Hardware` table is meant to store all of the instances of physical hardware that were built. Each `Hardware` element is meant to reference a `HardwareModel` entry.

Each `Hardware` entry stores the following data:

- `serial_number` (Text): The serial number (or part number) of the hardware
- `model` (`HardwareModel`): The hardware model the this entry references
- `set` (Integer): The set in which this entry belongs
- `create_ts` (Date & Time): When this entry was created

#### Order

As hardware can be treated in different ways in production, (initial build-up, repair, service, etc.), we create order numbers to keep track of the different types of treatment a piece of hardware with the same serial number can go through. We call these `Order` numbers.

Each `Order` entry stores the following data:

- `number` (Integer): Order number
- `hardware` (`Hardware`): Link to the hardware in question
- `order_type` (Text): The type of order we are fulfilling
- `create_ts` (Date & Time): When this entry was created

#### Equipment

Throughout production, different equipment is used. Typically in a production environment we wish to keep track of the equipment used. This is what the `Equipment` table is for.

Each `Equipment` entry stores the following data:

- `name` (Text): Name of equipment
- `number` (Integer): Equipment number (in case there are more than one of the same equipment)
- `calibration_ts` (Date & Time): Date and time of when the equipment was last calibrated
- `parent` (`Equipment`): The parent equipment (this will be empty if this is the top assembly)
- `status` (Text): This field is meant to show if the equipment is being used, in calibration, or is free to use
- `create_ts` (Date & Time): When this entry was created

### Production Tables

#### Production Step Model

Assembly and testing of hardware does not happen in a single step! The `ProductionStepModel` table is meant to hold all of the steps required for any assembly, repair, calibration or service procedure. Similarly to `HardwareModel`, it contains all of the entries that the production steps will refer to.

Each `ProductionStepModel` entry stores the following data:

- `name` (Text): The name of the production step model
- `parent` (`ProductionStepModel`): The parent step model (so sub-steps can be added if necessary)
- `version` (`Version`): The version of this step model entry
- `step_number` (Integer): The step number (so that the order of each entry can be saved)
- `optional` (Boolean): Marker if the step is optional or not
- `create_ts` (Date & Time): When this entry was created

#### Production Step

The `ProductionStep` table is meant to store all of the production steps that actually happened. This allows the production team to keep track of where each piece of hardware that is being built is, and what progress is being made.

Each `ProductionStep` entry stores the following data:

- `order` (`Order`): The order of the hardware in question
- `production_step_model` (`ProductionStepModel`): The production step model that this production step refers to
- `status` (Text): The current status of this production step
- `operator` (`User`): The operator executing this step
- `start_ts` (Date & Time): The date and time of when this production step was started
- `end_ts` (Date & Time): The date and time of when this production step was completed

#### Configuration

As with any automated handling of hardware, the configuration of an assembly tool, testing jig, or other material can have different configurations set. This is what the `Configuration` table is meant to store.

Each `Configuration` entry stores the following data:

- `name` (Text): The name of the configuration
- `parent` (`Configuration` ): The parent configuration
- `value` (`Value`): The value of the configuration
- `hardware_model` (`HardwareModel`): The hardware model that this configuration applies to
- `production_step_model` (`ProductionStepModel`): The production step model that this configuration applies to
- `version` (`Version`): The version of the configuration
- `description` (Text): Description of the configuration
- `create_ts` (Date & Time): When this entry was created

### Testing Tables

Throughout production, various tests are run on the hardware in question to ensure a certain level of quality specified by the intended customer. The tables below are meant to store this data as well as any non-compliances that can come up.

#### Measurement

The purpose of this table is self-explanatory (it stores the measurements taken on a specific piece of hardware).

Each `Measurement` entry stores the following data:

- `parent` (`Measurement`): The parent measurement
- `name` (Text): The name of the measurement
- `value` (Value): The value of the measurement
- `create_ts` (Date & Time): When this entry was created
- `production_step` (`ProductionStep`): The production step in which this measurement was taken

#### Specification

Each measurement that is taken is usually compared with a pre-defined specification, which is what the `Specification` table stores.

Each `Specification` entry stores the following data:

- `name` (Text): The name of the specification
- `valid_range` (`Range`): The range in which we consider a measurement to be valid
- `applicable_scope` (`Range`): The range in which we would want to check if a measurement is within the valid range
- `hardware_model` (`HardwareModel`): The hardware to which the specification applies to
- `production_step_model` (`ProductionStepModel`): The production step model that the specification applies to
- `group` (`SpecificationGroup`): The specification group that this specification belongs to
- `description` (Text): Description of this specification
- `severity` (Text): How important this specification is
- `version` (`Version`): The version of this specification
- `create_ts` (Date & Time): When this entry was created

#### Specification Group

As many specifications can be defined and are typically linked together, the `SpecificationGroup` table allows the data owner to create different groups to link each specification together.

Each `SpecificationGroup` entry stores the following data:

- `name` (Text): The name of the group
- `commencement_date` (Date & Time): The date and time that this group's specifications come into effect
- `expiration_date` (Date & Time): The date and time that this group's specifications expire
- `create_ts` (Date & Time): When this entry was created

#### Result

Typically, each raw measurement (or a group of measurements) is processed into a resulting value, which is then compared with a list of specifications. The `Result` table is meant to hold onto this processed data.

Each `Result` entry stores the following data:

- `parent` (`Result`): The parent result
- `name` (Text): The name of the result
- `create_ts` (Date & Time): When this entry was created
- `measurements` (`Measurement` - Many-to-Many): List of measurements this result was computed from
- `specification` (`Specification`): The specification that this result should satisfy
- `value` (Value): The value of this result
- `processor` (`Processor`): The processor (that took the input measurements and computed this result)

#### Non-Compliance

A non-compliance (or NC for short) is created when a result does not meet a specification. The `NonCompliance` table holds all of these entries.

Each `NonCompliance` entry stores the following data:

- `result` (`Result`): The associated result
- `status` (Text): Indicator to mark if the non-compliance has been resolved, is under review, being resolved, etc.
- `decision` (Text): Text describing the decision made (preferably including the reason why) (mostly for documentation purposes)
- `reporter` (`User`): The user that reported the non-compliance
- `signer` (`User`): The user that signed to make the final decision on the non-compliance
- `create_ts` (Date & Time): When this entry was created
- `close_ts` (Date & Time): When the non-compliance was closed

#### Non-Compliance Comment

Every non-compliance would usualy spark a new discussion. This table is meant to hold the comments made on an NC.

Each `NonComplianceComment` entry stores the following data:

- `parent` (`NonComplianceComment`): The parent comment (if it exists)
- `non_compliance` (`NonCompliance`): The non-compliance entry that this comment refers to
- `author` (`User`): The author of the comment
- `content` (Text): The content of the comment
- `create_ts` (Date & Time): When this entry was created

#### Processor

As each measurement (or multiple measurements) might need to be post-processed into a result, the `Processor` table keeps track of the different post-processing scripts and actions that are taken for each measurement.

Each `Processor` entry contains the following data:

- `name` (Text): The name of the processor
- `create_ts` (Date & Time): When this entry was created
- `version` (`Version`): The version of the processor
- `production_step_model` (`ProductionStepModel`): The production step model that this processor refers to
- `file_path` (File path): The file path of the post-processing script