# Decision Report

- generated_at: 2026-07-11T16:51:08.696408+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8541**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.83% / filled 20/20。**
- 全期間 MARKET基準: n=8541, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.97% | **+1.58%** |
| LIMIT_ATR | 10/20 | 50.0% | +3.00% | **+1.50%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.95% | **+1.27%** |
| ASK | 10/10 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_BB3S | 2/17 | 11.8% | +8.00% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.06% | **-0.02%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.38% | **-0.19%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | -0.80% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.57** / 初期 $100.00 (+3.57%)
- 確定トレード: 84件 (TP 30 / SL 53 / EXP 1)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.57
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.92** / 初期 $100.00 (+217.92%)
- 確定: 2729件 (Win 862 / Loss 916 / Flat 951) / skip 2373件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_7PCT` TP_HIT account +1.00% 残高後 $317.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1310件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0174 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.12** / 初期 $100.00 (-0.88%)
- 確定: 8件 (Win 1 / Loss 7 / Flat 0) / pending 4件 / skip 0件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.12

## 6. Latest Market Context

- 更新: 2026-07-11T16:51:01.217788+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64133.6
- Funnel: target 863 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +14.66% | $45,368,452.14 |
| EVAA/USDT:USDT | +4.56% | $28,183,797.40 |
| EDGE/USDT:USDT | +3.87% | $2,409,683.51 |
| CLO/USDT:USDT | +3.46% | $1,300,489.86 |
| CASHCAT/USDT:USDT | +3.26% | $1,494,545.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.56% | +4.57% |
| EDGE/USDT:USDT | below_1h_threshold | +3.80% | +3.81% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.26% | +3.27% |
| CLO/USDT:USDT | below_1h_threshold | +3.26% | +3.27% |
| BSB/USDT:USDT | below_1h_threshold | +2.78% | +2.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
