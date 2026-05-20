# Decision Report

- generated_at: 2026-05-20T19:13:58.370793+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4573**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4573, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_10PCT | 5/20 | 25.0% | -1.60% | **-0.40%** |
| LIMIT_9PCT | 5/20 | 25.0% | -1.60% | **-0.40%** |
| LIMIT_6PCT | 11/20 | 55.0% | -0.79% | **-0.43%** |
| LIMIT_7PCT | 9/20 | 45.0% | -0.98% | **-0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.41% | **+1.81%** |
| LIMIT_BB3S_LONG | 6/12 | 50.0% | +3.11% | **+1.56%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.69% | **+1.01%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.87** / 初期 $100.00 (+23.87%)
- 確定: 535件 (Win 137 / Loss 179 / Flat 219) / skip 599件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $123.87

## 4. Latest Market Context

- 更新: 2026-05-20T19:13:51.942420+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77371.4
- Funnel: target 759 → liquid 127 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1, 4h RSI 82.1 >= 65=1, 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +76.76% | $52,020,040.64 |
| EDEN/USDT:USDT | +34.00% | $27,521,713.45 |
| NIL/USDT:USDT | +15.47% | $1,730,820.05 |
| LAB/USDT:USDT | +11.59% | $44,290,669.32 |
| JTO/USDT:USDT | +9.17% | $1,448,173.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +4.26% | +4.27% |
| BEAT/USDT:USDT | below_1h_threshold | +3.65% | +3.65% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.58% | +3.58% |
| LAB/USDT:USDT | below_1h_threshold | +2.30% | +2.31% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.14% | +2.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
