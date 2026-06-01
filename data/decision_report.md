# Decision Report

- generated_at: 2026-06-01T23:59:56.212041+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5374**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=5374, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.57% | **+1.57%** |
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.63% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.25% | **+0.21%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.40% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 1041件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T23:59:53.362518+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=71409.8
- Funnel: target 773 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +34.04% | $6,934,941.72 |
| WLD/USDT:USDT | +12.93% | $138,449,019.32 |
| SLX/USDT:USDT | +12.62% | $12,435,433.83 |
| UB/USDT:USDT | +12.43% | $2,391,159.43 |
| MYX/USDT:USDT | +12.27% | $6,666,605.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +3.92% | +3.88% |
| PLAY/USDT:USDT | below_1h_threshold | +3.06% | +3.01% |
| GRASS/USDT:USDT | below_1h_threshold | +2.68% | +2.63% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.36% | +2.31% |
| MERL/USDT:USDT | below_1h_threshold | +2.13% | +2.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
