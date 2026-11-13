# Decision Report

- generated_at: 2026-11-13T12:06:40.093158+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18816**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18816, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +6.63% | **+1.66%** |
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 6/20 | 30.0% | +5.14% | **+1.54%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.93% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.76% | **+1.93%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.10% | **+1.26%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.47% | **+0.81%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.94% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,780.87** / 初期 $100.00 (+1680.87%)
- 確定: 7286件 (Win 2100 / Loss 2335 / Flat 2851) / skip 8091件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,780.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$397.44** / 初期 $100.00 (+297.44%)
- 確定: 4827件 (Win 1300 / Loss 1076 / Flat 2451) / skip 7400件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1173 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $397.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000285 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T12:06:19.048651+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=69365.0
- Funnel: target 1084 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +119.12% | $24,903,489.59 |
| BARD/USDT:USDT | +82.43% | $18,475,184.53 |
| KOR/USDT:USDT | +28.18% | $1,838,627.32 |
| ARIA/USDT:USDT | +24.22% | $10,472,029.79 |
| GANG/USDT:USDT | +21.35% | $1,277,326.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GANG/USDT:USDT | below_1h_threshold | +4.61% | +4.51% |
| AKE/USDT:USDT | below_1h_threshold | +4.04% | +3.94% |
| BARD/USDT:USDT | below_1h_threshold | +2.06% | +1.95% |
| MUU/USDT:USDT | below_1h_threshold | +1.89% | +1.78% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.10% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
