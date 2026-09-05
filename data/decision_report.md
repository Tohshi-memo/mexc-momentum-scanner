# Decision Report

- generated_at: 2026-09-05T09:36:27.970316+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13720**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13720, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.56% | **+1.28%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.20% | **+0.88%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 203件 (TP 75 / SL 123 / EXP 5)
- 最新: NIULAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$854.06** / 初期 $100.00 (+754.06%)
- 確定: 5027件 (Win 1517 / Loss 1646 / Flat 1864) / skip 5254件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.50% 残高後 $854.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.49** / 初期 $100.00 (+88.49%)
- 確定: 2465件 (Win 694 / Loss 586 / Flat 1185) / skip 4666件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0834 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.62** / 初期 $100.00 (+18.62%)
- 確定: 2348件 (Win 701 / Loss 901 / Flat 746) / pending 4件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $118.62

## 6. Latest Market Context

- 更新: 2026-09-05T09:36:16.194650+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=79666.0
- Funnel: target 1050 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +119.78% | $10,226,780.20 |
| 4/USDT:USDT | +52.52% | $18,326,674.66 |
| B/USDT:USDT | +44.26% | $2,316,085.98 |
| AKE/USDT:USDT | +40.22% | $14,893,825.68 |
| NIULAI/USDT:USDT | +39.17% | $1,569,248.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.55% | +3.49% |
| TUT/USDT:USDT | below_1h_threshold | +3.05% | +2.99% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.97% | +1.91% |
| FLOKI/USDT:USDT | below_1h_threshold | +1.64% | +1.58% |
| CAKE/USDT:USDT | below_1h_threshold | +1.63% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
