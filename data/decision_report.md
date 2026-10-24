# Decision Report

- generated_at: 2026-10-24T02:46:20.535602+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17325**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17325, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +2.11% | **+0.74%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.28% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +3.34% | **+1.43%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.85% | **+0.72%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.14% | **+0.45%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.46% | **+0.41%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.43** / 初期 $100.00 (+1210.43%)
- 確定: 6579件 (Win 1905 / Loss 2100 / Flat 2574) / skip 7307件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,310.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6807件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1081 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5484件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000333 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T02:46:08.068700+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=80902.0
- Funnel: target 1088 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +60.42% | $6,644,104.78 |
| IRYS/USDT:USDT | +54.30% | $100,544,229.99 |
| AXIS/USDT:USDT | +23.23% | $2,197,062.55 |
| SOXS/USDT:USDT | +2.99% | $29,328,824.64 |
| BTW/USDT:USDT | +2.65% | $27,162,521.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TIA/USDT:USDT | below_1h_threshold | +3.52% | +3.52% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +1.86% | +1.86% |
| AKE/USDT:USDT | below_1h_threshold | +1.08% | +1.07% |
| NIL/USDT:USDT | below_1h_threshold | +0.66% | +0.65% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.48% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
