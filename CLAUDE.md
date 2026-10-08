# 학원 프로젝트 통합 허브

이 저장소(`kj998777/-`)는 학원 관련 작업을 Claude Code 한 곳에서 지시하기 위한 **허브**입니다.
실제 코드는 아래 저장소들에 있으며, 세션에서 `/home/user/<이름>` 경로로 작업합니다.
세션에 저장소가 없으면 `add_repo`(owner `kj998777`)로 붙이고 `/home/user/<이름>`에 clone 합니다.

| 저장소 | 경로 | 역할 |
|---|---|---|
| `kj998777/medicmath-site` | `/home/user/medicmath-site` | 학원 **홍보·입학 사이트** (메인 문구, 프로그램·교습비, 강사진, 성적 향상 사례, 후기, FAQ, 입학 신청 폼, SEO, 문자 알림) |
| `kj998777/kj998666` | `/home/user/kj998666` | **학원 시험관리 시스템**(메딕차트) — 시험·정답, 반/학생, 자동채점, 배치고사, 문제은행, 학습지, 튜터 검수·포인트, 블로그 도구(`scripts/blog`) |
| `kj998777/-` | `/home/user/-` | 이 허브 + 예전 함수 그리기 파이썬 스크립트 |

두 사이트는 **같은 Supabase 프로젝트**를 씁니다. 스택: Next.js 14 (App Router) + TypeScript + Tailwind + Supabase, Vercel 배포(region `icn1`).

## 요청 → 어디서 처리하나

- 홈페이지 문구·사진·프로그램·교습비·강사·사례·후기·FAQ → `medicmath-site`
  - 기본값은 `lib/site.ts`, 실제 표시는 관리자 화면에서 저장한 `site_content` 표가 우선 (`lib/content.ts`).
  - 운영 중인 문구만 바꾸는 거라면 관리자 화면(`app/admin/(panel)/content`)에서 바꾸는 편이 코드 수정보다 빠를 수 있음 — 사용자에게 먼저 알려줄 것.
- 입학 신청·문자 알림 → `medicmath-site` (`components/AdmissionForm.tsx`, `lib/admission.ts`, `lib/notify.ts`, SOLAPI)
- SEO·사이트맵·검색엔진 인증 → `medicmath-site` (`app/sitemap.ts`, `app/robots.ts`, `lib/seoVerify.ts`, `public/google*.html`)
- 시험·채점·학생·반·배치고사·학습지·튜터 → `kj998666`
- 블로그 글/이미지 작업 → `kj998666/scripts/blog`, `kj998666/lib/blog`
- DB 구조 변경 → 해당 저장소 `supabase/` 에 다음 번호 SQL 파일을 추가 (`medicmath-site/supabase/00NN_*.sql`, `kj998666/supabase/migrations/00NN_*.sql`). 같은 DB이므로 두 저장소 마이그레이션이 서로 충돌하지 않는지 확인.

## 검사 명령

- `medicmath-site`: `npm run lint`, `npm run build`
- `kj998666`: `npm run lint`, `npm run build`, 테스트는 `npx tsx test/<이름>.test.ts` (예: `npm run test:grading`)
- 의존성이 없으면 먼저 `npm install`.

## 작업 규칙

- 사용자는 원장님(비개발자)입니다. 답변·커밋 메시지는 한국어로, 쉬운 말로.
- 각 저장소 안의 CLAUDE.md / `.claude/skills` 가 있으면 그것이 우선.
- 변경은 해당 저장소에서 브랜치를 만들어 커밋·푸시. PR·머지는 사용자가 요청할 때만.
- `.env` 값, `SUPABASE_SERVICE_ROLE_KEY`, SOLAPI 키는 절대 커밋하거나 화면에 출력하지 않기.
- 홈페이지의 교습비 게시표는 교육청 등록값 그대로여야 함(학원법) — 임의로 바꾸지 말고 확인받기.
- 성적 사례·후기는 사용자가 준 실제 내용만 사용. 지어내지 않기.
