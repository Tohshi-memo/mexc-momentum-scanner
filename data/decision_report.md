# Decision Report

- generated_at: 2026-08-03T22:06:21.977472+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10252**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10252, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |
| LIMIT_4PCT | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_BB3S | 6/17 | 35.3% | +0.87% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.80% | **+0.99%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$590.53** / 初期 $100.00 (+490.53%)
- 確定: 3710件 (Win 1176 / Loss 1214 / Flat 1320) / skip 3103件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $590.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2380件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0431 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.71** / 初期 $100.00 (+16.71%)
- 確定: 1028件 (Win 331 / Loss 398 / Flat 299) / pending 6件 / skip 694件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000502 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.71

## 6. Latest Market Context

- 更新: 2026-08-03T22:06:14.593400+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=63424.1
- Funnel: target 929 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +17.76% | $2,259,187.36 |
| PIPPIN/USDT:USDT | +14.74% | $5,621,228.00 |
| PLTRSTOCK/USDT:USDT | +12.64% | $2,481,126.44 |
| KORU/USDT:USDT | +10.07% | $16,394,083.45 |
| ON/USDT:USDT | +9.45% | $2,681,440.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +2.19% | +2.40% |
| UAI/USDT:USDT | below_1h_threshold | +1.22% | +1.43% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.34% |
| MUU/USDT:USDT | below_1h_threshold | +1.08% | +1.30% |
| DEXE/USDT:USDT | below_1h_threshold | +0.80% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
