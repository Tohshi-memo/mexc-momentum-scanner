# Decision Report

- generated_at: 2026-09-08T13:51:26.527651+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13996**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.55% / filled 20/20。**
- 全期間 MARKET基準: n=13996, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.38% | **+1.11%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.09% | **+0.76%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.81% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.04% | **+0.02%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.36% | **-0.13%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -1.63% | **-0.41%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | -1.12% | **-0.78%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,007.04** / 初期 $100.00 (+907.04%)
- 確定: 5260件 (Win 1584 / Loss 1707 / Flat 1969) / skip 5297件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,007.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.03** / 初期 $100.00 (+90.03%)
- 確定: 2599件 (Win 722 / Loss 622 / Flat 1255) / skip 4808件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0682 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $190.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.57** / 初期 $100.00 (+20.57%)
- 確定: 2585件 (Win 758 / Loss 976 / Flat 851) / pending 4件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $120.57

## 6. Latest Market Context

- 更新: 2026-09-08T13:51:14.024211+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.84% price=77760.1
- Funnel: target 1070 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +68.89% | $28,812,015.78 |
| BNCSTOCK/USDT:USDT | +31.92% | $2,249,863.75 |
| USELESS/USDT:USDT | +17.86% | $14,301,060.74 |
| FORM/USDT:USDT | +17.47% | $4,913,655.39 |
| AKE/USDT:USDT | +16.38% | $10,507,629.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +4.20% | +5.04% |
| KORU/USDT:USDT | below_1h_threshold | +2.35% | +3.19% |
| BULLA/USDT:USDT | below_1h_threshold | +1.87% | +2.70% |
| HNT/USDT:USDT | below_1h_threshold | +1.76% | +2.60% |
| UAI/USDT:USDT | below_1h_threshold | +0.96% | +1.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
