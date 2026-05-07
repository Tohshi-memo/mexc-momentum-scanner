# Decision Report

- generated_at: 2026-05-07T22:07:33.411311+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3711**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3711, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.70% | **+0.52%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.05% | **+0.42%** |
| LIMIT_BB3S | 4/19 | 21.1% | +1.13% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.22% | **+0.49%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 83件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T22:07:30.037245+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=79596.1
- Funnel: target 765 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +51.09% | $7,358,692.28 |
| NIL/USDT:USDT | +39.06% | $17,262,109.75 |
| TST/USDT:USDT | +26.31% | $5,758,772.10 |
| DYDX/USDT:USDT | +17.33% | $9,457,362.01 |
| NOT/USDT:USDT | +12.58% | $10,269,082.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_1h_threshold | +2.21% | +2.32% |
| B3/USDT:USDT | below_1h_threshold | +1.65% | +1.76% |
| D/USDT:USDT | below_1h_threshold | +1.32% | +1.43% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.11% | +1.22% |
| EVAA/USDT:USDT | below_1h_threshold | +0.82% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
