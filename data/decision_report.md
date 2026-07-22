# Decision Report

- generated_at: 2026-07-22T21:31:16.521367+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9323**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9323, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.24% | **+0.79%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.90% | **+0.36%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.24% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.39% | **+2.88%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.82% | **+2.82%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.43% | **+1.58%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.74% | **+1.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$444.06** / 初期 $100.00 (+344.06%)
- 確定: 3308件 (Win 1046 / Loss 1065 / Flat 1197) / skip 2576件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $444.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1573件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1539 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.37** / 初期 $100.00 (+1.37%)
- 確定: 426件 (Win 142 / Loss 177 / Flat 107) / pending 2件 / skip 373件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000404 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.37

## 6. Latest Market Context

- 更新: 2026-07-22T21:31:11.238948+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65876.9
- Funnel: target 890 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +65.00% | $4,956,249.07 |
| BANK/USDT:USDT | +19.23% | $105,701,004.27 |
| BROCCOLIF3B/USDT:USDT | +18.13% | $1,773,618.77 |
| ON/USDT:USDT | +12.21% | $1,754,940.55 |
| RIF/USDT:USDT | +10.74% | $4,157,743.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.25% | +3.26% |
| MUU/USDT:USDT | below_1h_threshold | +3.15% | +3.17% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.59% |
| SNXX/USDT:USDT | below_1h_threshold | +2.37% | +2.39% |
| KORU/USDT:USDT | below_1h_threshold | +1.87% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
