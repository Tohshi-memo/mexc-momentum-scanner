# Decision Report

- generated_at: 2026-05-28T00:44:23.724594+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4947**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=4947, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +3.67% | **+2.38%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.40% | **+1.92%** |
| LIMIT_4PCT | 10/20 | 50.0% | +2.87% | **+1.44%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.02% | **+0.81%** |
| LIMIT_5PCT | 4/20 | 20.0% | +3.25% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +3.62% | **+1.81%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +4.73% | **+1.66%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.08% | **+1.23%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.65% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$97.15** / 初期 $100.00 (-2.85%)
- 確定トレード: 68件 (TP 19 / SL 46 / EXP 3)
- 最新: B/USDT:USDT TP_HIT PnL +6.46% 残高後 $97.15
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 824件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T00:44:21.375745+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=74527.9
- Funnel: target 773 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +36.30% | $6,731,999.02 |
| NBISSTOCK/USDT:USDT | +12.83% | $1,471,448.68 |
| XLM/USDT:USDT | +6.39% | $66,159,825.88 |
| RIVER/USDT:USDT | +4.23% | $13,248,683.71 |
| GENIUS/USDT:USDT | +4.21% | $1,427,167.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +4.95% | +4.80% |
| BEAT/USDT:USDT | below_1h_threshold | +4.31% | +4.16% |
| UB/USDT:USDT | below_1h_threshold | +2.03% | +1.88% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.87% | +1.72% |
| SNOWSTOCK/USDT:USDT | below_1h_threshold | +1.50% | +1.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
