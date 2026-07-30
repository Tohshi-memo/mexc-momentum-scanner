# Decision Report

- generated_at: 2026-07-30T17:16:22.902409+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9908**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9908, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.70% | **-2.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.02% | **+0.31%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.03% | **+0.02%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.81% | **-0.24%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.60% | **-0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.97% | **+2.78%** |
| MARKET_LONG | 20/20 | 100.0% | +2.70% | **+2.70%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +4.47% | **+2.24%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +3.67% | **+1.28%** |
| LIMIT_FIB1272_LONG | 2/20 | 10.0% | +2.82% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2949件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2076件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0083 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.82** / 初期 $100.00 (+10.82%)
- 確定: 801件 (Win 261 / Loss 317 / Flat 223) / pending 4件 / skip 590件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000122 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $110.82

## 6. Latest Market Context

- 更新: 2026-07-30T17:16:15.898333+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64772.3
- Funnel: target 920 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +9.36% | $2,865,549.17 |
| MMT/USDT:USDT | +7.17% | $3,648,161.97 |
| ROBO/USDT:USDT | +6.42% | $1,787,649.09 |
| EVAA/USDT:USDT | +5.73% | $1,922,544.46 |
| UAI/USDT:USDT | +5.01% | $23,177,703.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.83% |
| BEAT/USDT:USDT | below_1h_threshold | +2.22% | +2.25% |
| MSFU/USDT:USDT | below_1h_threshold | +2.10% | +2.13% |
| ESP/USDT:USDT | below_1h_threshold | +2.00% | +2.02% |
| AEON1/USDT:USDT | below_1h_threshold | +1.98% | +2.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
