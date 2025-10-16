# Ending service

This page covers the technical steps for ending your 2i2c service and ensuring a smooth transition.

:::{admonition} Deciding whether to end service?
See the [community leadership guide on deciding to end service](../../community-lead/service-lifecycle/ending-service.md).
:::

## Timeline and communication

We recommend giving at least **30 days notice** before ending service to ensure proper transition:

1. **Contact 2i2c support**: [Contact support](../../support.md) with your planned end date
2. **Notify hub users**: Inform users about the timeline and their responsibilities for data export
3. **Coordinate with 2i2c**: Work with the 2i2c team to schedule final steps

## Exporting data

### User directories and files

Each hub user must download their own files:

1. Direct users to [download their home directory](../../user/service-lifecycle/offboarding.md)
2. Set a clear deadline for data export (at least 1 week before service end)
3. Remind users that data will be permanently deleted after service ends

### S3 bucket archives (if applicable)

If 2i2c has archived home directories to an S3 bucket:

1. Request access credentials from 2i2c support
2. Follow the [S3 archive download instructions](../../user/service-lifecycle/offboarding.md)
3. Download archives before the final service date

## Replicating your infrastructure (optional)

2i2c's infrastructure is fully open-source as part of our [Right to Replicate](https://2i2c.org/right-to-replicate) commitment.

If you want to continue running a JupyterHub independently:

1. See [](replicate.md) for step-by-step replication instructions
2. Review the [infrastructure repository](https://github.com/2i2c-org/infrastructure) for your hub's configuration

## Final steps

Once data is exported and any replication is complete:

1. **Confirm with 2i2c support** that all data export is complete
2. **Review final billing** for any outstanding cloud costs
4. **Infrastructure cleanup**: Cloud resources will be deprovisioned

## Questions?

Contact [2i2c support](../../support.md) for assistance with any aspect of ending service.