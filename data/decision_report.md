# Decision Report

- generated_at: 2026-07-26T06:31:21.428639+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9560**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=9560, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.86% | **+0.52%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.88% | **+0.45%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.48% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$464.08** / 初期 $100.00 (+364.08%)
- 確定: 3388件 (Win 1077 / Loss 1099 / Flat 1212) / skip 2733件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $464.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.20** / 初期 $100.00 (+39.20%)
- 確定: 1213件 (Win 337 / Loss 269 / Flat 607) / skip 1758件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1241 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $139.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.24** / 初期 $100.00 (+9.24%)
- 確定: 603件 (Win 205 / Loss 230 / Flat 168) / pending 3件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000604 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $109.24

## 6. Latest Market Context

- 更新: 2026-07-26T06:31:14.387307+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=64275.0
- Funnel: target 898 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +69.83% | $36,232,163.46 |
| PIEVERSE/USDT:USDT | +40.45% | $1,012,424.18 |
| DIA/USDT:USDT | +32.12% | $1,775,518.18 |
| BANK/USDT:USDT | +20.97% | $95,321,043.53 |
| SHIB/USDT:USDT | +17.74% | $65,473,307.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.32% | +3.50% |
| VVV/USDT:USDT | below_1h_threshold | +2.47% | +2.64% |
| LIGHT/USDT:USDT | below_1h_threshold | +2.09% | +2.27% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.04% | +2.21% |
| EUL/USDT:USDT | below_1h_threshold | +0.78% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
