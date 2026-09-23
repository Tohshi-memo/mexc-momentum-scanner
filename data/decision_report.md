# Decision Report

- generated_at: 2026-09-23T18:11:34.184798+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15442**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=15442, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.44% | **+1.95%** |
| LIMIT_5PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.21% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.22% | **+1.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.71% | **+1.02%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.14% | **+0.08%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5896件 (Win 1739 / Loss 1890 / Flat 2267) / skip 6107件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.39** / 初期 $100.00 (+152.39%)
- 確定: 3389件 (Win 933 / Loss 790 / Flat 1666) / skip 5464件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0626 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $252.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3776件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000242 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T18:11:18.686969+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=84196.8
- Funnel: target 1061 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +8.57% | $3,652,765.50 |
| PENDLE/USDT:USDT | +5.93% | $2,853,013.60 |
| ZRO/USDT:USDT | +5.76% | $10,723,816.56 |
| BR/USDT:USDT | +5.36% | $6,241,921.50 |
| FIGHT/USDT:USDT | +4.65% | $1,196,742.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +2.47% | +2.57% |
| SOXL/USDT:USDT | below_1h_threshold | +2.24% | +2.34% |
| LSK/USDT:USDT | below_1h_threshold | +1.94% | +2.04% |
| NIL/USDT:USDT | below_1h_threshold | +1.77% | +1.87% |
| BTW/USDT:USDT | below_1h_threshold | +1.25% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
