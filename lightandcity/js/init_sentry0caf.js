(function() {
  try {
    const EXTRA_KEY = "ROUTE_TO";
    const SENTRY_FO_SHOP_DSN = "https:
    const transport = Sentry.makeMultiplexedTransport(Sentry.makeFetchTransport,
      (args) => {
        const event = args.getEvent();
        if (event && event.extra && EXTRA_KEY in event.extra && Array.isArray(event.extra[EXTRA_KEY])) {
          return event.extra[EXTRA_KEY];
        }
        return [];
      });
    const SENTRY_ENABLED_SITES = {
      "닥터피엘": "S20240510bb273a9dcaf2f",
      "톡스웰": "S2023112193f6b6f5df998",
      "대한민국농수산": "S202503072a75d91d55d18",
      "모무": "S202303281d5896e2ed8fe",
      "호무로": "S20220211b601322b3a563",
      "테스트": "S2017090859b1e4072a107"
    };
    Sentry.init({
      dsn: SENTRY_FO_SHOP_DSN,
      environment: TEST_SERVER ? "development" : "production",
      integrations: [Sentry.moduleMetadataIntegration()],
      transport,
      sampleRate: (SITE_CODE === SENTRY_ENABLED_SITES.호무로 || SITE_CODE === SENTRY_ENABLED_SITES.테스트) ? 1 : 0.05,
      beforeSend: (event) => {
        if (event?.exception?.values?.[0]?.stacktrace?.frames) {
          const frames = event.exception.values[0].stacktrace.frames;
          const handled = !!event?.exception?.values?.[0]?.mechanism?.handled;
          const routeTo = frames.filter((frame) => frame.module_metadata && frame.module_metadata.dsn).map((v) => v.module_metadata).slice(-1);
          if (handled && routeTo.length) {
            event.extra = {
              ...event.extra,
              [EXTRA_KEY]: routeTo,
            };
            return event;
          }
        }
        if (Object.values(SENTRY_ENABLED_SITES).includes(SITE_CODE)) {
          if (SITE_CODE === SENTRY_ENABLED_SITES.호무로 || SITE_CODE === SENTRY_ENABLED_SITES.테스트) {
            if (event.message && event.message.includes('DEBUG')) {
              return event;
            }
            return null;
          }
          return event;
        }
        return null;
      },
    });
    Sentry.setTag("site_code", SITE_CODE);
    Sentry.setTag("unit_code", UNIT_CODE);
  } catch (error) {
    console.warn("Issue during Sentry initialization: Some error tracking features may be limited.", error);
  }
})();