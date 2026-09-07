# Decision Report

- generated_at: 2026-09-07T22:06:12.173035+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13914**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13914, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.55% | **+0.27%** |
| LIMIT_BB3S | 3/20 | 15.0% | +1.74% | **+0.26%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.95% | **+1.62%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.04% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +5.33% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$923.58** / 初期 $100.00 (+823.58%)
- 確定: 5187件 (Win 1555 / Loss 1684 / Flat 1948) / skip 5288件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $923.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4753件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定: 2505件 (Win 738 / Loss 940 / Flat 827) / pending 4件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000293 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $121.13

## 6. Latest Market Context

- 更新: 2026-09-07T22:06:05.012319+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79163.9
- Funnel: target 1062 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +23.41% | $5,510,632.46 |
| MEMEROBINHOOD/USDT:USDT | +16.04% | $5,488,134.21 |
| SOPH/USDT:USDT | +12.60% | $1,681,281.68 |
| AERO/USDT:USDT | +12.55% | $3,535,171.19 |
| INJ/USDT:USDT | +9.45% | $41,582,346.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CP/USDT:USDT | below_1h_threshold | +2.67% | +2.62% |
| XAN/USDT:USDT | below_1h_threshold | +0.91% | +0.87% |
| AR/USDT:USDT | below_1h_threshold | +0.80% | +0.75% |
| ACE/USDT:USDT | below_1h_threshold | +0.78% | +0.73% |
| AKE/USDT:USDT | below_1h_threshold | +0.68% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
