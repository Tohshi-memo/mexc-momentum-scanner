# Decision Report

- generated_at: 2026-09-13T03:36:33.285732+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14367**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14367, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +0.78% | **+0.39%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 8/20 | 40.0% | -0.04% | **-0.01%** |
| LIMIT_5PCT | 12/20 | 60.0% | -0.35% | **-0.21%** |
| LIMIT_7PCT | 8/20 | 40.0% | -0.80% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +5.02% | **+2.51%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.38% | **+1.32%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5498件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$219.50** / 初期 $100.00 (+119.50%)
- 確定: 2885件 (Win 799 / Loss 676 / Flat 1410) / skip 4893件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $219.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.58** / 初期 $100.00 (+26.58%)
- 確定: 2817件 (Win 838 / Loss 1084 / Flat 895) / pending 6件 / skip 3017件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000426 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.58

## 6. Latest Market Context

- 更新: 2026-09-13T03:36:17.323812+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=77194.5
- Funnel: target 1068 → liquid 126 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 99.2 >= 65=1, 4h RSI 83.3 >= 65=1, 4h RSI 68.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +517.07% | $76,743,703.88 |
| POWR/USDT:USDT | +46.86% | $1,683,793.58 |
| ZCAT/USDT:USDT | +43.36% | $1,177,989.48 |
| LONGXIA/USDT:USDT | +21.43% | $9,867,856.57 |
| STORJ/USDT:USDT | +17.23% | $19,052,729.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +3.38% | +3.46% |
| FLOCK/USDT:USDT | below_1h_threshold | +3.31% | +3.40% |
| ILV/USDT:USDT | below_1h_threshold | +2.90% | +2.99% |
| USELESS/USDT:USDT | below_1h_threshold | +2.69% | +2.78% |
| REZ/USDT:USDT | below_1h_threshold | +1.61% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
