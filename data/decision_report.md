# Decision Report

- generated_at: 2026-07-31T18:06:28.764291+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10023**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10023, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.25% | **+0.42%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.49% | **+0.37%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.24% | **+1.48%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.78% | **+1.24%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.65% | **+1.24%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.95% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$562.98** / 初期 $100.00 (+462.98%)
- 確定: 3577件 (Win 1144 / Loss 1168 / Flat 1265) / skip 3007件
- 成長率目線: 平均log +0.000483 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $562.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2156件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0750 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定: 851件 (Win 277 / Loss 335 / Flat 239) / pending 4件 / skip 644件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $112.37

## 6. Latest Market Context

- 更新: 2026-07-31T18:06:18.829184+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63183.0
- Funnel: target 921 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +13.64% | $15,076,513.95 |
| GIGGLE/USDT:USDT | +11.02% | $13,648,784.05 |
| AKE/USDT:USDT | +8.94% | $15,131,472.77 |
| OUSTSTOCK/USDT:USDT | +7.15% | $2,192,723.36 |
| SYN/USDT:USDT | +6.04% | $2,846,872.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OUSTSTOCK/USDT:USDT | below_1h_threshold | +4.08% | +4.13% |
| KOMA/USDT:USDT | below_1h_threshold | +3.34% | +3.39% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +3.14% | +3.19% |
| SNXX/USDT:USDT | below_1h_threshold | +2.67% | +2.72% |
| COINBASE/USDT:USDT | below_1h_threshold | +2.60% | +2.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
