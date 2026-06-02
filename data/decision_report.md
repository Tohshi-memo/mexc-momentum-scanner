# Decision Report

- generated_at: 2026-06-02T00:32:20.294406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5380**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=5380, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.59% | **+1.59%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.46% | **+0.73%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.10% | **+0.04%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.40% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 897件 (Win 208 / Loss 270 / Flat 419) / skip 1044件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-02T00:32:17.365119+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=71245.7
- Funnel: target 774 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +60.95% | $8,013,963.16 |
| MYX/USDT:USDT | +14.44% | $6,678,967.21 |
| WLD/USDT:USDT | +12.75% | $138,675,895.04 |
| UB/USDT:USDT | +12.28% | $2,413,072.35 |
| ORDI/USDT:USDT | +11.28% | $6,490,045.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.96% | +5.16% |
| H/USDT:USDT | below_1h_threshold | +4.47% | +4.67% |
| LAB/USDT:USDT | below_1h_threshold | +4.08% | +4.28% |
| NEX/USDT:USDT | below_1h_threshold | +1.83% | +2.04% |
| CHZ/USDT:USDT | below_1h_threshold | +1.73% | +1.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
