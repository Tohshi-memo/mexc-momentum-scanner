# Decision Report

- generated_at: 2026-08-02T10:06:18.412172+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10152**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10152, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/20 | 20.0% | +7.00% | **+1.40%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.29% | **+0.86%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.88% | **+0.44%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$574.89** / 初期 $100.00 (+474.89%)
- 確定: 3671件 (Win 1166 / Loss 1202 / Flat 1303) / skip 3042件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUMPFUN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.20% 残高後 $574.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1281件 (Win 359 / Loss 298 / Flat 624) / skip 2282件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0869 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.82** / 初期 $100.00 (+12.82%)
- 確定: 960件 (Win 305 / Loss 374 / Flat 281) / pending 6件 / skip 660件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000342 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PUMPFUN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.08% 残高後 $112.82

## 6. Latest Market Context

- 更新: 2026-08-02T10:06:11.141456+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63228.9
- Funnel: target 922 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +57.48% | $13,784,171.92 |
| 1000RATS/USDT:USDT | +38.51% | $30,517,914.76 |
| UAI/USDT:USDT | +32.87% | $24,193,379.46 |
| HOME/USDT:USDT | +30.07% | $3,462,298.11 |
| HYPER/USDT:USDT | +15.36% | $1,109,956.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +1.29% | +1.33% |
| HOME/USDT:USDT | below_1h_threshold | +0.98% | +1.01% |
| ON/USDT:USDT | below_1h_threshold | +0.74% | +0.78% |
| KAITO/USDT:USDT | below_1h_threshold | +0.73% | +0.76% |
| HEI/USDT:USDT | below_1h_threshold | +0.47% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
