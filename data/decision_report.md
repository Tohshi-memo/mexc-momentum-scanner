# Decision Report

- generated_at: 2026-10-28T05:41:25.245332+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17691**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=17691, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.45% | **+0.69%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.70% | **+0.68%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,532.91** / 初期 $100.00 (+1432.91%)
- 確定: 6760件 (Win 1968 / Loss 2170 / Flat 2622) / skip 7492件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,532.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$357.78** / 初期 $100.00 (+257.78%)
- 確定: 4220件 (Win 1148 / Loss 967 / Flat 2105) / skip 6882件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0763 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $357.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5852件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T05:41:11.161901+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=80917.3
- Funnel: target 1083 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +63.56% | $7,004,603.25 |
| SI/USDT:USDT | +50.15% | $1,538,184.25 |
| APR/USDT:USDT | +22.74% | $6,813,477.73 |
| PONS/USDT:USDT | +21.87% | $2,881,037.02 |
| BLESS/USDT:USDT | +18.57% | $1,251,127.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HAEDAL/USDT:USDT | below_1h_threshold | +3.43% | +3.49% |
| BLESS/USDT:USDT | below_1h_threshold | +3.06% | +3.12% |
| PONS/USDT:USDT | below_1h_threshold | +1.49% | +1.55% |
| USELESS/USDT:USDT | below_1h_threshold | +0.56% | +0.62% |
| BCH/USDT:USDT | below_1h_threshold | +0.22% | +0.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
