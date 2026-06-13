# Decision Report

- generated_at: 2026-06-13T00:36:11.750672+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6551**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.64% / filled 20/20。**
- 全期間 MARKET基準: n=6551, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+3.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.64% | **+3.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.64% | **+3.64%** |
| ASK | 20/20 | 100.0% | +3.10% | **+3.10%** |
| LIMIT_1PCT | 13/20 | 65.0% | +2.31% | **+1.50%** |
| LIMIT_ATR | 6/20 | 30.0% | +4.58% | **+1.37%** |
| LIMIT_2PCT | 10/20 | 50.0% | +1.82% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.14% | **+0.04%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.00% | **-0.00%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | -0.92% | **-0.92%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$162.85** / 初期 $100.00 (+62.85%)
- 確定: 1424件 (Win 388 / Loss 464 / Flat 572) / skip 1688件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $162.85

## 4. Latest Market Context

- 更新: 2026-06-13T00:36:08.127943+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63518.2
- Funnel: target 774 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +27.14% | $64,287,278.03 |
| H/USDT:USDT | +12.80% | $29,018,337.99 |
| RIF/USDT:USDT | +12.49% | $1,010,697.02 |
| ORCA/USDT:USDT | +11.82% | $1,652,894.94 |
| AIN/USDT:USDT | +11.77% | $1,905,832.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.05% | +4.10% |
| RIF/USDT:USDT | below_1h_threshold | +3.99% | +4.04% |
| PYTH/USDT:USDT | below_1h_threshold | +2.40% | +2.45% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.28% | +2.33% |
| RENDER/USDT:USDT | below_1h_threshold | +1.57% | +1.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
