# Decision Report

- generated_at: 2026-08-30T02:06:26.351112+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12991**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12991, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.13% | **+0.90%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.77% | **+0.69%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.52% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$769.61** / 初期 $100.00 (+669.61%)
- 確定: 4761件 (Win 1450 / Loss 1566 / Flat 1745) / skip 4791件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $769.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$169.94** / 初期 $100.00 (+69.94%)
- 確定: 2075件 (Win 577 / Loss 502 / Flat 996) / skip 4327件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0905 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $169.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.35** / 初期 $100.00 (+15.35%)
- 確定: 2040件 (Win 598 / Loss 794 / Flat 648) / pending 3件 / skip 2421件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000425 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $115.35

## 6. Latest Market Context

- 更新: 2026-08-30T02:06:15.111397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78084.7
- Funnel: target 1023 → liquid 114 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +35.82% | $11,917,575.99 |
| FONE/USDT:USDT | +34.61% | $1,239,214.35 |
| HNT/USDT:USDT | +30.00% | $25,412,376.16 |
| PONS/USDT:USDT | +26.10% | $1,282,214.52 |
| CYS/USDT:USDT | +13.75% | $1,591,178.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HNT/USDT:USDT | below_1h_threshold | +4.26% | +4.22% |
| 4/USDT:USDT | below_1h_threshold | +3.44% | +3.39% |
| BTR/USDT:USDT | below_1h_threshold | +2.43% | +2.39% |
| PONS/USDT:USDT | below_1h_threshold | +1.78% | +1.74% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.55% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
