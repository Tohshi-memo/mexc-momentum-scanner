# Decision Report

- generated_at: 2026-08-30T08:46:19.281477+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13038**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=13038, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.09% | **+1.04%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_BB3S | 8/17 | 47.1% | +0.91% | **+0.43%** |
| LIMIT_10PCT | 5/20 | 25.0% | +0.29% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$774.74** / 初期 $100.00 (+674.74%)
- 確定: 4807件 (Win 1463 / Loss 1584 / Flat 1760) / skip 4792件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $774.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$171.87** / 初期 $100.00 (+71.87%)
- 確定: 2122件 (Win 591 / Loss 518 / Flat 1013) / skip 4327件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0282 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $171.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.50** / 初期 $100.00 (+16.50%)
- 確定: 2080件 (Win 610 / Loss 809 / Flat 661) / pending 3件 / skip 2427件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.50

## 6. Latest Market Context

- 更新: 2026-08-30T08:46:11.224249+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78017.3
- Funnel: target 1023 → liquid 120 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.0 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +82.00% | $40,504,076.62 |
| NIULAI/USDT:USDT | +81.59% | $3,980,942.14 |
| PONS/USDT:USDT | +64.39% | $1,765,849.62 |
| FONE/USDT:USDT | +50.38% | $1,466,618.28 |
| SKR/USDT:USDT | +30.33% | $1,896,222.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +3.52% | +3.60% |
| BTR/USDT:USDT | below_1h_threshold | +3.01% | +3.09% |
| 4/USDT:USDT | below_1h_threshold | +2.41% | +2.49% |
| HNT/USDT:USDT | below_1h_threshold | +2.40% | +2.48% |
| ZKP/USDT:USDT | below_1h_threshold | +2.08% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
