# Decision Report

- generated_at: 2026-07-17T16:41:17.219770+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8868**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8868, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.71% | **+1.22%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.92% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +5.97% | **+1.49%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.20% | **+1.21%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.10% | **+1.08%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$355.50** / 初期 $100.00 (+255.50%)
- 確定: 2983件 (Win 929 / Loss 950 / Flat 1104) / skip 2446件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LRC/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $355.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$109.85** / 初期 $100.00 (+9.85%)
- 確定: 830件 (Win 197 / Loss 172 / Flat 461) / skip 1449件
- 成長率目線: 平均log +0.000113 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0650 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $109.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.06** / 初期 $100.00 (-0.94%)
- 確定: 134件 (Win 42 / Loss 75 / Flat 17) / pending 6件 / skip 203件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.06

## 6. Latest Market Context

- 更新: 2026-07-17T16:41:10.785339+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63390.2
- Funnel: target 885 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +4.52% | $1,080,459.42 |
| RESOLV/USDT:USDT | +3.04% | $1,763,271.55 |
| KIOXIASTOCK/USDT:USDT | +2.70% | $1,439,063.16 |
| H/USDT:USDT | +2.36% | $1,129,249.52 |
| LAB/USDT:USDT | +2.34% | $10,017,939.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +4.52% | +4.59% |
| RESOLV/USDT:USDT | below_1h_threshold | +2.90% | +2.97% |
| ALABSTOCK/USDT:USDT | below_1h_threshold | +2.46% | +2.52% |
| H/USDT:USDT | below_1h_threshold | +2.36% | +2.43% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.09% | +2.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
