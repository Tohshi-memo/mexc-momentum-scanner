# Decision Report

- generated_at: 2026-07-30T18:01:35.019912+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9911**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9911, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-3.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.30% | **-3.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.02% | **+0.02%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.93% | **-0.33%** |
| LIMIT_3PCT | 19/20 | 95.0% | -0.62% | **-0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +4.61% | **+3.23%** |
| MARKET_LONG | 20/20 | 100.0% | +3.10% | **+3.10%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +5.49% | **+2.74%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +5.25% | **+2.10%** |
| LIMIT_3PCT_LONG | 3/20 | 15.0% | +3.48% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3520件 (Win 1113 / Loss 1147 / Flat 1260) / skip 2952件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2079件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0115 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.62** / 初期 $100.00 (+10.62%)
- 確定: 802件 (Win 261 / Loss 318 / Flat 223) / pending 3件 / skip 593件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000122 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUU/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $110.62

## 6. Latest Market Context

- 更新: 2026-07-30T18:01:27.649078+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64836.5
- Funnel: target 920 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +12.59% | $2,117,773.06 |
| MMT/USDT:USDT | +9.94% | $4,600,436.44 |
| EVAA/USDT:USDT | +7.78% | $2,140,189.88 |
| CAP/USDT:USDT | +4.76% | $3,172,786.55 |
| ESP/USDT:USDT | +4.64% | $5,243,685.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +2.65% | +2.66% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.52% | +1.53% |
| AAPU/USDT:USDT | below_1h_threshold | +1.00% | +1.01% |
| KOMA/USDT:USDT | below_1h_threshold | +0.92% | +0.93% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.80% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
