# Decision Report

- generated_at: 2026-05-07T08:22:37.335863+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3598**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3598, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +5.43% | **+1.63%** |
| LIMIT_8PCT | 7/20 | 35.0% | +3.83% | **+1.34%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.86% | **+0.30%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.35% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.37% | **+1.85%** |
| MARKET_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.89% | **+1.16%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.55** / 初期 $100.00 (+6.55%)
- 確定: 92件 (Win 32 / Loss 37 / Flat 23) / skip 67件
- 成長率目線: 平均log +0.000689 / 幾何平均 +0.069% per trade / maxDD +2.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORCA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $106.55

## 4. Latest Market Context

- 更新: 2026-05-07T08:22:34.644729+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=81298.9
- Funnel: target 771 → liquid 190 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +202.54% | $1,991,212.03 |
| PENGUIN/USDT:USDT | +113.67% | $2,270,909.02 |
| B3/USDT:USDT | +87.81% | $10,335,154.55 |
| DOGS/USDT:USDT | +61.76% | $13,356,282.52 |
| D/USDT:USDT | +50.53% | $1,113,108.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +3.64% | +3.87% |
| SATO/USDT:USDT | below_1h_threshold | +3.57% | +3.79% |
| B3/USDT:USDT | below_1h_threshold | +2.83% | +3.05% |
| FHE/USDT:USDT | below_1h_threshold | +2.76% | +2.99% |
| NIL/USDT:USDT | below_1h_threshold | +1.96% | +2.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
