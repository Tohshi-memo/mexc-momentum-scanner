# Decision Report

- generated_at: 2026-07-15T11:21:13.372181+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8736**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8736, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 10/20 | 50.0% | +4.72% | **+2.36%** |
| LIMIT_8PCT | 9/20 | 45.0% | +5.23% | **+2.36%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.93% | **+0.97%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.71% | **+3.15%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.75% | **+3.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +3.28% | **+1.82%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.76% | **+1.79%** |

## 2. $100 Live Portfolio

- 残高: **$102.71** / 初期 $100.00 (+2.71%)
- 確定トレード: 97件 (TP 33 / SL 62 / EXP 2)
- 最新: DODO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.63** / 初期 $100.00 (+242.63%)
- 確定: 2879件 (Win 901 / Loss 935 / Flat 1043) / skip 2418件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.82% 残高後 $342.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.15** / 初期 $100.00 (+6.15%)
- 確定: 704件 (Win 165 / Loss 165 / Flat 374) / skip 1443件
- 成長率目線: 平均log +0.000085 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0965 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $106.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 60件 (Win 19 / Loss 39 / Flat 2) / pending 2件 / skip 149件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000340 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T11:21:08.478618+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64639.9
- Funnel: target 870 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +199.42% | $17,560,498.33 |
| DODO/USDT:USDT | +37.35% | $10,823,995.05 |
| AEHRSTOCK/USDT:USDT | +31.98% | $3,934,000.49 |
| US/USDT:USDT | +31.35% | $4,624,726.15 |
| XEC/USDT:USDT | +15.51% | $1,370,470.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 0G/USDT:USDT | below_1h_threshold | +2.82% | +2.81% |
| KAITO/USDT:USDT | below_1h_threshold | +1.18% | +1.17% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.10% | +1.09% |
| US/USDT:USDT | below_1h_threshold | +1.00% | +0.99% |
| AEHRSTOCK/USDT:USDT | below_1h_threshold | +0.95% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
