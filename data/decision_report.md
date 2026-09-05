# Decision Report

- generated_at: 2026-09-05T19:06:22.947925+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13772**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13772, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.47% | **+0.42%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.23% | **+0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.33% | **+0.18%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.09% | **+0.06%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.11% | **+0.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$858.94** / 初期 $100.00 (+758.94%)
- 確定: 5078件 (Win 1523 / Loss 1656 / Flat 1899) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $858.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.98** / 初期 $100.00 (+87.98%)
- 確定: 2517件 (Win 701 / Loss 595 / Flat 1221) / skip 4666件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0379 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $187.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.63** / 初期 $100.00 (+19.63%)
- 確定: 2389件 (Win 709 / Loss 907 / Flat 773) / pending 1件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000229 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.63

## 6. Latest Market Context

- 更新: 2026-09-05T19:06:11.478768+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=79897.8
- Funnel: target 1050 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +25.50% | $24,660,658.35 |
| SUSHI/USDT:USDT | +23.41% | $1,264,720.41 |
| MAGMA/USDT:USDT | +16.88% | $2,511,905.31 |
| BASECAT/USDT:USDT | +16.78% | $2,101,946.85 |
| NIULAI/USDT:USDT | +11.70% | $2,825,758.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +4.77% | +4.84% |
| FLOCK/USDT:USDT | below_1h_threshold | +2.93% | +3.01% |
| SUSHI/USDT:USDT | below_1h_threshold | +1.51% | +1.59% |
| AR/USDT:USDT | below_1h_threshold | +1.36% | +1.44% |
| PONS/USDT:USDT | below_1h_threshold | +1.17% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
