# Decision Report

- generated_at: 2026-09-13T02:31:24.880384+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14350**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=14350, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_7PCT | 8/20 | 40.0% | +2.20% | **+0.88%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.72% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.87% | **+1.55%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.46% | **+1.32%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.87% | **+1.29%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.48% | **+1.18%** |
| LIMIT_BB3S_LONG | 6/12 | 50.0% | +2.15% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5481件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$219.23** / 初期 $100.00 (+119.23%)
- 確定: 2868件 (Win 795 / Loss 669 / Flat 1404) / skip 4893件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1446 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: REZ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $219.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.07** / 初期 $100.00 (+26.07%)
- 確定: 2801件 (Win 833 / Loss 1077 / Flat 891) / pending 3件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000469 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: REZ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.07

## 6. Latest Market Context

- 更新: 2026-09-13T02:31:12.096000+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77224.3
- Funnel: target 1068 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +114.67% | $67,195,947.68 |
| POWR/USDT:USDT | +45.91% | $1,279,763.15 |
| ZCAT/USDT:USDT | +32.40% | $1,126,259.95 |
| ALCH/USDT:USDT | +18.35% | $2,671,937.91 |
| STORJ/USDT:USDT | +17.02% | $19,268,352.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +5.00% | +5.08% |
| ZCAT/USDT:USDT | below_1h_threshold | +2.97% | +3.05% |
| STX/USDT:USDT | below_1h_threshold | +1.66% | +1.74% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +0.82% | +0.90% |
| AKE/USDT:USDT | below_1h_threshold | +0.48% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
