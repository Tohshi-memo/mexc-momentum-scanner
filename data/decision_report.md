# Decision Report

- generated_at: 2026-08-01T00:06:10.478542+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10036**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10036, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/20 | 30.0% | +2.08% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.47% | **+1.73%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.52%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.42% | **+1.35%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.53% | **+1.26%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.69% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$570.26** / 初期 $100.00 (+470.26%)
- 確定: 3588件 (Win 1148 / Loss 1171 / Flat 1269) / skip 3009件
- 成長率目線: 平均log +0.000485 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $570.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2168件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0799 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.79** / 初期 $100.00 (+11.79%)
- 確定: 861件 (Win 279 / Loss 340 / Flat 242) / pending 4件 / skip 647件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000275 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.79

## 6. Latest Market Context

- 更新: 2026-08-01T00:06:04.598451+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=62915.0
- Funnel: target 921 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +31.54% | $17,318,967.01 |
| JIMOTHY/USDT:USDT | +22.36% | $1,124,245.06 |
| TLM/USDT:USDT | +21.88% | $1,593,953.21 |
| GIGGLE/USDT:USDT | +18.63% | $20,338,153.79 |
| 1000RATS/USDT:USDT | +15.32% | $16,300,639.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DIA/USDT:USDT | below_1h_threshold | +3.14% | +3.05% |
| 1000RATS/USDT:USDT | below_1h_threshold | +2.12% | +2.03% |
| TLM/USDT:USDT | below_1h_threshold | +1.97% | +1.88% |
| KOMA/USDT:USDT | below_1h_threshold | +1.33% | +1.24% |
| UAI/USDT:USDT | below_1h_threshold | +1.22% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
