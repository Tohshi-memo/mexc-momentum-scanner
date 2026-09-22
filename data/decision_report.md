# Decision Report

- generated_at: 2026-09-22T22:06:34.530720+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15367**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15367, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_BB3S | 9/15 | 60.0% | +1.34% | **+0.80%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.32% | **+0.79%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.83% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.38% | **+1.66%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.54% | **+1.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,155.82** / 初期 $100.00 (+1055.82%)
- 確定: 5846件 (Win 1729 / Loss 1880 / Flat 2237) / skip 6082件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSEBOOK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,155.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5425件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.24** / 初期 $100.00 (+22.24%)
- 確定: 3116件 (Win 915 / Loss 1222 / Flat 979) / pending 4件 / skip 3724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000095 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `MARKET` EXPIRED account +0.08% 残高後 $122.24

## 6. Latest Market Context

- 更新: 2026-09-22T22:06:15.313350+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=86115.3
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUSEBOOK/USDT:USDT | +35.74% | $1,025,750.22 |
| FOLKS/USDT:USDT | +22.33% | $2,049,574.30 |
| DRIFT/USDT:USDT | +21.80% | $1,583,982.95 |
| 4/USDT:USDT | +21.03% | $2,187,921.90 |
| USELESS/USDT:USDT | +16.71% | $10,296,964.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KERNEL/USDT:USDT | below_1h_threshold | +1.89% | +1.92% |
| SAGA/USDT:USDT | below_1h_threshold | +0.89% | +0.92% |
| TUT/USDT:USDT | below_1h_threshold | +0.74% | +0.78% |
| 4/USDT:USDT | below_1h_threshold | +0.74% | +0.77% |
| USELESS/USDT:USDT | below_1h_threshold | +0.58% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
