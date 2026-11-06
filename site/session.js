/* Campaign details: update this object if EGU changes the session code or URL.
   Keep the matching HTML fallback, social artwork and share copy in sync. */
const session = Object.freeze({
  code: 'HS3.8',
  url: 'https://meetingorganizer.copernicus.org/EGU27/session/61787',
  supportUrl: 'https://www.egu27.eu/attendance/financial_support_and_waivers.html',
  supportDeadline: '1 December 2026 · 13:00 CET',
  supportDeadlineIso: '2026-12-01T13:00:00+01:00',
  repository: 'https://github.com/Jorub/egu27-hs3-8-precip-et-dataset-for-hydrology',
});

document.querySelectorAll('[data-session-code]').forEach((element) => {
  element.textContent = session.code;
});
document.querySelectorAll('[data-session-link]').forEach((element) => {
  element.href = session.url;
});
document.querySelectorAll('[data-repository-link]').forEach((element) => {
  element.href = session.repository;
});
document.querySelectorAll('[data-support-link]').forEach((element) => {
  element.href = session.supportUrl;
});
document.querySelectorAll('[data-support-deadline]').forEach((element) => {
  element.textContent = session.supportDeadline;
  element.dateTime = session.supportDeadlineIso;
});
document.title = `Precipitation and Evapotranspiration Datasets for Hydrological Studies: Development, Evaluation, and Applications · EGU27 ${session.code}`;
