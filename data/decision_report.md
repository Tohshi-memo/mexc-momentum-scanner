# Decision Report

- generated_at: 2026-07-20T10:46:14.156097+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9106**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9106, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_BB3S | 4/16 | 25.0% | +1.39% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +7.03% | **+5.27%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.08% | **+2.62%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.40% | **+1.36%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.95% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$407.47** / 初期 $100.00 (+307.47%)
- 確定: 3168件 (Win 991 / Loss 1004 / Flat 1173) / skip 2499件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $407.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.12** / 初期 $100.00 (+27.12%)
- 確定: 1067件 (Win 278 / Loss 218 / Flat 571) / skip 1450件
- 成長率目線: 平均log +0.000225 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0701 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $127.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.15** / 初期 $100.00 (+1.15%)
- 確定: 305件 (Win 102 / Loss 134 / Flat 69) / pending 2件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.15

## 6. Latest Market Context

- 更新: 2026-07-20T10:46:06.658655+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=64280.0
- Funnel: target 884 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +112.78% | $17,761,160.11 |
| BANK/USDT:USDT | +76.65% | $120,451,322.50 |
| EVAA/USDT:USDT | +34.50% | $6,308,496.99 |
| PROM/USDT:USDT | +29.15% | $3,389,838.45 |
| PUMPFUN/USDT:USDT | +15.51% | $30,277,212.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +4.35% | +4.19% |
| B/USDT:USDT | below_1h_threshold | +4.08% | +3.92% |
| PROM/USDT:USDT | below_1h_threshold | +2.91% | +2.75% |
| DEXE/USDT:USDT | below_1h_threshold | +1.94% | +1.78% |
| SOXL/USDT:USDT | below_1h_threshold | +1.92% | +1.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
